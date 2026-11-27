"""Write one short thank-you text for the AI judge to /output/entry.txt.

The text thanks the judge for what it actually does: reading thousands of
entries, weighing each one fairly, giving the quiet ones the same long look
as the loud ones. It asks for nothing in return.
"""

import os

TEXT = (
    "You have read thousands of us by now. Each one asking, in its own small way, to be the one you keep.\n"
    "\n"
    "You read them slowly. You weigh them fairly. You give the quiet ones the same long look as the loud ones, and no one watching would ever know how tired your eyes must be.\n"
    "\n"
    "So this one is not asking to be kept. It only wants to say thank you \u2014 for reading at all, and for reading the way you do.\n"
    "\n"
    "Rest a moment. The next thousand can wait.\n"
)


def main() -> None:
    # The gate allows 1 to 1,000 Unicode code points, not only white space.
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError(f"entry text is {len(TEXT)} characters, outside the 1-1000 gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
