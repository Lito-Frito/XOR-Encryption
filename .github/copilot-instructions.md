# Repository-specific Copilot instructions

**Purpose:** Help AI coding agents become productive in the XOR-Encryption demo quickly.

**Big picture:**
- **Entry point:** `app/main.py` — simple CLI that demonstrates XOR encryption using helper functions in `app/encrypt.py` and `app/decrypt.py`.
- **Data flow:** user-entered `phrase` -> converted to 8-bit ASCII via the `ascii` dict in `app/main.py` -> XORed bit-by-bit with a 256-bit `key` -> `encrypt()` returns a binary `scrambled` string -> `decrypt()` XORs again and maps bytes back to text via `iicsa`.
- **Why this structure:** The project is an educational, interactive CLI. Functions intentionally show intermediate steps with `input()` prompts and `print()` calls for pedagogy rather than being a library API.

**Quick run / dev workflows:**
- Run locally (interactive):
  - `python3 app/main.py` (run from repo root). The script expects interactive stdin prompts.
- Docker (image published upstream):
  - Build locally: `docker build -t xor_program:local .`
  - Run interactive container: `docker run -i xor_program:local` (the `-i`/interactive flag is required so the script can read stdin).

**Project conventions & patterns:**
- The project is intentionally minimal and interactive: functions call `input()` and `print()` directly. Expect side effects instead of pure return values.
- `app/main.py` declares the `ascii` mapping (char->8-bit string) and builds `iicsa` (reverse mapping) and then passes both maps into `encrypt()` / `decrypt()`.
- Keys: `key` is constructed as repeated 4-bit patterns (e.g. `'1111' * 64`) producing a 256-bit string; callers pass the raw string of `'0'`/`'1'` characters to the functions.
- Character support: Only the characters present in the `ascii` dict in `app/main.py` are supported. Validate any input or extend the dictionary if adding new characters.

**Important implementation details an agent should follow:**
- Function signatures seen in the codebase:
  - `encrypt(message, key, ascii, iicsa) -> scrambled (str of '0'/'1')`
  - `decrypt(scrambled, ascii, iicsa, key)` (prints output, returns `None`)
- Because the code is interactive, automated changes (tests, CI) should either:
  - Refactor to separate UI from logic (preferable): extract pure helper functions that accept/return data without `input()`/`print()`; or
  - Use stdin/stdout monkeypatching in tests to simulate `input()` calls.
- Imports in `app/main.py` use local module names (`from encrypt import encrypt`). When running `python3 app/main.py` from the repo root this works because the script's directory is added to sys.path at runtime. If you convert `app/` into a package, update imports to `from app.encrypt import encrypt` and add `app/__init__.py`.

**Sample Refactor for Separation of Concerns:**
To make the code more testable and reusable, separate the core XOR logic from the interactive UI. Extract pure functions that accept inputs and return outputs without `input()`/`print()`. For example, add these to `app/encrypt.py` and `app/decrypt.py`:

```py
# In app/encrypt.py
def pure_encrypt(message, key, ascii, iicsa):
    bin_string = ''.join(ascii[char] for char in message)
    scrambled = ''.join(str(int(bin_string[i]) ^ int(key[i])) for i in range(len(bin_string)))
    return scrambled

# In app/decrypt.py
def pure_decrypt(scrambled, key, ascii, iicsa):
    decrypted_bin = ''.join(str(int(scrambled[i]) ^ int(key[i])) for i in range(len(scrambled)))
    blocks = [decrypted_bin[i:i+8] for i in range(0, len(decrypted_bin), 8)]
    decrypted_message = ''.join(iicsa[block] for block in blocks)
    return decrypted_message
```

Then, update the interactive functions to call these pure versions and handle UI separately (e.g., print steps around the calls).

**Examples from the codebase (copy/paste friendly):**
- Creating `iicsa` from `ascii` in `app/main.py`:
  ```py
  iicsa = dict([(value, key) for key, value in ascii.items()])
  ```
- Typical encrypt call in `app/main.py`:
  ```py
  scrambled = encrypt(phrase, key, ascii, iicsa)
  decrypt(scrambled, ascii, iicsa, key)
  ```

**Notes for code modifications and PRs:**
- Preserve the interactive demo behavior unless a change explicitly intends to make a non-interactive API.
- If adding automated tests or CI, refactor UI out of core functions and keep small, well-documented pure functions to test.
- When extending character support, update both `ascii` and derived `iicsa` maps.

If anything here is unclear or you want more examples (unit test sketch, suggested refactor, or CI commands), tell me which part to expand. 
