#!/usr/bin/env python3
"""Tiny demo: greet by name or print a friendly default."""


def greet(name: str | None = None) -> str:
    who = name.strip() if name else "world"
    return f"Hello, {who}!"


if __name__ == "__main__":
    import sys

    arg = sys.argv[1] if len(sys.argv) > 1 else None
    print(greet(arg))
