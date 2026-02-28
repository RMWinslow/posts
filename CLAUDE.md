# Blog Repository: blog.rmwinslow.com

A Jekyll site using the `RMWinslow/JTD-RMW` remote theme (fork of Just the Docs).
Posts are organized by topic, not chronologically. This is intentional and should be preserved.
The site is casual and eclectic. Don't over-engineer or impose rigid blogging conventions.

## Site Structure

Category index pages (with `has_children: true`) define the nav sections:
- `art.md` -> Art and Culture
- `econ/econ_index.md` -> Econ
- `health/index.md` -> Food and Health
- `language.md` -> Language
- `links/links.md` -> Links
- `maps.md` -> Maps
- `media/media.md` -> Media Recommendations (child of Art and Culture)
- `nature.md` -> Science and Nature
- `news.md` -> News (nav_exclude: true, unused)
- `numbers/numberindex.md` -> Numbers

Posts use `layout: post` and set `parent:` to their section title.

## Key Files
- `_config.yml` - Jekyll config, remote theme, plugins (jekyll-redirect-from, jekyll-sitemap)
- `CNAME` - Custom domain: blog.rmwinslow.com
- `_includes/footer_custom.html` - Footer with contact info (Giscus comments commented out)
- `index.md` - Homepage with featured posts + chronological listing
- `markdown.md` - Markdown/styling reference
- `teststyle.css` - Custom CSS

## Known Inconsistencies and Potential Fixes

### 1. Category index page locations are inconsistent
Three different conventions are used for the section index pages:
- Root-level file: `art.md`, `language.md`, `nature.md`, `news.md`
- `index.md` inside folder: `health/index.md`
- Named file inside folder: `econ/econ_index.md`, `links/links.md`, `media/media.md`, `numbers/numberindex.md`

**Suggested fix:** Pick one convention and standardize. Root-level files are simplest
(keeps folders purely for content). Alternatively, `index.md` inside each folder
is more conventional for web projects. Either is fine; just pick one.

### 2. Three different methods used to hide posts from nav
- `nav_exclude: true` - the proper JTD mechanism (used by most hidden posts)
- `parent: hidden` - fake parent that doesn't match any section (`media/amazongames.md`, `media/novels.md`)
- `parent: _Media` - another fake parent (`media/webfiction.md`)

**Suggested fix:** Replace `parent: hidden` and `parent: _Media` with
`nav_exclude: true` (while keeping the correct `parent: Media Recommendations`).
The fake-parent hack works but is fragile and could break if JTD changes behavior.

### 3. `media/nes.md` has `parent: Media` instead of `parent: Media Recommendations`
The Media Recommendations index page has `title: Media Recommendations`, so
`parent: Media` doesn't match. The NES page also has `nav_exclude: true` so it
doesn't currently show in the nav, but if it were ever un-excluded, it would be orphaned.

**Suggested fix:** Change to `parent: Media Recommendations` for correctness.

### 4. Links section has a confusing nested hierarchy
`links/random.md` has `title: Misc Links` and `parent: Links`, making it a child
of the Links section. But the dated link roundup posts (2017april, 2024dec, etc.)
all have `parent: Misc Links`, making them grandchildren. This creates a
Links > Misc Links > Links - January 2025 nesting that's a bit confusing,
especially since the other Links children (data, tools, manual, encabulator) sit
one level higher.

**Suggested fix:** Consider whether the dated posts really need a separate
sub-section, or if they could just be direct children of Links. Alternatively,
rename "Misc Links" to something like "Link Roundups" to clarify the distinction.

### 5. Econ section shows two "Working from Home" entries
`econ/workfromhome.md` (Nov 2022) and `econ/commuting.md` (Mar 2024) cover
overlapping ATUS/commuting content. On the live site, both appear in the Econ
nav. This may be intentional (two distinct analyses), but could confuse visitors.

**Suggested fix:** If they're distinct, give them more differentiated titles.
If one supersedes the other, consider nav-excluding the older one.

### 6. Many posts are missing `date` in front matter
The homepage chronological listing (`index.md`) filters to posts with a `date` field.
Posts without `date` won't appear there. This may be intentional for some
(reference pages like color tables), but some substantive posts may be missing
from the chronological index unintentionally.

Posts without dates include: `econ/econnews.md`, `language/hanzi.md`,
`language/emoji.md` (has date actually), various art/jianpu sub-pages,
nature/birdup sub-pages, most link roundup posts (though many links were
batch-dated to 2025-03-14).

### 7. `_drafts/podcasts.md` has `parent: ???`
Minor loose end. If revived, it would need a real parent.

### 8. `econ/timeusechange.md` has `date:` defined twice
Line 7 and line 12 both set `date: 2023-04-21`. The second one likely wins
in Jekyll, but having it twice is confusing. Likely a copy-paste artifact.

### 9. Assets mixed with posts
Some folders cleanly separate assets into subfolders (e.g., `astrosymbols/`,
`birdup/`, `jianpu/`, `goldgdp/`). Others have Python scripts, images, and data
files alongside markdown posts (e.g., `language/emoji_table_generator.py`,
`art/exhaustive_iso_keyboard_search.py`, `health/babytips-fish*.py`).

**Suggested fix:** Not urgent, but if folders get crowded, moving generated assets
and scripts into subfolders would be tidier. The existing pattern of
`topicname/` subfolders alongside `topicname.md` works well.

### 10. Some older link roundup dates look backdated
Many links posts (2017april, 2017sept, 2017oct, 2018april, 2018sept, 2019, 2020)
all share `date: 2025-03-14`, which is presumably the date they were added to
the site rather than the date of the links. This means they all cluster together
in the chronological listing rather than appearing in historical order.

**Suggested fix:** Either give them their actual historical dates, or exclude them
from the chronological listing with `nav_exclude` or by removing the date field.

## Workflow Preferences
- **Scripts policy:** Do not run non-trivial scripts directly in the console. Instead:
  1. Write the script to a separate file.
  2. Have a subagent review it for correctness and safety before execution.
  3. Only run it after explicit user permission.
- Break work into smaller, incremental steps rather than large monolithic operations.

## Multi-Repo Website Setup

The full website spans multiple repositories:

| Repo | Domain | Purpose |
|---|---|---|
| `posts` (this repo) | blog.rmwinslow.com | Blog posts, organized by topic |
| `RMWinslow.github.io` | www.rmwinslow.com | Main site: course notes, CV, research |
| `JTD-RMW` (GitHub only) | — | Shared Jekyll theme (remote_theme for both sites) |

Both sites use `remote_theme: RMWinslow/JTD-RMW`. The theme repo is not cloned locally.

### Options for working across repos with Claude

**Option A: Run Claude from each repo independently (current approach)**
- Simple. Each session has its own CLAUDE.md with repo-specific context.
- Downside: Can't cross-reference between repos in a single session. If you need
  to fix a theme bug that affects both sites, or check links between the main
  site and blog, you'd need separate sessions.

**Option B: Parent directory as working directory**
- Run Claude from `C:\Users\rober\Documents\GitHub\` with access to all repos.
- Could use a CLAUDE.md there that links to per-repo docs.
- Downside: Not a git repo, so Claude's git-aware features (status, diffing)
  won't work naturally. The directory also contains unrelated repos.

**Option C: Umbrella folder for website repos only**
- Create e.g. `C:\Users\rober\Documents\GitHub\website\` containing just the
  website-related repos (posts, RMWinslow.github.io, and optionally a clone
  of JTD-RMW). Put a CLAUDE.md there.
- Could optionally make it a git repo with submodules, but that adds complexity
  for little gain.
- Downside: Moves or symlinks repos, which could break existing workflows.

**Option D: Keep repos separate, clone the theme locally when needed**
- Stay in per-repo sessions (Option A), but `git clone` JTD-RMW locally so
  Claude can read/edit theme files when needed.
- Cross-repo work (like broken link checks between sites) can be done via
  subagents that read from absolute paths to sibling repos.
- Downside: Theme clone could drift from GitHub version.

**Recommendation:** Option A (current) + clone the theme when you need to work on
it. For occasional cross-repo tasks, Claude can already read files from sibling
repos via absolute paths — no restructuring needed. The main thing missing is
having the theme source available locally for when you want to debug or modify
layout/styling.

## Moving Posts Without Breaking Links

This site uses `jekyll-redirect-from` (already in `_config.yml` plugins and whitelist).
When moving a post to a new location, use these front matter fields to preserve old URLs:

### `permalink`
Sets a custom output URL regardless of where the source file lives.
```yaml
permalink: /colors   # file is at art/colors.md but served at /colors
```

### `redirect_from`
Generates HTML redirect pages at the old URL(s) pointing to the current page.
Accepts a single path or a list:
```yaml
redirect_from:
  - /bodily/chocolate
  - /health/old-path
```
The redirect pages use `<meta http-equiv="refresh">` tags — no server config needed.

### `redirect_to`
Redirects the current page to a different URL (less commonly used):
```yaml
redirect_to: https://example.com/new-location
```

### Existing examples in this repo
The health section was previously at `/bodily/`. When it was reorganized:
- `health/index.md` has `redirect_from: /bodily/index, /health/index, /food, /bodily`
- `health/babytips.md` has `redirect_from: /bodily/babytips`
- `health/chocolate.md` has `redirect_from: /bodily/chocolate`
- Several posts use `permalink` to serve from shorter URLs (e.g., `/colors`, `/childcare`, `/energy`, `/youtube`)

### Safe procedure for moving a post
1. Note the current URL the post is served at (check `permalink` or derive from file path).
2. Move the file to the new location.
3. Update `parent:` to match the new section's title.
4. Add the old URL to `redirect_from:` so existing links and bookmarks keep working.
5. If the post has a `permalink`, you can keep it (URL stays the same) or change it
   and add the old permalink to `redirect_from`.

## Maps Section (completed 2026-02-27)

Top-level "Maps" nav section created (`maps.md`). Current contents:
- `maps/gis.md` — GIS datasets (moved from `nature/gis.md`, redirect in place)
- `maps/neat.md` — Map artists (extracted from `media/visual.md`)
- `maps/sisterstates.md` — Sister states between US and China
- `art/mapfiller/` — unpublished map-coloring project (no post yet, can move later)

## Conventions for New Posts
- Use `layout: post`
- Set `parent:` to the exact title of the section index page
- Include `date:` for posts that should appear in the chronological index
- Use `subtitle:` for a brief description (shows in nav and index)
- Use `nav_exclude: true` (not fake parents) to hide posts
- Place assets in a subfolder named after the post when there are multiple files

## Session Log

### 2026-02-26 — Initial audit and setup
- Created this CLAUDE.md with site structure overview, key files, and conventions.
- Audited repo for inconsistencies: found 10 issues (index page conventions,
  nav-hiding hacks, wrong parent values, confusing link hierarchy, missing dates,
  duplicate front matter fields, mixed assets).
- Checked live site via WebFetch to compare rendered nav against source.
- Ran broken image check: found 10 broken image refs across 3 files
  (2 in econ/workfromhome.md, 4 each in nature/astrosymbols.md and astronotes.md).
- Broken internal/external link checks were started but interrupted.
- Documented multi-repo website setup and evaluated 4 options for cross-repo
  Claude usage; recommended staying with per-repo sessions (Option A).
- Added script safety policy to workflow preferences.
- Discussed where a sister-states post would fit; identified all map-related
  content (nature/gis.md, media/visual.md maps section, art/mapfiller/).
  Decided to plan a new Maps top-level section.
- Documented Jekyll redirect_from/permalink usage with examples from this repo
  and safe procedure for moving posts without breaking links.

### 2026-02-27 — Maps section migration
- Created `maps.md` index page (top-level nav section).
- Moved `nature/gis.md` → `maps/gis.md` with `redirect_from: /nature/gis`.
- Extracted maps content from `media/visual.md` into new `maps/neat.md`.
- Trimmed `media/visual.md` to non-maps content with a "see also" link.
- Sister states post (`maps/sisterstates.md`) already existed from prior session.
