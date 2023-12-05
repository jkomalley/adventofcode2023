import re
from typing import TextIO
import click


def getGameNum(line):
    return re.search(r"\d+", line).group()


def get(s, color):
    ret = 0

    regex = rf"\d+ {color}"
    val = re.search(regex, s)

    if val:
        val = re.match(r"\d+", val[0])

    if val:
        ret = int(val[0])

    return ret


def isPossible(line, r, g, b):
    sets = line.split("; ")
    for s in sets:
        rNum = get(s, "red")
        gNum = get(s, "green")
        bNum = get(s, "blue")
        if rNum > r or gNum > g or bNum > b:
            return False
    return True


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
@click.option("-r", default=12)
@click.option("-g", default=13)
@click.option("-b", default=14)
def main(input: TextIO, r, g, b):
    print("Advent of Code Day 2 Part A")

    data = input.readlines()

    total = 0
    for line in data:
        gameNum = getGameNum(line)
        ret = isPossible(line[8:], r, g, b)

        print(f"Game {gameNum}: {ret}")

        if ret:
            total += int(gameNum)

    print(f"{total = }")


if __name__ == "__main__":
    main()
