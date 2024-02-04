from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from typing import Any


def parse_line(s: str) -> dict:
    # parses an input line into a dict for easy usage later
    _s = s.strip().split(" ")
    if len(_s) == 0:
        raise ValueError("Parsed line is empty.")
    dest = _s[-1]  # always the destination
    _s = _s[:-2]  # remove the last two items
    # f is the operation to run, so determine what it should be along with the
    # operands
    f, op1, op2 = None, None, None
    if "AND" in s:
        f = lambda a, b: int(a) & int(b)
        op1 = _s[0]
        op2 = _s[2]
    elif "OR" in s:
        f = lambda a, b: int(a) | int(b)
        op1 = _s[0]
        op2 = _s[2]
    elif "LSHIFT" in s:
        f = lambda a, b: int(a) << int(b)
        op1 = _s[0]
        op2 = _s[2]
    elif "RSHIFT" in s:
        f = lambda a, b: int(a) >> int(b)
        op1 = _s[0]
        op2 = _s[2]
    elif "NOT" in s:
        # ints in python are stored signed unless uint is used
        # this performs the not but applies 0xFFFF as bitmask
        # to do the not as if it were unsigned
        f = lambda a, b: ~int(a) & 0xFFFF
        op1 = _s[1]
    else:
        f = lambda a, b: int(a)
        op1 = _s[0]
    return {"dest": dest, "op": f, "op1": mycast(op1), "op2": mycast(op2)}


def mycast(s: Any) -> Any:
    # convert s to int if possible, otherwise dont change it
    res = None
    if s is not None:
        try:
            res = int(s)
        except (ValueError, TypeError):
            res = s
    return res


def algo1(args: str) -> int:
    # for each line, try to run the operation given using the operands
    # if the operands are not set yet, put that operation on the end of the list
    # to process, then move onto the next one
    parsed = [parse_line(line) for line in args.splitlines() if len(line) > 0]
    res = {}
    i = 0
    while len(parsed) > 0:
        d = parsed[i].get("dest")
        x0 = parsed[i].get("op1")
        x = res.get(x0, None) if type(x0) == str else x0
        y0 = parsed[i].get("op2")
        y = res.get(y0, None) if type(y0) == str else y0
        f = parsed[i].get("op")
        try:
            res[d] = f(x, y)
        except (ValueError, TypeError):
            parsed.append(parsed[i])
        parsed.pop(i)

    return res.get("a")


def algo2(args: str) -> int:
    # this is identical to algo1, but b is set to the answer for algo1
    # then b is ignored later on per the instructions
    parsed = [parse_line(line) for line in args.splitlines() if len(line) > 0]
    res = {"b": 956}
    while len(parsed) > 0:
        d = parsed[0].get("dest")
        if d == "b":
            parsed.pop(0)
        x0 = parsed[0].get("op1")
        x = res.get(x0, None) if type(x0) == str else x0
        y0 = parsed[0].get("op2")
        y = res.get(y0, None) if type(y0) == str else y0
        f = parsed[0].get("op")
        try:
            res[d] = f(x, y)
        except (ValueError, TypeError):
            parsed.append(parsed[0])
        parsed.pop(0)

    return res.get("a")


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 7
p.title = "Some Assembly Required"
fn = Path(environ.get("data_folder")).absolute() / (
    Path(__file__).stem + ".txt"
)
args = read_text(fn)
p.algo = [algo1, algo2]
p.args = [args, args]
p.date_solved = "2024-02-03"
p.url = f"https://adventofcode.com/{p.year}/day/{p.day}"
p.github_url = environ.get("github_url") + "/".join(
    ["problems", Path(__file__).name]
)


if __name__ == "__main__":
    # test the given input
    p.run(["123 -> a"], n=1, a=0)
    assert p.solution[0] == 123, "Result incorrect"
    p.run(["456 -> a"], n=1, a=0)
    assert p.solution[0] == 456, "Result incorrect"
    txt = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> a
"""
    p.run([txt], n=1, a=0)
    assert p.solution[0] == 65079, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
