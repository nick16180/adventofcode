# this just runs all of the problems in this folder so that the output
#  can be created all at once

from pathlib import Path
from importlib import import_module as im
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
)

if __name__ == "__main__":
    for file in Path(__file__).parent.glob("xmas*.py"):
        logging.info(f"current file {file.name}")
        c = im(file.stem)
        p = c.p  # this is the problem object
        # now just run the methods to generate output
        p.run()
        p.save_for_website(file)
