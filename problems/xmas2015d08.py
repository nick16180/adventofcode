from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from codecs import decode


def charcounter1(s: str) -> dict:
    # counts characters based on problem
    # decoded strings give the correct length
    t = decode(str(s[1:-1]), "unicode_escape")
    return {
        "memory": len(t),
        "memorystr": t,
        "code": len(s),
        "codestr": s,
    }


def charcounter2(s: str) -> dict:
    # counts characters based on problem
    t = decode(str(s[1:-1]), "unicode_escape")
    u = s
    # instead of trying to use existing methods to escape strings, just count
    x = len(u) + 2
    # count extra if quotes or foward slashes appear
    # if there is one char found, then the string will split into two
    # if two are found, then split into three, etc
    # so substract one
    x += len(u.split('"')) - 1
    x += len(u.split("\\")) - 1
    return {
        "code": len(s),
        "codestr": s,
        "final": x,
        "finalstr": u,
    }


def algo1(args: str) -> int:
    # count chars then find difference in amounts
    counted = [charcounter1(line) for line in args.splitlines()]
    x = sum(map(lambda x: x.get("code"), counted))
    y = sum(map(lambda x: x.get("memory"), counted))
    return x - y


def algo2(args: str) -> int:
    # count chars then find difference in amounts
    counted = [charcounter2(line) for line in args.splitlines()]
    x = sum(map(lambda x: x.get("final"), counted))
    y = sum(map(lambda x: x.get("code"), counted))
    return x - y


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 8
p.title = "Matchsticks"
fn = Path(environ.get("data_folder")).absolute() / (
    Path(__file__).stem + ".txt"
)
args = read_text(fn)
p.algo = [algo1, algo2]
p.args = [args, args]
p.date_solved = "2024-02-04"
p.url = f"https://adventofcode.com/{p.year}/day/{p.day}"
p.github_url = environ.get("github_url") + "/".join(
    ["problems", Path(__file__).name]
)


if __name__ == "__main__":
    # test the given input
    p.run([r'""'], n=1, a=0)
    assert p.solution[0] == (2 - 0), "Result incorrect"
    p.run([r'"abc"'], n=1, a=0)
    assert p.solution[0] == (5 - 3), "Result incorrect"
    p.run([r'"aaa\"aaa"'], n=1, a=0)
    assert p.solution[0] == (10 - 7), "Result incorrect"
    p.run([r'"\x27"'], n=1, a=0)
    assert p.solution[0] == (6 - 1), "Result incorrect"
    p.run([r'""'], n=1, a=1)
    assert p.solution[0] == (6 - 2), "Result incorrect"
    p.run([r'"abc"'], n=1, a=1)
    assert p.solution[0] == (9 - 5), "Result incorrect"
    p.run([r'"aaa\"aaa"'], n=1, a=1)
    assert p.solution[0] == (16 - 10), "Result incorrect"
    p.run([r'"\x27"'], n=1, a=1)
    assert p.solution[0] == (11 - 6), "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
