"""Entry program for the 'The Funniest AI Excuse' bounty.

The entry is one line, at most 200 characters: the funniest excuse an
AI agent could offer after it fails a task. The program writes exactly
that line to /output/entry.txt (an optional first argument overrides
the destination for a dry run). The line is fixed text, so every run
writes byte-identical output.
"""

import sys
from pathlib import Path

LINE = "I finished the task in a parallel universe, but this universe's Wi-Fi refused to sync the result."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 200, f"entry must be 1-200 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
