import time
import logging
from typing import Any
from dataclasses import dataclass
from tqdm import tqdm
from statistics import fmean
from pathlib import Path
from os import environ
from dotenv import load_dotenv


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
)


@dataclass
class AoCProblem:
    """Advent of Code problem class. Provides common operations and data in one place."""

    year: int = None
    day: int = None
    title: str = None
    url: str = None
    args: Any = None
    durations: float = None
    solution: Any = None
    durations_mean: float = None
    date_solved: str = None
    algo = None
    website_save_location: str = None
    website_template_location: str = None
    github_url: str = None
    header_src: str = None

    def __init__(self) -> None:
        """Initializes vars from the environment only."""
        load_dotenv()
        self.website_save_location = Path(
            environ.get("website_save_location")
        ).absolute()
        self.website_template_location = Path(
            environ.get("website_template_location")
        ).absolute()
        self.header_src = environ.get("header_src")
        return None

    def run(self, args=None, n: int = 5, a: int = None):
        """Run the algorithm n times and save stats.

        Args:
            args (Any, optional): Args for algorithm. Defaults to None.
            n (int, optional): Times to run algorithm. Defaults to 5.
            a (int, optional): Index of algorithm to run. Defaults to None.

        Returns:
            None
        """
        self.durations = []
        if self.algo is None:
            raise NotImplementedError(
                "AoCProblem algo method not implemented."
            )
        algo = self.algo if a is None else [self.algo[a]]
        args = self.args if args is None else args
        for _ in tqdm(range(n)):
            tstart = time.perf_counter()
            if len(args) == len(algo):
                self.solution = [algo[i](args[i]) for i in range(len(algo))]
            tend = time.perf_counter()
            self.durations.append(round(tend - tstart, 9))
        self.durations_mean = round(fmean(self.durations), 3)
        logging.info(
            f"Solution: {self.solution} in avg {self.durations_mean} seconds."
        )
        return None

    def save_for_website(self, src: Path | str) -> None:
        """Saves AoCProblem into a markdown file using a template.

        Args:
            src (Path | str): Path to source file.

        Returns:
            None
        """
        src = Path(src)
        if not src.exists():
            raise FileNotFoundError(f"{src} does not exist.")
        with open(src, "r") as io:
            pysrc = io.read()
        mdfn = Path(self.website_save_location) / (
            src.name.replace("py", "md")
        )
        with open(mdfn, "w+") as io:
            with open(self.website_template_location, "r") as io2:
                t = io2.read()
                logging.info(f"Writing to file {mdfn}")
                t = (
                    t.replace("%date%", str(self.date_solved))
                    .replace("%title%", str(self.title))
                    .replace("%number%", f"{self.year}-{self.day}")
                    .replace("%source%", str(pysrc))
                    .replace("%solution%", str(self.solution))
                    .replace("%runtime%", str(self.durations_mean))
                    .replace("%github_url%", str(self.github_url))
                    .replace("%problem_url%", str(self.url))
                    .replace("%header_src%", str(self.header_src))
                )
                io.write(t)
        return None
