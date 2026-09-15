# Generation VI — Full Decompilation Scope

This repository participates in a four-title Generation VI decompilation program covering Pokémon X, Pokémon Y, Pokémon Omega Ruby, and Pokémon Alpha Sapphire in parallel.

The project is not limited to executable code. Every subsystem below is opened as a first-class workstream and remains incomplete until it is backed by target-specific evidence.

## Workstreams

1. Target identity, region, language, revision, update and hashes
2. NCCH/CXI container, ExHeader, ExeFS and RomFS structure
3. Executable segments, address maps and relocation assumptions
4. Function boundaries, cross-references, provisional symbols and reconstructed source
5. Resource archives, compression, BinLinker/GARC-like containers and file tables
6. Scripts, events, flags, variables and story-state logic
7. Pokémon species/form data, stats, types, abilities, evolution, breeding and learnsets
8. Moves, battle effects, targeting, priority, flags and acquisition routes
9. Abilities, hidden abilities, battle/field behavior and special mechanics
10. Items, key items, berries, TMs/HMs, Mega Stones, Orbs and unused entries
11. Type chart and battle rules including Fairy, Steel resistance changes and all battle formats
12. Mega Evolution, Mega Stones, split Mega forms and Mega Rayquaza special handling
13. ORAS Primal Reversion and strong-weather mechanics
14. Maps, locations, connections, collision, objects, warps and facilities
15. NPCs, trainers, teams, rewards, rematches, dialogue-state changes and version differences
16. Encounters, capture systems, Horde/Friend Safari/DexNav/Mirage Spot and special encounters
17. Experience, EV/IV, nature, breeding, inheritance, affection and training systems
18. Communications and online systems: local, PSS, GTS, Wonder Trade, Battle Spot, Bank/Transporter interfaces
19. XY-only systems: Pokémon-Amie, Super Training, PSS, O-Power, Friend Safari, Trainer PR Video
20. ORAS-only systems: PokéNav Plus, DexNav, AreaNav, BuzzNav, PlayNav, Secret Bases, Contests, Soaring, Mirage Spots
21. Graphics: models, textures, animations, cameras, effects, UI, icons, fonts and text boxes
22. Audio: BGM, cries, sound effects, sequencing, banks and event-dependent playback
23. Story/event chronology and version-specific branches
24. Localization, language/region differences, text resources and naming
25. Patches, revisions, bug fixes and compatibility changes
26. Unused/dummy/test data, unreachable maps, scripts, assets and text
27. External distributions, event Pokémon/items and service-era behavior
28. Cross-generation inheritance, changed mechanics and later reuse without retroactive rule mixing

## Comparison buckets

Evidence is classified only after direct verification:

- title-specific
- XY common
- ORAS common
- Generation VI common
- region/language/revision/update specific

A public reference can guide investigation, but does not promote a claim to verified target data by itself.

## Completion rule

A workstream is not complete because representative examples are documented. Completion requires the full inventory for its declared scope, explicit version/title differences, evidence/provenance, and reproducible validation where practical.

ROM/game-image binaries, decrypted title keys and private console keys remain outside Git. Reconstructed source, tooling, manifests, metadata, documentation, patches and independently authored assets may be committed.