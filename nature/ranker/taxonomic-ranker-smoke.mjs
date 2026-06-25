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
assert(/id="save-png-button">Save PNG<\/button>/.test(html), "Save PNG control is missing.");
assert(!/data-view-button="results"/.test(html), "Results tab should not be in the top controls.");
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
const viewButtons = ["rank", "data"].map((view) => {
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
    if (selector === "img[data-taxon-image]:not([src])") return [];
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

function makeContext(search = "", hash = "") {
  const locationStub = {
    hash,
    href: `http://127.0.0.1/taxonomic-ranker.html${search}${hash}`,
    search
  };
  const setUrl = (url) => {
    const parsed = new URL(String(url), locationStub.href);
    locationStub.href = parsed.href;
    locationStub.hash = parsed.hash;
    locationStub.search = parsed.search;
  };
  const context = vm.createContext({
    console,
    document: documentStub,
    history: {
      pushState(_state, _title, url) {
        setUrl(url);
      },
      replaceState(_state, _title, url) {
        setUrl(url);
      }
    },
    localStorage: localStorageStub,
    navigator: { clipboard: { writeText: async () => {} } },
    setTimeout,
    clearTimeout,
    fetch: async () => ({ ok: false }),
    location: locationStub,
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

smokeAssert(ROOT_TAXON_ID === "48460", "root taxon id should be iNaturalist Life.");
smokeAssert(nodes.has(ROOT_TAXON_ID), "Life root node was not indexed.");
smokeAssert(!nodes.get(ROOT_TAXON_ID).childrenLoaded, "Life should start unloaded before lazy subtaxa arrive.");

const root = nodes.get(ROOT_TAXON_ID);
setTaxonChildren(root, [
  taxonFromInaturalist({ id: 1, name: "Animalia", preferred_common_name: "Animals", rank: "kingdom" }),
  taxonFromInaturalist({ id: 47126, name: "Plantae", preferred_common_name: "Plants", rank: "kingdom" })
], 2);
setTaxonChildren(nodes.get("1"), [
  taxonFromInaturalist({ id: 2, name: "Chordata", preferred_common_name: "Chordates", rank: "phylum" }),
  taxonFromInaturalist({ id: 47120, name: "Arthropoda", preferred_common_name: "Arthropods", rank: "phylum" })
], 2);

smokeAssert(root.children.every((child) => child.rank === "kingdom"), "root children are not kingdom-level cards.");
smokeAssert(getPath("2").map((pathNode) => pathNode.rank).join(">") === "stateofmatter>kingdom>phylum", "lazy child path did not preserve parentage.");
smokeAssert(imageIsInDontCareTier({ closest: () => ({ dataset: { tier: "dc" } }) }), "Don't care image skip helper did not detect dc tier.");
smokeAssert(!imageIsInDontCareTier({ closest: () => ({ dataset: { tier: "f" } }) }), "Don't care image skip helper matched a normal tier.");

const initialRankingKeys = Object.keys(state.rankings);
smokeAssert(initialRankingKeys.length === 0, "initial unloaded render should not create rankings.");
smokeAssert(document.querySelector("#save-status").textContent === "Local saves ready", "initial save status did not verify localStorage readiness.");

const lifeRanking = ensureRanking(ROOT_TAXON_ID);
smokeAssert(lifeRanking.unranked.includes("1"), "Animalia did not start unranked.");
render();
smokeAssert(document.querySelector("#context-info-link").href.endsWith("/taxa/48460"), "current taxon info link did not point at Life on iNaturalist.");
smokeAssert(document.querySelector("#context-info-link").title === "Open Life on iNaturalist", "current taxon info link title did not update.");
const rootMarkupAfterRender = document.querySelector("#unranked-list").innerHTML;
smokeAssert(rootMarkupAfterRender.includes("TODO: reimplement traversal in some form"), "hidden traversal TODO comment is missing.");
smokeAssert(rootMarkupAfterRender.includes('class="open-child card-tool"'), "hidden traversal button markup is missing.");
smokeAssert(rootMarkupAfterRender.includes('data-add-children="1"'), "add-children control is missing.");
smokeAssert(rootMarkupAfterRender.includes('data-add-children="47126"'), "add-children control should not require lookahead.");
state.rankings[ROOT_TAXON_ID].expandedTaxa = ["1"];
render();
smokeAssert(!document.querySelector("#unranked-list").innerHTML.includes('data-add-children="1"'), "add-children control did not vanish after expansion.");
state.rankings[ROOT_TAXON_ID] = {
  unranked: ["2", ...root.children.map((child) => child.id)],
  addedChildren: ["2"],
  expandedTaxa: ["1"],
  tiers: emptyTiers()
};
ensureRanking(ROOT_TAXON_ID);
smokeAssert(state.rankings[ROOT_TAXON_ID].unranked[0] === "2", "added child was not allowed at the top of unranked.");
localStorage.setItem(STORAGE_KEY, JSON.stringify({
  currentGroupId: ROOT_TAXON_ID,
  rankings: {
    [ROOT_TAXON_ID]: {
      unranked: ["2", ...root.children.map((child) => child.id)],
      addedChildren: ["2"],
      expandedTaxa: ["1"],
      tiers: emptyTiers()
    }
  }
}));
nodes.delete("2");
parents.delete("2");
state = loadState();
smokeAssert(nodes.has("2"), "reload did not keep a placeholder for an added descendant.");
setTaxonChildren(nodes.get("1"), [
  taxonFromInaturalist({ id: 2, name: "Chordata", preferred_common_name: "Chordates", rank: "phylum" }),
  taxonFromInaturalist({ id: 47120, name: "Arthropoda", preferred_common_name: "Arthropods", rank: "phylum" })
], 2);
ensureRanking(ROOT_TAXON_ID);
render();
smokeAssert(document.querySelector("#unranked-list").innerHTML.includes("Chordates"), "reloaded added descendant did not render after child-list poll.");
smokeAssert(canResetGroup(root, state.rankings[ROOT_TAXON_ID]), "reset group was not enabled for added descendants without placed cards.");
smokeAssert(document.querySelector("#clear-group-button").disabled === false, "reset group button stayed disabled for added descendants.");
clearCurrentGroup();
smokeAssert(state.rankings[ROOT_TAXON_ID].addedChildren.length === 0, "reset group did not remove added descendants.");
smokeAssert(state.rankings[ROOT_TAXON_ID].unranked.join(",") === root.children.map((child) => child.id).join(","), "reset group did not restore the polled child list.");
state.rankings[ROOT_TAXON_ID] = { unranked: [], ranked: ["1"] };
ensureRanking(ROOT_TAXON_ID);
smokeAssert(state.rankings[ROOT_TAXON_ID].tiers.b.includes("1"), "legacy ranked data did not migrate into B tier.");
state.rankings[ROOT_TAXON_ID] = { unranked: root.children.map((child) => child.id), tiers: emptyTiers() };
ensureRanking(ROOT_TAXON_ID);
moveTaxon("1", "tier:s", 0);
smokeAssert(state.rankings[ROOT_TAXON_ID].tiers.s[0] === "1", "moveTaxon did not place Animalia first in S tier.");
smokeAssert(!state.rankings[ROOT_TAXON_ID].unranked.includes("1"), "moveTaxon left Animalia in unranked.");
const storedAfterMove = JSON.parse(localStorage.getItem(STORAGE_KEY));
smokeAssert(storedAfterMove.rankings[ROOT_TAXON_ID].tiers.s[0] === "1", "moveTaxon did not persist tier order to localStorage.");
smokeAssert(document.querySelector("#save-status").textContent === "Saved locally", "save status did not confirm successful persistence.");

openGroup("2");
smokeAssert(location.hash === "#2", "openGroup did not update the taxon hash.");
smokeAssert(state.currentGroupId === "2", "openGroup did not navigate to the requested taxon.");
const hashUrl = new URL(location.href);
hashUrl.hash = "1";
location.href = hashUrl.href;
location.hash = hashUrl.hash;
routeFromHash();
smokeAssert(state.currentGroupId === "1", "hash routing did not navigate to the requested taxon.");

state.currentGroupId = "1";
render();
smokeAssert(document.querySelector("#context-title").textContent === "Animals", "drill-down context did not render Animals.");
const beforeResultsKeys = Object.keys(state.rankings).sort().join(",");
activeView = "results";
render();
const afterResultsKeys = Object.keys(state.rankings).sort().join(",");
smokeAssert(beforeResultsKeys === afterResultsKeys, "results view created extra empty rankings.");

state.currentGroupId = "1";
clearCurrentGroup();
smokeAssert(state.rankings["1"].unranked.length === nodes.get("1").children.length, "clearCurrentGroup did not restore all animal phyla.");
smokeAssert(countPlaced(state.rankings["1"]) === 0, "clearCurrentGroup left placed animal cards.");

placeLeftovers();
smokeAssert(state.rankings["1"].unranked.length === 0, "placeLeftovers did not empty unranked.");
smokeAssert(state.rankings["1"].tiers.dc.length === nodes.get("1").children.length, "placeLeftovers did not send all leftovers to Don't care tier.");

renderData();
const exported = JSON.parse(document.querySelector("#data-box").value);
smokeAssert(exported.rankings[ROOT_TAXON_ID].tiers.s.includes("1"), "export is missing root tier data.");
smokeAssert(exported.rankings["1"].tiers.dc.length === nodes.get("1").children.length, "export is missing drill-down tier data.");
smokeAssert(!Object.prototype.hasOwnProperty.call(exported, "taxa"), "export should not include a stored taxonomy snapshot.");

globalThis.__smokeResults = smokeResults;
`;

if (scripts[0]) {
  try {
    const context = makeContext("?noautoload=1");
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
