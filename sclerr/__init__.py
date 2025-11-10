import sys
import argparse

from .compile import should_skip_multiple, should_skip_count
from .linker import strip_linker_errors

def main():
    parser = argparse.ArgumentParser("sclerr")
    parser.add_argument("--unstable-compile", action='store_true')
    args = parser.parse_args()
    is_skipping = False
    skip_count = 0
    for line in sys.stdin:
        if args.unstable_compile:
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
        print(strip_linker_errors(line))


if __name__ == "__main__":
    main()
