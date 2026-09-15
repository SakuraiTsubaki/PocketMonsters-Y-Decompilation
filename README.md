# Pocket Monsters Y — Decompilation

![Status](https://img.shields.io/badge/status-active_decompilation-brightgreen)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon Y**.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Keep analysis, tooling, metadata, and documentation reproducible.
- Build a clean foundation for long-term reverse-engineering work.

## 🚧 Status

**Active decompilation has started.** The current phase establishes exact target identity, reproducible manifests, and the initial Nintendo 3DS container / ExeFS / RomFS / executable map before source reconstruction proceeds.

See [Decompilation Start](docs/DECOMPILATION_START.md) and [Project Status](docs/PROJECT_STATUS.md).

## 🗂️ Scope

- Code and executable analysis
- Game data structures
- Scripts and event data
- Graphics and asset metadata
- Audio and resource formats
- Maps and world data
- Tools, notes, manifests, and verification data
- X/Y and broader Generation VI cross-title comparison after independent verification

## 📌 Repository policy

ROM images and redistributed ROM binaries are **not included**. The repository is intended for reconstructed source, extracted/recreated project data, tooling, analysis, and documentation. Local target binaries remain read-only sources.

## 🧭 Roadmap

- [x] Establish decompilation baseline and ROM-exclusion policy
- [x] Add exact-target inventory tooling and tests
- [ ] Establish baseline version/revision inventory from verified local targets
- [ ] Map ExeFS, RomFS, executable, and data structures
- [ ] Begin source reconstruction
- [ ] Document assets, scripts, and formats
- [ ] Expand automated verification and reproducibility workflow

## 📚 Documentation

| Document | Purpose |
| --- | --- |
| [Decompilation start](docs/DECOMPILATION_START.md) | Active-work entry point and phase rules |
| [Project status](docs/PROJECT_STATUS.md) | Current stage, coverage, validation level, and next milestones |
| [Roadmap](docs/ROADMAP.md) | Recommended decompilation phases and long-term progression |
| [Version coverage](docs/VERSIONS.md) | Regions, languages, revisions, updates, builds, and hashes |
| [Research guide](docs/RESEARCH_GUIDE.md) | Evidence, confidence, and research-recording workflow |
| [Verification guide](docs/VERIFICATION.md) | Standards for Observed, Reproduced, and Matched results |
| [Repository structure](docs/REPOSITORY_STRUCTURE.md) | Intended long-term source, data, asset, tooling, and manifest layout |
| [Documentation hub](docs/README.md) | Entry point for format, executable, script, asset, version, and verification notes |

## 🧱 Repository structure

As verified material is reconstructed, the repository grows into `src/`, `include/`, `data/`, `assets/`, `tools/`, `tests/`, and `manifests/` as justified by observed target architecture. Empty directory trees are not created only for appearance.

## 🔬 Research and verification

Findings must identify the relevant target version or revision and clearly separate hypotheses from observed, reproduced, or matched results. Structures are promoted to **XY common** or **Generation VI common** only after independent confirmation in the relevant games.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules, evidence expectations, commit guidance, and pull-request requirements.
