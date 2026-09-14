# Documentation Hub

This directory is the central documentation portal for the decompilation project. Use it to move from target identification and research through reconstruction, asset handling, manifests, and verification without losing version context or evidence.

## Quick links

| Document | Purpose |
| --- | --- |
| [Project Status](PROJECT_STATUS.md) | Current stage, target coverage, validation level, and next milestones |
| [Roadmap](ROADMAP.md) | Recommended project phases from target definition through reproducible reconstruction |
| [Version Coverage](VERSIONS.md) | Regions, languages, revisions, updates, builds, hashes, and support status |
| [Research Policy](RESEARCH_POLICY.md) | No-ROM public-source workflow, Japan-market comparison origin, full regional census, and GitHub-output policy |
| [Public Source Census](PUBLIC_SOURCE_CENSUS.md) | Master list of source families, mandatory domain sweeps, evidence classes, and gaps |
| [Research Guide](RESEARCH_GUIDE.md) | Evidence, confidence, offsets, naming, and research-recording practices |
| [Verification Guide](VERIFICATION.md) | Standards for Unverified, Observed, Reproduced, and Matched results |
| [Repository Structure](REPOSITORY_STRUCTURE.md) | Intended long-term layout for source, data, assets, tools, tests, and manifests |
| [Project Standards](PROJECT_STANDARDS.md) | Naming, provenance, generated-data, manifest, and repository-boundary rules |
| [Asset Workflow](ASSET_WORKFLOW.md) | Extraction, reviewable assets, deduplication, manifest registration, and batch workflow |
| [Manifest Guide](../manifests/README.md) | Machine-readable inventories, hashes, target coverage, provenance, and shared assets |
| [Public Source Inventory](../manifests/source-inventory.csv) | Machine-readable registry of reviewed and pending public evidence sources |
| [pk3DS Index 01](research/PK3DS_INDEX_01_CORE_DATA.md) | First pinned source-level audit of Gen VI game config, GARC mapping, personal/move/learnset/evolution/trainer structures |
| [Contributing](../CONTRIBUTING.md) | Contribution rules, evidence expectations, commits, and pull-request guidance |

## Research areas

As verified work becomes concrete, documentation may grow into areas such as `architecture/`, `formats/`, `research/`, `versions/`, and `verification/`. Create these directories when they contain real research material rather than as empty placeholders.

`research/` now contains source-level audits pinned to specific upstream revisions. A research index records what a public implementation or document says; it does not automatically promote that claim to direct retail observation.

## Recommended documentation flow

1. Identify the target in `VERSIONS.md`.
2. Register evidence in `../manifests/source-inventory.csv` and follow `RESEARCH_POLICY.md` / `RESEARCH_GUIDE.md`.
3. Record source-level audits in `research/` or format-specific notes in `formats/`.
4. Reconstruct source, data, or assets following `PROJECT_STANDARDS.md` and `REPOSITORY_STRUCTURE.md`.
5. For asset work, follow `ASSET_WORKFLOW.md` and register material in `../manifests/`.
6. Apply the validation levels defined in `VERIFICATION.md`.
7. Update `PROJECT_STATUS.md`, `VERSIONS.md`, and `ROADMAP.md` when meaningful milestones are reached.

## Documentation rules

- Distinguish confirmed findings from hypotheses and public-implementation observations from direct retail observations.
- Identify the exact target version or revision for version-specific claims.
- Keep market/region, selectable language, revision, and update as separate axes.
- Use the Japan-market release as the comparison origin without assuming it is the development master of every other build.
- Record offsets, paths, symbols, hashes, commands, upstream commits, and other stable evidence when practical.
- Use `TBD`, `unknown`, or `null` instead of inventing missing information.
- Preserve enough provenance for another researcher to reproduce or verify the finding.
- Keep retail ROM images, decrypted game images, console keys, and other redistributable game binaries out of the repository.
