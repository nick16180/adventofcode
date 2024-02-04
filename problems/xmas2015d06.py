from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path


def parse_line(s: str) -> dict:
    # parses an input line into a dict for easy usage later
    op = "toggle" if "toggle" in s else "on" if "turn on" in s else "off"
    _s = (
        s.replace("toggle", "")
        .replace("turn on", "")
        .replace("turn off", "")
        .replace("through", "")
        .replace("  ", " ")
        .strip()
        .split(" ")
    )
    pair1 = [int(v) for v in _s[0].split(",")]
    pair2 = [int(v) for v in _s[1].split(",")]
    return {"operation": op, "box_tl": pair1, "box_br": pair2}


def algo1(args: str, size=1000) -> int:
    # initialize grid, then set each value based on line operation
    grid = [[0 for i in range(size)] for i in range(size)]
    parsed = [parse_line(line) for line in args.splitlines()]
    for p in parsed:
        # need the +1 because range is 0-indexed
        r1 = range(p.get("box_tl")[0], p.get("box_br")[0] + 1)
        r2 = range(p.get("box_tl")[1], p.get("box_br")[1] + 1)
        for i in r1:
            for j in r2:
                if p.get("operation") == "on":
                    grid[i][j] = 1
                elif p.get("operation") == "off":
                    grid[i][j] = 0
                else:
                    grid[i][j] = (grid[i][j] + 1) % 2
    return sum([sum(row) for row in grid])


def algo2(args: str, size=1000) -> int:
    # initialize grid, then set each value based on line operation
    grid = [[0 for i in range(size)] for i in range(size)]
    parsed = [parse_line(line) for line in args.splitlines()]
    for p in parsed:
        # need the +1 because range is 0-indexed
        r1 = range(p.get("box_tl")[0], p.get("box_br")[0] + 1)
        r2 = range(p.get("box_tl")[1], p.get("box_br")[1] + 1)
        for i in r1:
            for j in r2:
                if p.get("operation") == "on":
                    grid[i][j] += 1
                elif p.get("operation") == "off":
                    grid[i][j] = max(0, grid[i][j] - 1)
                else:
                    grid[i][j] += 2
    return sum([sum(row) for row in grid])


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 6
p.title = "Probably a Fire Hazard"
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
    p.run(["turn on 0,0 through 999,999"], n=1, a=0)
    assert p.solution[0] == 1_000_000, "Result incorrect"
    p.run(["toggle 0,0 through 999,0"], n=1, a=0)
    assert p.solution[0] == 1000, "Result incorrect"
    p.run(["turn off 499,499 through 500,500"], n=1, a=0)
    assert p.solution[0] == 0, "Result incorrect"
    p.run(["turn on 0,0 through 0,0"], n=1, a=1)
    assert p.solution[0] == 1, "Result incorrect"
    p.run(["toggle 0,0 through 999,999"], n=1, a=1)
    assert p.solution[0] == 2_000_000, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
