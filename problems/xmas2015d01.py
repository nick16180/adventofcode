from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from functools import reduce


def accumulator(acc: dict, add) -> dict:
    if add in acc.keys():
        acc[add] += 1
    else:
        acc[add] = 1
    return acc


def algo1(args: str) -> int:
    letter_count = reduce(accumulator, map(lambda x: x, args), {})
    return letter_count.get("(", 0) - letter_count.get(")", 0)


def algo2(args: str) -> int:
    pos = 0
    i = 0
    while pos >= 0 and i < len(args):
        pos += 1 if args[i] == "(" else -1
        if pos >= 0:
            i += 1
    return i + 1


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 1
p.title = "Not Quite Lisp"
fn = Path(environ.get("data_folder")).absolute() / (
    Path(__file__).stem + ".txt"
)
args = read_text(fn)
p.algo = [algo1, algo2]
p.args = [args, args]
p.date_solved = "2024-01-22"
p.url = f"https://adventofcode.com/{p.year}/day/{p.day}"
p.github_url = environ.get("github_url") + "/".join(
    ["problems", Path(__file__).name]
)


if __name__ == "__main__":
    # test the given input
    p.run(["(())"], n=1, a=0)
    assert p.solution[0] == 0, "Result incorrect"
    p.run(["()()"], n=1, a=0)
    assert p.solution[0] == 0, "Result incorrect"
    p.run(["((("], n=1, a=0)
    assert p.solution[0] == 3, "Result incorrect"
    p.run(["(()(()("], n=1, a=0)
    assert p.solution[0] == 3, "Result incorrect"
    p.run(["))((((("], n=1, a=0)
    assert p.solution[0] == 3, "Result incorrect"
    p.run(["())"], n=1, a=0)
    assert p.solution[0] == -1, "Result incorrect"
    p.run(["))("], n=1, a=0)
    assert p.solution[0] == -1, "Result incorrect"
    p.run([")))"], n=1, a=0)
    assert p.solution[0] == -3, "Result incorrect"
    p.run([")())())"], n=1, a=0)
    assert p.solution[0] == -3, "Result incorrect"
    p.run([")"], n=1, a=1)
    assert p.solution[0] == 1, "Result incorrect"
    p.run(["()())"], n=1, a=1)
    assert p.solution[0] == 5, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
