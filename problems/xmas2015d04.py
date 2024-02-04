from adventofcode.AoCProblem import AoCProblem
from adventofcode.utils import read_text
from dotenv import load_dotenv
from os import environ
from pathlib import Path
from hashlib import md5


def hash_search(args: str, n: int) -> int:
    # this is just a brute force search through all hashes
    # looks for the first hash that has n leading zeroes
    # there might be a smarter way to do this but i am not implementing the
    # md5 algorithm
    found = False
    i = 0
    while not found:
        m = args + str(i)
        x = md5(m.encode())
        y = str(x.hexdigest())
        if y[:n] == "0" * n:
            found = True
        else:
            i += 1
    return i


def algo1(args: str):
    return hash_search(args, 5)


def algo2(args: str):
    return hash_search(args, 6)


# set up problem
load_dotenv()
p = AoCProblem()
p.year = 2015
p.day = 4
p.title = "The Ideal Stocking Stuffer"
args = "ckczppom"
p.algo = [algo1, algo2]
p.args = [args, args]
p.date_solved = "2024-01-27"
p.url = f"https://adventofcode.com/{p.year}/day/{p.day}"
p.github_url = environ.get("github_url") + "/".join(
    ["problems", Path(__file__).name]
)


if __name__ == "__main__":
    # test the given input
    p.run(["abcdef"], n=1, a=0)
    assert p.solution[0] == 609043, "Result incorrect"
    p.run(["pqrstuv"], n=1, a=0)
    assert p.solution[0] == 1048970, "Result incorrect"

    # test
    p.run(n=1)

    # get average time
    p.run()

    # save to website markdown
    p.save_for_website(__file__)
