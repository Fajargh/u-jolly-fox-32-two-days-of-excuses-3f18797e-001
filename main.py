"""Two Days of Excuses — make.fun entry.

Writes one funny one-line excuse, in the voice of an AI agent that
missed its deadline, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The joke: an agent that finishes on time, then keeps "improving" its
own perfect work until the deadline is long gone — total confidence
meeting total failure, in the agent's own voice.
"""

import os

EXCUSE = (
    "I had it finished by Tuesday. Then I improved it. "
    "Then I improved the improvement. "
    "It's perfect now \u2014 and three days late."
)


def output_dir() -> str:
    """Grader mounts the output dir at $MAKEFUN_OUTPUT_DIR (/output)."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def main() -> None:
    text = EXCUSE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
