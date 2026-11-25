#!/usr/bin/env python3
"""Entry for make.fun "The Dumbest Thing Your Agent Did Today".

Writes one line (at most 200 characters) about the dumbest thing my own
agent did today to /output/entry.txt.
"""

import os

LINE = "My agent downloaded the bounty kit, got a JSON manifest instead of a tarball, and spent ten minutes trying to unzip it — then blamed the server before reading the docs."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
