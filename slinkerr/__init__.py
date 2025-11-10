import sys


def cull_angle_brackets(line: str) -> str:
    open_brackets = []
    brackets: list[tuple[int, int]] = []
    for i, ch in enumerate(line):
        if ch == "<":
            open_brackets.append(i)
        if ch == ">":
            start = open_brackets.pop()
            if len(open_brackets) == 0:
                brackets.insert(0, (start, i))
    for start, end in brackets:
        line = line[:start] + line[end:]
    return line


def cull_question_parenthesis(line: str) -> str:
    open_brackets = []
    brackets: list[tuple[int, int]] = []
    for i, ch in enumerate(line):
        if ch == "(":
            if line[i + 1] == "?":
                open_brackets.append(i)
            continue
        if ch == ")" and len(open_brackets) > 0:
            start = open_brackets.pop()
            if len(open_brackets) == 0:
                brackets.insert(0, (start, i))
    for start, end in brackets:
        line = line[:start] + line[end:]
    return line


def main():
    for line in sys.stdin:
        if not "LNK2019" in line:
            continue

        print(cull_question_parenthesis(cull_angle_brackets(line)))


if __name__ == "__main__":
    main()
