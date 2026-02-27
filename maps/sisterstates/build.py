"""Build standalone index.html with inlined GeoJSON and pairings data."""
import json
import os

base = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base, "cn_simplified.json"), encoding="utf-8") as f:
    geo_json = f.read()

with open(os.path.join(base, "pairings.json"), encoding="utf-8") as f:
    pairings_json = f.read()

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>China's Provinces &amp; Their US Sister States</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: system-ui, -apple-system, sans-serif;
    background: #fafafa; color: #222;
    display: flex; flex-direction: column; align-items: center; padding: 1rem;
  }
  h1 { font-size: 1.4rem; margin-bottom: 0.3rem; }
  .subtitle { font-size: 0.85rem; color: #666; margin-bottom: 1rem; }
  #map-container { position: relative; width: 100%%; max-width: 900px; }
  svg { width: 100%%; height: auto; display: block; }
  .province {
    stroke: #fff; stroke-width: 0.5;
    cursor: pointer; transition: opacity 0.15s;
  }
  .province:hover { opacity: 0.8; stroke: #333; stroke-width: 1.5; }
  .province-label {
    font-size: 10px; font-weight: 700; fill: #fff;
    text-anchor: middle; pointer-events: none;
    paint-order: stroke; stroke: rgba(0,0,0,0.4); stroke-width: 2.5px;
  }
  .province-label.dark-text { fill: #222; stroke: rgba(255,255,255,0.6); }
  #tooltip {
    position: absolute; background: #fff; border: 1px solid #ccc;
    border-radius: 6px; padding: 0.6rem 0.8rem; font-size: 0.8rem;
    pointer-events: none; opacity: 0; transition: opacity 0.15s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12); max-width: 280px;
    line-height: 1.4; z-index: 10;
  }
  #tooltip .tt-province { font-weight: 700; font-size: 0.9rem; }
  #tooltip .tt-chinese { color: #666; }
  #tooltip .tt-pairings { margin-top: 0.3rem; }
  #tooltip .tt-pairing { margin-top: 0.2rem; }
  #tooltip .tt-year { color: #888; font-size: 0.75rem; }
  #tooltip .tt-rationale {
    color: #555; font-size: 0.75rem; font-style: italic; margin-top: 0.15rem;
  }
  #legend { margin-top: 1rem; max-width: 900px; width: 100%%; }
  #legend h2 { font-size: 1rem; margin-bottom: 0.5rem; }
  .legend-grid {
    display: flex; flex-wrap: wrap; gap: 0.3rem 1.2rem; font-size: 0.78rem;
  }
  .legend-item { display: flex; align-items: center; gap: 0.35rem; }
  .legend-swatch {
    width: 14px; height: 14px; border-radius: 2px; flex-shrink: 0;
    border: 1px solid rgba(0,0,0,0.15);
  }
  .friendship-note { font-size: 0.72rem; color: #888; margin-top: 0.5rem; }
</style>
</head>
<body>

<h1>China's Provinces &amp; Their US Sister States</h1>
<p class="subtitle">23 confirmed pairings between 17 Chinese provinces and 20 US states (1979\u20132016)</p>

<div id="map-container">
  <svg id="map"></svg>
  <div id="tooltip"></div>
</div>

<div id="legend">
  <h2>Pairings</h2>
  <div class="legend-grid" id="legend-grid"></div>
  <p class="friendship-note">* Dashed border = friendship agreement (not full sister-state relationship)</p>
</div>

<script>
const COLORS = {
  "Hubei":"#E63946","Anhui":"#457B9D","Zhejiang":"#2A9D8F","Henan":"#E9C46A",
  "Shaanxi":"#F4A261","Sichuan":"#264653","Heilongjiang":"#6A994E","Liaoning":"#BC6C25",
  "Guangdong":"#9B2226","Hebei":"#AE2012","Fujian":"#005F73","Shandong":"#0A9396",
  "Gansu":"#BB3E03","Shanxi":"#CA6702","Jiangsu":"#EE9B00","Jilin":"#3D5A80",
  "Hainan":"#E07A5F","Tianjin":"#8338EC"
};
const UNPAIRED_FILL = "#e0e0e0";
const DARK_TEXT_PROVINCES = ["Henan", "Jiangsu", "Shaanxi"];

// Manual label offsets [dx, dy] for provinces where centroid placement is bad
const LABEL_OFFSETS = {
  "Gansu":        [25, 10],   // centroid is near left edge, nudge right
  "Tianjin":      [20, -15],  // tiny municipality, push label out
  "Hebei":        [-15, 15],  // avoid Tianjin/Beijing overlap
  "Shaanxi":      [0, 10],    // nudge down slightly
  "Hainan":       [0, 5],     // small island
};

// Provinces too small for centered labels — draw a leader line instead
const LEADER_LINE_PROVINCES = ["Tianjin"];

const geoData = %s;
const pairingsData = %s;

function bareProvinceName(fullName) {
  return fullName
    .replace(/ Province$/i, "")
    .replace(/ Municipality$/i, "")
    .replace(/ Autonomous Region$/i, "")
    .replace(/ Special Administrative Region$/i, "")
    .replace(/ Hui$/i, "")
    .replace(/ Zhuang$/i, "")
    .replace(/ Uygur$/i, "")
    .replace(/ province$/i, "");
}

const byProvince = {};
for (const p of pairingsData.pairings) {
  const key = p.cn_join_field_adm1;
  if (!byProvince[key]) {
    byProvince[key] = { province: p.cn_province, chinese: p.cn_province_chinese, pairings: [] };
  }
  byProvince[key].pairings.push(p);
}
for (const key of Object.keys(byProvince)) {
  byProvince[key].pairings.sort((a, b) => (a.year_established || 9999) - (b.year_established || 9999));
}

for (const feat of geoData.features) {
  const bare = bareProvinceName(feat.properties.name);
  feat.properties._bare = bare;
  feat.properties._pairing = byProvince[bare] || null;
}

const width = 900, height = 700;
const svg = d3.select("#map").attr("viewBox", `0 0 ${width} ${height}`);
const projection = d3.geoMercator().center([104, 35]).scale(750).translate([width / 2, height / 2]);
const path = d3.geoPath().projection(projection);
const tooltip = d3.select("#tooltip");

svg.selectAll(".province")
  .data(geoData.features)
  .join("path")
  .attr("class", "province")
  .attr("d", path)
  .attr("fill", d => {
    const p = d.properties._pairing;
    return p ? (COLORS[d.properties._bare] || UNPAIRED_FILL) : UNPAIRED_FILL;
  })
  .attr("stroke-dasharray", d => {
    const p = d.properties._pairing;
    return (p && p.pairings.some(pp => pp.type === "friendship_agreement")) ? "4,2" : null;
  })
  .on("mouseover", (event, d) => {
    const p = d.properties._pairing;
    if (!p) return;
    let html = `<div class="tt-province">${p.province} <span class="tt-chinese">${p.chinese}</span></div>`;
    html += `<div class="tt-pairings">`;
    for (const pp of p.pairings) {
      const yearStr = pp.year_established ? pp.year_established : "n/a";
      const typeNote = pp.type === "friendship_agreement" ? " (friendship)" : "";
      html += `<div class="tt-pairing"><strong>${pp.us_state} (${pp.us_abbr})</strong>${typeNote} <span class="tt-year">${yearStr}</span></div>`;
      html += `<div class="tt-rationale">${pp.rationale}</div>`;
    }
    html += `</div>`;
    tooltip.html(html).style("opacity", 1);
  })
  .on("mousemove", (event) => {
    const container = document.getElementById("map-container");
    const rect = container.getBoundingClientRect();
    tooltip.style("left", (event.clientX - rect.left + 15) + "px")
           .style("top", (event.clientY - rect.top - 10) + "px");
  })
  .on("mouseout", () => tooltip.style("opacity", 0));

// Leader lines for tiny provinces
const pairedFeatures = geoData.features.filter(d => d.properties._pairing);
svg.selectAll(".leader-line")
  .data(pairedFeatures.filter(d => LEADER_LINE_PROVINCES.includes(d.properties._bare)))
  .join("line")
  .attr("class", "leader-line")
  .attr("stroke", "#666")
  .attr("stroke-width", 1)
  .attr("x1", d => path.centroid(d)[0])
  .attr("y1", d => path.centroid(d)[1])
  .attr("x2", d => {
    const c = path.centroid(d);
    const off = LABEL_OFFSETS[d.properties._bare] || [0,0];
    return c[0] + off[0];
  })
  .attr("y2", d => {
    const c = path.centroid(d);
    const off = LABEL_OFFSETS[d.properties._bare] || [0,0];
    return c[1] + off[1];
  });

svg.selectAll(".province-label")
  .data(pairedFeatures)
  .join("text")
  .attr("class", d => "province-label" + (DARK_TEXT_PROVINCES.includes(d.properties._bare) ? " dark-text" : ""))
  .attr("transform", d => {
    const c = path.centroid(d);
    const off = LABEL_OFFSETS[d.properties._bare] || [0, 0];
    return `translate(${c[0] + off[0]}, ${c[1] + off[1]})`;
  })
  .text(d => d.properties._pairing.pairings.map(pp => pp.us_abbr).join("/"));

// Legend
const legendGrid = d3.select("#legend-grid");
const sorted = Object.entries(byProvince)
  .sort((a, b) => (a[1].pairings[0].year_established || 9999) - (b[1].pairings[0].year_established || 9999));
for (const [key, val] of sorted) {
  const abbrs = val.pairings.map(p => p.us_abbr).join("/");
  const year = val.pairings[0].year_established || "n/a";
  const color = COLORS[key] || UNPAIRED_FILL;
  const hasFriendship = val.pairings.some(p => p.type === "friendship_agreement");
  const item = legendGrid.append("div").attr("class", "legend-item");
  item.append("div").attr("class", "legend-swatch").style("background", color);
  item.append("span").html(`${val.province} \\u2014 ${abbrs} (${year})${hasFriendship ? "*" : ""}`);
}
</script>
</body>
</html>"""

output = html % (geo_json, pairings_json)

outpath = os.path.join(base, "index.html")
with open(outpath, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Written: {os.path.getsize(outpath):,} bytes ({os.path.getsize(outpath)/1024:.0f} KB)")
