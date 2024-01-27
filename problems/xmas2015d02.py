from dotenv import load_dotenv
from os import environ
from pathlib import Path


def algo1(args):
    y = [[int(v) for v in line.split("x")] for line in args.splitlines()]
    z = [[row[0] * row[1], row[1] * row[2], row[0] * row[2]] for row in y]
    zz = [min(row) + 2 * sum(row) for row in z]
    return sum(zz)


def algo2(args):
    y = [[int(v) for v in line.split("x")] for line in args.splitlines()]
    z = [row[0] * row[1] * row[2] + 2 * (sum(row) - max(row)) for row in y]
    return sum(z)


load_dotenv()
args = None
fn = Path(environ.get("data_folder")).absolute() / (Path(__file__).stem + ".txt")
with open(fn, "r") as io:
    args = io.read()

print(algo1(args))
print(algo2(args))
