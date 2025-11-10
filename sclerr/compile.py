def should_skip_multiple(line: str, is_skipping: bool) -> bool:
    components = line.split(" ")
    if components[0] == "FAILED:":
        path = components[2]
        is_irrelevant = path.startswith("subprojects") or path.startswith("C:\\Program Files")
        return is_irrelevant
    if is_skipping:
        return not line.endswith(" errors generated.")
    return False

def should_skip_count(line: str) -> int:
    if line.startswith("In file included from"):
        return 1
    if line.startswith("C:\\Program Files"):
        return 3
    if line.strip() == "^":
        return 1
    return 0