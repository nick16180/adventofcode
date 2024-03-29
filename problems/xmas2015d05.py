from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from collections import Counter


def is_nice1(s: str) -> bool:
    # determine if a string is nice based on rules given
    VOWELS = ["a", "e", "i", "o", "u"]
    RESTR = ["ab", "cd", "pq", "xy"]
    # check for vowels
    test1 = sum([1 for c in s if c in VOWELS]) >= 3
    # check for restriced letter pairs
    test2 = False
    for r in RESTR:
        test2 = r in s
        if test2:
            break
    # look for doubles
    test3 = False
    x = list(range(0, len(s)))
    y = x[1:]
    x = x[: len(x)]
    for p in zip(x, y):
        # checks for doubles
        test3 = s[p[0]] == s[p[1]]
        if test3:
            break
    return test1 and not test2 and test3


def is_nice2(s: str) -> bool:
    # look for pairs of letters that appear 2+ times
    # then make sure there are not runs of three within runs of four
    # this is specifically excluded from the rules
    test1 = True
    x = list(range(0, len(s)))
    y = x[1:]
    x = x[: len(x)]
    pairs = [s[p[0]] + s[p[1]] for p in zip(x, y)]
    cpairs = Counter(pairs)
    dpairs = list(filter(lambda k: cpairs[k] > 1, cpairs.keys()))
    if len(dpairs) == 0:
        test1 = False
    for p in dpairs:
        if p[0] == p[1]:
            if p[0] * 3 in s and p[0] * 4 not in s:
                test1 = False
                break
    # look for groups of three letters where the first and third are the same
    test2 = False
    x = list(range(0, len(s)))
    y = [i + 1 for i in x[1 : len(x) - 1]]
    x = x[: len(x) - 1]
    for p in zip(x, y):
        test2 = s[p[0]] == s[p[1]]
        if test2:
            break
    return test1 and test2


def algo1(args: str) -> int:
    lines = args.splitlines()
    return sum([int(is_nice1(line)) for line in lines])


def algo2(args: str) -> int:
    lines = args.splitlines()
    return sum([int(is_nice2(line)) for line in lines])


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 5
p.title = "Doesn't He Have Intern-Elves For This?"
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
    p.run(["ugknbfddgicrmopn"], n=1, a=0)
    assert p.solution[0] == 1, "Result incorrect"
    p.run(["aaa"], n=1, a=0)
    assert p.solution[0] == 1, "Result incorrect"
    p.run(["jchzalrnumimnmhp"], n=1, a=0)
    assert p.solution[0] == 0, "Result incorrect"
    p.run(["haegwjzuvuyypxyu"], n=1, a=0)
    assert p.solution[0] == 0, "Result incorrect"
    p.run(["dvszwmarrgswjxmb"], n=1, a=0)
    assert p.solution[0] == 0, "Result incorrect"
    p.run(["qjhvhtzxzqqjkmpb"], n=1, a=1)
    assert p.solution[0] == 1, "Result incorrect"
    p.run(["xxyxx"], n=1, a=1)
    assert p.solution[0] == 1, "Result incorrect"
    p.run(["uurcxstgmygtbstg"], n=1, a=1)
    assert p.solution[0] == 0, "Result incorrect"
    p.run(["ieodomkazucvgmuy"], n=1, a=1)
    assert p.solution[0] == 0, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
