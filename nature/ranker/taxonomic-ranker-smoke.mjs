import fs from "node:fs";
import vm from "node:vm";

const htmlPath = new URL("./taxonomic-ranker.html", import.meta.url);
const html = fs.readFileSync(htmlPath, "utf8");
const failures = [];

function assert(condition, message) {
  if (!condition) failures.push(message);
}

assert(/<!doctype html>/i.test(html), "HTML doctype is missing.");
assert(!/<script\s+src=/i.test(html), "External script tag found.");
assert(!/<link[^>]+rel=["']stylesheet["']/i.test(html), "External stylesheet link found.");
assert(!/React|Vue|Svelte|Angular/i.test(html), "Framework reference found.");
assert(!/Available groups|tier-board|data-tier-select/i.test(html), "Old all-groups UI text found.");
assert(/Tier list/.test(html), "Tier list heading is missing.");
assert(/id="save-status">Checking local saves<\/span>/.test(html), "Initial save status should not claim a completed save.");

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map((match) => match[1]);
assert(scripts.length === 1, `Expected one inline script, found ${scripts.length}.`);

if (scripts[0]) {
  try {
    new Function(scripts[0]);
  } catch (error) {
    failures.push(`Inline script does not parse: ${error.message}`);
  }
}

class FakeClassList {
  constructor() {
    this.names = new Set();
  }

  add(...names) {
    names.forEach((name) => this.names.add(name));
  }

  remove(...names) {
    names.forEach((name) => this.names.delete(name));
  }

  toggle(name, force) {
    if (force === undefined) {
      if (this.names.has(name)) {
        this.names.delete(name);
        return false;
      }
      this.names.add(name);
      return true;
    }
    if (force) this.names.add(name);
    else this.names.delete(name);
    return Boolean(force);
  }
}

class FakeElement {
  constructor(selector = "") {
    this.selector = selector;
    this.dataset = {};
    this.classList = new FakeClassList();
    this.style = {};
    this.attributes = {};
    this.children = [];
    this.textContent = "";
    this.innerHTML = "";
    this.value = "";
    this.hidden = false;
    this.disabled = false;
  }

  setAttribute(name, value) {
    this.attributes[name] = String(value);
  }

  addEventListener() {}

  select() {}

  matches(selector) {
    return this.selector === selector;
  }

  closest() {
    return null;
  }

  querySelectorAll() {
    return [];
  }
}

const elementCache = new Map();
const viewButtons = ["rank", "results", "data"].map((view) => {
  const button = new FakeElement(`[data-view-button="${view}"]`);
  button.dataset.viewButton = view;
  return button;
});

const documentStub = {
  documentElement: new FakeElement("html"),
  querySelector(selector) {
    if (!elementCache.has(selector)) elementCache.set(selector, new FakeElement(selector));
    return elementCache.get(selector);
  },
  querySelectorAll(selector) {
    if (selector === "[data-view-button]") return viewButtons;
    if (selector === "img[data-wiki-image]:not([src])") return [];
    if (selector === ".dropzone.drag-over") return [];
    return [];
  },
  addEventListener() {}
};

const storage = new Map();
const localStorageStub = {
  getItem(key) {
    return storage.has(key) ? storage.get(key) : null;
  },
  setItem(key, value) {
    storage.set(key, String(value));
  },
  removeItem(key) {
    storage.delete(key);
  }
};

function makeContext(search = "") {
  const context = vm.createContext({
    console,
    document: documentStub,
    localStorage: localStorageStub,
    navigator: { clipboard: { writeText: async () => {} } },
    setTimeout,
    clearTimeout,
    fetch: async () => ({ ok: false }),
    location: { search },
    URL,
    URLSearchParams,
    globalThis: {}
  });
  context.globalThis = context;
  return context;
}

const smokeScript = `
${scripts[0] || ""}

const smokeResults = [];
function smokeAssert(condition, message) {
  if (!condition) smokeResults.push(message);
}

smokeAssert(nodes.has("life"), "life node was not indexed.");
smokeAssert(TAXONOMY.children.every((child) => child.rank === "kingdom"), "root children are not kingdom-level cards.");
smokeAssert([...nodes.values()].some((node) => node.rank === "phylum"), "no phylum-level nodes found.");
smokeAssert([...nodes.values()].some((node) => node.rank === "class"), "no class-level nodes found.");
smokeAssert([...nodes.values()].some((node) => node.rank === "order"), "no order-level nodes found.");
smokeAssert([...nodes.values()].filter((node) => node.rank === "order").length >= 50, "order-level starter set is too small.");

const orderPaths = [...nodes.values()]
  .filter((node) => node.rank === "order")
  .map((node) => getPath(node.id).map((pathNode) => pathNode.rank).join(">"));
smokeAssert(orderPaths.every((path) => path === "root>kingdom>phylum>class>order"), "at least one order path is not top-down root>kingdom>phylum>class>order.");

const initialRankingKeys = Object.keys(state.rankings);
smokeAssert(initialRankingKeys.length === 1 && initialRankingKeys[0] === "life", "initial render should only create the current root ranking.");

const lifeRanking = ensureRanking("life");
smokeAssert(lifeRanking.unranked.includes("animalia"), "animalia did not start unranked.");
state.rankings.life = { unranked: [], ranked: ["animalia"] };
ensureRanking("life");
smokeAssert(state.rankings.life.tiers.b.includes("animalia"), "legacy ranked data did not migrate into B tier.");
state.rankings.life = { unranked: TAXONOMY.children.map((child) => child.id), tiers: emptyTiers() };
ensureRanking("life");
smokeAssert(document.querySelector("#save-status").textContent === "Local saves ready", "initial save status did not verify localStorage readiness.");
moveTaxon("animalia", "tier:s", 0);
smokeAssert(state.rankings.life.tiers.s[0] === "animalia", "moveTaxon did not place animalia first in S tier.");
smokeAssert(!state.rankings.life.unranked.includes("animalia"), "moveTaxon left animalia in unranked.");
const storedAfterMove = JSON.parse(localStorage.getItem(STORAGE_KEY));
smokeAssert(storedAfterMove.rankings.life.tiers.s[0] === "animalia", "moveTaxon did not persist tier order to localStorage.");
smokeAssert(document.querySelector("#save-status").textContent === "Saved locally", "save status did not confirm successful persistence.");

state.currentGroupId = "animalia";
render();
smokeAssert(document.querySelector("#context-title").textContent === "Animals", "drill-down context did not render Animals.");
const beforeResultsKeys = Object.keys(state.rankings).sort().join(",");
activeView = "results";
render();
const afterResultsKeys = Object.keys(state.rankings).sort().join(",");
smokeAssert(beforeResultsKeys === afterResultsKeys, "results view created extra empty rankings.");

state.currentGroupId = "animalia";
clearCurrentGroup();
smokeAssert(state.rankings.animalia.unranked.length === nodes.get("animalia").children.length, "clearCurrentGroup did not restore all animal phyla.");
smokeAssert(countPlaced(state.rankings.animalia) === 0, "clearCurrentGroup left placed animal cards.");

placeLeftovers();
smokeAssert(state.rankings.animalia.unranked.length === 0, "placeLeftovers did not empty unranked.");
smokeAssert(state.rankings.animalia.tiers.f.length === nodes.get("animalia").children.length, "placeLeftovers did not send all leftovers to F tier.");

renderData();
const exported = JSON.parse(document.querySelector("#data-box").value);
smokeAssert(exported.rankings.life.tiers.s.includes("animalia"), "export is missing root tier data.");
smokeAssert(exported.rankings.animalia.tiers.f.length === nodes.get("animalia").children.length, "export is missing drill-down tier data.");

globalThis.__smokeResults = smokeResults;
`;

if (scripts[0]) {
  try {
    const context = makeContext();
    vm.runInContext(smokeScript, context, { filename: "taxonomic-ranker-smoke.vm.js", timeout: 2000 });
    failures.push(...context.__smokeResults);
  } catch (error) {
    failures.push(`Runtime smoke test failed: ${error.stack || error.message}`);
  }

  try {
    const builtInContext = makeContext("?smoke=1");
    vm.runInContext(scripts[0], builtInContext, { filename: "taxonomic-ranker-built-in-smoke.vm.js", timeout: 2000 });
    const smokeState = builtInContext.document.documentElement.dataset.smoke;
    const smokeDetails = builtInContext.document.documentElement.dataset.smokeDetails;
    assert(smokeState === "pass", `Built-in smoke mode did not pass: ${smokeDetails || smokeState || "no result"}`);
  } catch (error) {
    failures.push(`Built-in smoke mode failed: ${error.stack || error.message}`);
  }
}

if (failures.length) {
  console.error(failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log("taxonomic-ranker smoke tests passed");
