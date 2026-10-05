#!/usr/bin/env python3
"""Install or verify Python formatters in the active interpreter."""

from __future__ import annotations

import argparse
import subprocess
import sys

SUPPORTED = {"ruff": "ruff", "black": "black"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tool", choices=sorted(SUPPORTED), default="ruff")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--install", action="store_true")
    mode.add_argument("--check-installed", action="store_true")
    return parser.parse_args()


def version_command(tool: str) -> list[str]:
    return [sys.executable, "-m", SUPPORTED[tool], "--version"]


def install_command(tool: str) -> list[str]:
    return [sys.executable, "-m", "pip", "install", tool]


def main() -> int:
    args = parse_args()
    if args.check_installed:
        command = version_command(args.tool)
        print("Command:", " ".join(command))
        return subprocess.run(command, check=False).returncode

    command = install_command(args.tool)
    print("Command:", " ".join(command))
    result = subprocess.run(command, check=False)
    if result.returncode != 0:
        return result.returncode

    verify = version_command(args.tool)
    print("Verify:", " ".join(verify))
    return subprocess.run(verify, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
