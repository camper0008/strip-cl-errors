import sys
import argparse
import importlib.metadata

from .compile import should_skip_multiple, should_skip_count
from .linker import strip_linker_errors


def main():
    parser = argparse.ArgumentParser("sclerr")
    parser.add_argument("--unstable-strip-compile", action="store_true")
    parser.add_argument("-v", "--version", action="store_true")
    parser.add_argument("-lbd", "--linker-bracket-depth", type=int, default=0)
    args = parser.parse_args()
    if args.version:
        print(f"sclerr@{importlib.metadata.version('sclerr')}")
        exit(0)
    is_skipping = False
    skip_count = 0
    for line in sys.stdin:
        if args.unstable_strip_compile:
            if skip_count > 0:
                skip_count -= 1
                continue
            is_skipping = should_skip_multiple(line, is_skipping)

            if is_skipping:
                continue

            skip_count = should_skip_count(line)
            if skip_count > 0:
                skip_count -= 1
                continue
        result = strip_linker_errors(line, args.linker_bracket_depth)
        if result.strip() != "":
            print(result)


if __name__ == "__main__":
    main()
