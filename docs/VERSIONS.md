# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

## Baseline policy

The comparison origin for this repository is the **Japan-market release of Pokémon Y**. This is a research baseline, not a claim that the Japanese retail build is the development master for every worldwide release.

No local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or retail hash is currently available. Therefore no retail target in this table may be marked `Verified`, `Mapped`, or `Matched` solely from public documentation or third-party implementations.

Generation VI separates **market/region** from **in-game language**. The official Japanese Pokémon X/Y site states that a new save can select Japanese, English, Spanish, French, German, Italian, or Korean, and that the selected language cannot be changed during that save. Consequently, `Japan` must not be treated as synonymous with `Japanese-language data`.

## Current target inventory

| Status | Market / region | Language | Revision / update | Platform / build | Hashes | Evidence / notes |
| --- | --- | --- | --- | --- | --- | --- |
| Reference only | Japan | Selectable: JA / EN / ES / FR / DE / IT / KO | Base / 1.0 | Nintendo 3DS; package and download releases | unknown | Official JP product pages give a 2013-10-12 release date. Retail build identity and hashes remain unavailable. |
| Reference only | Japan | same selectable set | Ver. 1.5 | Nintendo 3DS update data | unknown | Nintendo Japan currently records Ver.1.5 distribution on 2015-04-23. Exact update-title metadata and hashes remain unverified locally. |
| Planned | Japan | same selectable set | Ver. 1.1–1.4 | Nintendo 3DS update data | unknown | Historical public references establish intermediate updates, but each Japanese-market notice, package identity, and hash still requires source-by-source recovery and registration. |
| Planned | Worldwide markets outside Japan | TBD by market/SKU | Base and all applicable updates | Nintendo 3DS | unknown | Official JP material says X/Y launched worldwide on 2013-10-12 except some regions; exact regional SKU boundaries must be censused rather than inferred. |

## Official baseline observations already established

- Official Japanese product page: Pokémon X/Y release date `2013-10-12`; Nintendo 3DS; package/download.
- Official Japanese X/Y language page: seven selectable languages — Japanese, English, Spanish, French, German, Italian, Korean.
- The language choice is made when beginning the adventure and cannot be changed for that save.
- Nintendo Japan's current X/Y page records update data `Ver.1.5` dated `2015-04-23`.
- Nintendo Japan states that Nintendo 3DS online-play services for this title ended on `2024-04-09 09:00 JST`; historical functionality and current service state must be documented separately.

These observations identify public reference targets. They do **not** establish retail file hashes, executable identities, title IDs, archive paths, or binary equality between markets.

## Required region / language census

For every discovered retail or update target, record independently:

1. game (`Y`),
2. market / distribution region,
3. physical vs download distribution where relevant,
4. selectable in-game language set,
5. revision / update version,
6. release or distribution date,
7. title/update identifiers when supported by reliable evidence,
8. hashes when a lawful verified source later becomes available,
9. source IDs from `../manifests/source-inventory.csv`,
10. known differences from the Japan-market baseline.

Do not create a regional target merely because a language exists in the seven-language selector.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes confirmed.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target verified from a local retail image.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to relevant documentation or verification issues.
6. Keep market/region, language, game version, revision, and update as separate axes.
7. Use the Japan-market release as the comparison origin, while preserving evidence that contradicts or complicates a simple JP→overseas lineage.
8. Use `unknown`, `TBD`, or `null` rather than filling gaps by inference.
