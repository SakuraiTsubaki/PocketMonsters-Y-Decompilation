# Public Source Sweep 01 — Census First

## Purpose

This project has no local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or extracted retail asset set. Therefore research must begin by **exhaustively locating public evidence before deeply auditing any single tool or subsystem**.

The Japanese release is the comparison origin for regional research. This does not assume that every Japanese file is the development master or that Japan necessarily received every release first. It means that regional/language/revision/update comparisons are recorded as differences from a Japanese baseline whenever the evidence allows that baseline to be defined.

All useful findings, source registrations, gap lists, tools, schemas, tests, comparison tables and verification records are committed to this repository. Retail ROM/game images and other non-redistributable binaries are not.

## What changed in this sweep

The source census is no longer centered on pk3DS or any other single project. `manifests/source-inventory.csv` now registers a broad source network spanning:

- Japanese Pokémon/Nintendo official pages, manuals, update pages, news indexes and guidebook references.
- North American official Pokémon/Nintendo product, support, manual and update-history pages.
- Additional regional official notices where they independently document release/update chronology.
- Public reverse-engineering implementations: pk3DS, historical pk3DS forks, CTRMap, CTRMap-F5, PKHeX, Project_CTR, Azahar, Ohana3DS-Rebirth, SPICA, n3ds_importer, citro3d and tex3ds.
- Independent battle-mechanics implementation in Pokémon Showdown for generation-specific reverse cross-checking.
- Project Pokémon historical ROM/save research, including the 3DS R&D forum, X/Y save research, WC6/WC6Full, RAM2Sav, PCEdit and Pokémon Link research.
- Project Pokémon EventsGallery for machine-readable Gen VI event preservation.
- Serebii's X/Y hub and system pages as a large secondary discovery index.
- Bulbapedia's Generation VI glitch/battle/overworld collections as patch-sensitive research leads whose references must be traced back to stronger evidence.
- GameFAQs historical guides as secondary walkthrough, translation, location and mechanics discovery material.
- The Cutting Room Floor as an unused/debug/beta source family; direct access is currently limited by HTTP 403 from the available crawler, so it remains registered rather than silently omitted.
- Internet Archive / Wayback Machine as a required recovery layer for removed official sites, Pokémon Global Link pages, event campaigns and older regional material.
- Pokémon Bank / Poké Transporter official support material for the Gen VI external-transfer timeline.
- Text/localization corpora such as poke-corpus, subject to copyright and license review before mirroring any bulk text.

## Exhaustion rule

A source family is **not** considered surveyed merely because its home page has been found. It stays open until the relevant public surface has been enumerated as far as practicable.

Examples:

- an official game site means crawling its navigation sections, dated news/update entries, campaign/event pages, product pages and surviving linked documents;
- a forum means enumerating all relevant result pages/topics and following historically significant attachments, mirrors and referenced tools when still public;
- a GitHub project means recording the canonical repository, relevant historical forks/lineage, important branches/tags/commits, format parsers, tests and linked research when material;
- a secondary wiki/database means enumerating the Gen VI category or game hub and following references back toward primary or implementation evidence;
- a web archive means storing the original URL, capture timestamp, archival URL and what disappeared from the live web.

No finite search can prove that the entire public Internet has been exhausted. Project completeness is therefore measured by explicit source-family coverage, recursive enumeration and a maintained gap list, not by declaring victory after a few search results.

## Japanese-origin regional matrix

Regional work is recorded along independent axes:

`game × market/region × selectable language × revision/build × update version × distribution/service date`

Do not collapse `region` and `language`. X/Y permit multiple selectable languages, while hardware market, software product identity, distribution campaign, support page and update publication can still be region-specific.

Every regional difference record should ultimately identify:

- Japanese baseline evidence;
- target region/market evidence;
- language if relevant;
- revision/update context;
- difference type (data, text, graphics, behavior, distribution, service, legal/support wording, etc.);
- source IDs;
- verification status and unresolved conflicts.

## Current state

`manifests/source-inventory.csv` contains the first expanded census batch. The inventory is intentionally open-ended and will continue to grow before and during subsystem reconstruction.

Deep audits such as `PK3DS_INDEX_01_CORE_DATA.md` remain useful, but they are now subordinate to this wider census: no single implementation is allowed to define the Generation VI model by itself.
