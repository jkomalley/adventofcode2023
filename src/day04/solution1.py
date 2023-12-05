import click


def calculateCardValue(numWinning: int) -> int:
    val = 0
    if numWinning > 0:
        val = 1
        for _ in range(numWinning - 1):
            val += val

    return val


def getCardValues(data: list[str]) -> list[int]:
    ret = []

    for line in data:
        # parse line for winning nums and my numbers. Store in set objects
        _, line = line.split(": ")
        winningNumbers, myNumbers = line.split(" | ")

        winningNumbers = set([int(n) for n in winningNumbers.split()])
        myNumbers = set([int(n) for n in myNumbers.split()])

        # use intersection to count number of winning numbers I have
        numWinning = len(winningNumbers.intersection(myNumbers))

        # calculate card value based on number of winning numbers
        ret.append(calculateCardValue(numWinning))

    return ret


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 4")

    data = input.readlines()
    input.close()

    answer = sum(getCardValues(data))

    print(f"{answer = }")


if __name__ == "__main__":
    main()
