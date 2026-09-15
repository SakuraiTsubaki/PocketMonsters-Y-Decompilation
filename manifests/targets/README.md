# Target Manifests

Store metadata-only identity manifests for locally verified targets here. Do not commit game-image bytes, decrypted keys, console keys, or private local paths.

Recommended naming: `<title>_<region>_<language>_<revision-or-update>_<kind>.json`.

Kinds should distinguish at least `source`, `extracted`, `exefs`, and `romfs` when those layers have been independently inventoried. Every manifest should contain hashes/sizes only and remain traceable to a specific verified local target.
