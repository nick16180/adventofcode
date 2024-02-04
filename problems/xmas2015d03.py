from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from typing import List


def follow_directions(args: str) -> List:
    # starting coord
    p = [0, 0]
    locs = [p.copy()]
    for i in range(len(args)):
        # adjust coord based on direction
        if args[i] == "^":
            p[1] += 1
        if args[i] == "v":
            p[1] += -1
        if args[i] == ">":
            p[0] += 1
        if args[i] == "<":
            p[0] += -1
        # need to make a copy of the coord before moving on
        q = p.copy()
        locs.append(q)
    # this gets the locations - can apply set() later to get uniques
    x = [f"{locs[i][0]}, {locs[i][1]}" for i in range(len(locs))]
    return x


def algo1(args: str) -> int:
    x = follow_directions(args)
    return len(list(set(x)))


def algo2(args: str) -> int:
    # first direction is always santa, then robo
    # so just rerun the algorithm above with different sets of args
    santa = "".join([args[i] for i in range(len(args)) if i % 2 == 0])
    robo = "".join([args[i] for i in range(len(args)) if i % 2 == 1])
    santax = follow_directions(santa)
    robox = follow_directions(robo)
    x = santax + robox
    return len(list(set(x)))


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 3
p.title = "Perfectly Spherical Houses in a Vacuum"
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
    p.run([">"], n=1, a=0)
    assert p.solution[0] == 2, "Result incorrect"
    p.run(["^>v<"], n=1, a=0)
    assert p.solution[0] == 4, "Result incorrect"
    p.run(["^v^v^v^v^v"], n=1, a=0)
    assert p.solution[0] == 2, "Result incorrect"
    p.run(["^v"], n=1, a=1)
    assert p.solution[0] == 3, "Result incorrect"
    p.run(["^>v<"], n=1, a=1)
    assert p.solution[0] == 3, "Result incorrect"
    p.run(["^v^v^v^v^v"], n=1, a=1)
    assert p.solution[0] == 11, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
