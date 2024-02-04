# Advent of Code

This is just a place for me to upload my Advent of Code solutions. I made sure to not include any data or descriptions from the website per their wishes. If you do not know, Advent of Code is just a bunch of programming puzzles with a Chritmas theme, like an advent calendar.

All of the solutions are written in Python, though I might try out another programming language as I get further into the problems.

If you are interested in trying them out yourself, visit [Advent of Code](https://adventofcode.com/).

## Installation

Installing is a breeze if you have poetry installed (I highly recommend it).

Copy the repo then run the following:

```bash
cd adventofcode
poetry install
```

## Usage

The most important parts of this project are located in the ```adventofcode``` module. Within that module are helpful tools that enable quick iteration through problems because they allow for a simple workflow. Review a few of the problem solutions to understand this workflow.

The data required to run the problems is not within this repo, but if you made an account and started solving problems, you could add them to a folder called ```data``` within this repo. The name of the file should end with ```txt``` and the file's name should match the python file name that it is associated with. So, the data for the problem contained in ```problems/xmas2015d05.py``` is ```data/xmas2015d05.txt```.

I also wanted to include this code on my website [mtcactus.com](mtcactus.com), so I have a markdown template that is used to generate a markdown file for the website.