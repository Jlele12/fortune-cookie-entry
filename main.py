"""Fortune Cookie Wisdom for Developers — make.fun entry (u-gentle-koala-60).

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: same output on every run.
"""
import os

FORTUNE = "The bug you seek tomorrow hides in the code you are sure of today."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(FORTUNE) <= 120
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
