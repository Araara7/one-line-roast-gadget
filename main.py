#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes one original roast line about the Wi-Fi router to /output/entry.txt.
Deterministic: the same bytes on every run. No network, stdlib only.
"""

import os

ENTRY = "My Wi-Fi drops every time I join an important call, then reconnects the second I switch to my phone, like it was testing my loyalty."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
