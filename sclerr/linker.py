def cull_angle_brackets(line: str, depth: int) -> str:
    open_brackets = []
    brackets: list[tuple[int, int]] = []
    for i, ch in enumerate(line):
        if ch == "<":
            open_brackets.append(i)
        if ch == ">":
            start = open_brackets.pop()
            if len(open_brackets) == depth:
                brackets.insert(0, (start, i))
    for start, end in brackets:
        line = line[:start] + "<..>" + line[end + 1 :]
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
        line = line[:start] + line[end + 1 :]
    return line


def cull_cdecl(line: str) -> str:
    return line.replace("__cdecl", "")


def cull_whitespace(line: str) -> str:
    line = line
    while "  " in line:
        line = line.replace("  ", " ")
    return line


def strip_linker_errors(line: str, linker_bracket_depth: int) -> str:
    if line.startswith('"link"'):
        return ""

    if "LNK2019" in line:
        return cull_whitespace(
            cull_cdecl(
                cull_question_parenthesis(
                    cull_angle_brackets(line, linker_bracket_depth)
                )
            )
        )
    return line
