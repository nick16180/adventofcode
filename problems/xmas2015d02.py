from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path


def algo1(args: str) -> int:
    y = [[int(v) for v in line.split("x")] for line in args.splitlines()]
    # just use the formula given in the problem
    z = [[row[0] * row[1], row[1] * row[2], row[0] * row[2]] for row in y]
    zz = [min(row) + 2 * sum(row) for row in z]
    return sum(zz)


def algo2(args: str) -> int:
    y = [[int(v) for v in line.split("x")] for line in args.splitlines()]
    # just use the formula given in the problem
    z = [row[0] * row[1] * row[2] + 2 * (sum(row) - max(row)) for row in y]
    return sum(z)


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 2
p.title = "I Was Told There Would Be No Math"
fn = Path(environ.get("data_folder")).absolute() / (
    Path(__file__).stem + ".txt"
)
args = read_text(fn)
p.algo = [algo1, algo2]
p.args = [args, args]
p.date_solved = "2024-01-27"
p.url = f"https://adventofcode.com/{p.year}/day/{p.day}"
p.github_url = environ.get("github_url") + "/".join(
    ["problems", Path(__file__).name]
)


if __name__ == "__main__":
    # test the given input
    p.run(["2x3x4"], n=1, a=0)
    assert p.solution[0] == 58, "Result incorrect"
    p.run(["1x1x10"], n=1, a=0)
    assert p.solution[0] == 43, "Result incorrect"
    p.run(["2x3x4"], n=1, a=1)
    assert p.solution[0] == 34, "Result incorrect"
    p.run(["1x1x10"], n=1, a=1)
    assert p.solution[0] == 14, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
