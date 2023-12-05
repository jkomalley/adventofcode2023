import re
from typing import TextIO
import click


def getGameNum(line):
    return re.search(r"\d+", line).group()


def get(s, color):
    ret = 0
    # print(f"{s = } : {color = }")
    regex = rf"\d+ {color}"
    val = re.search(regex, s)

    # print(val)

    if val:
        val = re.match(r"\d+", val[0])

    if val:
        ret = int(val[0])

    # print(f"Found {ret} {color}")

    return ret


def isPossible(line, r, g, b):
    sets = line.split("; ")
    for s in sets:
        rNum = get(s, "red")
        gNum = get(s, "green")
        bNum = get(s, "blue")
        if rNum > r or gNum > g or bNum > b:
            # print(f"Not possible: {rNum = } {gNum = } {bNum = }")
            return False
        # print(f"Possible: {rNum = } {gNum = } {bNum = }")
    return True


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
@click.option("-r", default=12)
@click.option("-g", default=13)
@click.option("-b", default=14)
def main(input: TextIO, r, g, b):
    print("Advent of Code Day 2 Part A")

    data = input.readlines()

    # data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    #         ]

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
