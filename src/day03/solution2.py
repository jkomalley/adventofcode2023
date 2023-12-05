import re
import string
import click


def checkForSymbols(data, x, y):
    ret = False

    symbols = set(string.punctuation) - set(".")

    xMax = len(data[y])
    yMax = len(data)

    # check up (y-1,x)
    if y > 0:
        if data[y - 1][x] in symbols:
            ret = True

    # check up right (y-1,x+1)
    if y > 0 and x + 1 < xMax:
        if data[y - 1][x + 1] in symbols:
            ret = True

    # check right (y,x+1)
    if x + 1 < xMax:
        if data[y][x + 1] in symbols:
            ret = True

    # check down right (y+1,x+1)
    if y + 1 < yMax and x + 1 < xMax:
        if data[y + 1][x + 1] in symbols:
            ret = True

    # check down (y+1,x)
    if y + 1 < yMax:
        if data[y + 1][x] in symbols:
            ret = True

    # check down left (y+1,x-1)
    if y + 1 < yMax and x > 0:
        if data[y + 1][x - 1] in symbols:
            ret = True

    # check left (y,x-1)
    if x > 0:
        if data[y][x - 1] in symbols:
            ret = True

    # check up left (y-1,x-1)
    if y > 0 and x > 0:
        if data[y - 1][x - 1] in symbols:
            ret = True

    return ret


def getPartNumbers(data: list[str]) -> list[int]:
    ret = []
    curNum = None
    setNone = None

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if x == setNone:
                curNum = None
                setNone = None

            if c.isdigit():
                if curNum == None:
                    curNum = re.match("\d+", data[y][x:])[0]
                    # print(f"{curNum = }")
                    setNone = x + len(curNum)
                    curNum = int(curNum)
                if checkForSymbols(data, x, y) and curNum:
                    # print(curNum)
                    ret.append(curNum)
                    curNum = 0

    return ret


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 3")

    data = input.readlines()

    # data = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598..",
    # ]

    dataArray = getPartNumbers(data)

    answer = sum(dataArray)

    print(f"{answer = }")


if __name__ == "__main__":
    main()
