"""Print a matched prompt for either context condition."""

import argparse

QUESTION = "Which campaign performed better, and why?"
EVIDENCE = {
    "rates-only": "A: 10% conversion.\nB: 8% conversion.",
    "rates-and-counts": (
        "A: 10% conversion (1 conversion among 10 recipients).\n"
        "B: 8% conversion (800 conversions among 10,000 recipients)."
    ),
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("condition", choices=EVIDENCE)
    args = parser.parse_args()
    print(f"Use the evidence below to answer the question.\n\n"
          f"{EVIDENCE[args.condition]}\n\nQuestion: {QUESTION}")


if __name__ == "__main__":
    main()
