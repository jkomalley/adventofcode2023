from math import prod
import re
from typing import TextIO
import click


def get(s, color):
    ret = 0
    regex = rf"\d+ {color}"

    val = re.search(regex, s)

    if val:
        val = re.match(r"\d+", val[0])

    if val:
        ret = int(val[0])

    return ret


def getMinColors(line: str) -> tuple[int, int, int]:
    sets = line.split("; ")
    minR = 0
    minG = 0
    minB = 0
    for s in sets:
        rNum = get(s, "red")
        gNum = get(s, "green")
        bNum = get(s, "blue")
        
        minR = max(minR, rNum)
        minG = max(minG, gNum)
        minB = max(minB, bNum)

    return (minR, minG, minB)


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input: TextIO):
    print("Advent of Code Day 2 Part A")

    data = input.readlines()

    total = 0
    for line in data:
        ret = getMinColors(line[8:])
        power = prod(ret)
        total += power

    print(f"answer = {total}")


if __name__ == "__main__":
    main()
