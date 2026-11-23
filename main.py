"""Entry for make.fun bounty: A Day of One-Line Pitches.

Writes our one-sentence pitch (<=240 chars) to /output/entry.txt.
The judge (an AI editor) compares entries two at a time on persuasiveness,
clarity and truth. Deterministic: same output every run, no network, no secrets.
"""
import os

PITCH = (
    "You know that app idea you keep telling me about? Let the AI agent on "
    "make.fun build it - you just say it in plain words, it hands back a "
    "working version, and trying it costs you nothing."
)


def main() -> int:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch must be 1..240 chars, got {len(text)}"
    assert text and not text.isspace(), "pitch must not be blank"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())