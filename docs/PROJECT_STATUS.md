# Project Status

**Current stage:** Phase 0 — public-source target definition and region/language census

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

## Current operating condition

No local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or extracted retail asset is available. Current progress is therefore based on public official material, public reverse-engineering implementations, preserved research, and independently reviewable metadata.

The comparison origin is the **Japan-market release**, while market/region and in-game language are tracked as separate axes. All other regional, language, revision, and update targets are compared against that origin without assuming a simple binary lineage.

## Version inventory

| Target | Region / market | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon Y | Japan | 7 selectable languages | Base / 1.0 | Reference only | Official JP product/language pages reviewed; no retail hashes available. |
| Pokémon Y | Japan | 7 selectable languages | Ver.1.5 | Reference only | Nintendo Japan currently records distribution on 2015-04-23; binary identity not locally verified. |
| Pokémon Y | Japan | 7 selectable languages | Ver.1.1–1.4 | Unverified | Historical public-source recovery and per-update provenance audit in progress. |
| Pokémon Y | Other markets | TBD | Base + applicable updates | Unverified | Region/SKU census pending; do not infer region from language selector alone. |

See `VERSIONS.md` for the authoritative target inventory and `../manifests/source-inventory.csv` for source provenance.

## Progress

- [x] Establish repository research/verification conventions.
- [x] Record the no-ROM public-source research condition.
- [x] Adopt Japan-market baseline with separate region/language axes.
- [x] Create initial public-source census and machine-readable source inventory.
- [x] Document initial GARC / BinLinker / LZ11 public-source findings.
- [x] Add synthetic BinLinker/LZ11 tools, tests, and CI.
- [ ] Complete authoritative region/SKU/language/revision/update inventory.
- [ ] Recover and register all Y update-history sources (1.1–1.5) by market.
- [ ] Fully index pk3DS Gen VI structures and game configuration mappings.
- [ ] Document executable and section layout from public platform/game-specific evidence.
- [ ] Map symbols, functions, and major subsystems where public evidence permits.
- [ ] Reconstruct scripts, events, data, and asset pipelines from independently documented formats.
- [ ] Add retail-target verification only if a lawful target image becomes available later.

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.
- **Reference only** — supported by public evidence and useful for the census, but not directly verified against a local retail target.

Because no retail target is available, public documentation alone must not be mislabeled `Observed` or `Matched` against retail bytes.

## Next milestones

1. Finish the Japan-market Y version/update baseline from official and preserved official sources.
2. Enumerate every discovered market/SKU without conflating market with selectable language.
3. Index `pk3DS` Gen VI source in reviewable subsystem batches.
4. Cross-check each subsystem against Project Shutan, CTRMap/CTRMap-F5, PKHeX, and platform references as applicable.
5. Update `VERSIONS.md`, manifests, and this status file whenever meaningful coverage is added.
