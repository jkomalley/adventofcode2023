import click


def getCardValues(data: list[str]) -> list[int]:
    ret = []

    for line in data:
        _, line = line.split(": ")
        print(line)
        winningNumbers, myNumbers = line.split(" | ")

        winningNumbers = set([int(n) for n in winningNumbers.split()])
        myNumbers = set([int(n) for n in myNumbers.split()])

        # print(f"{winningNumbers = } {myNumbers = }")

        numWinning = len(winningNumbers.intersection(myNumbers))

        print(f"{numWinning = }")

        val = 0
        if numWinning > 0:
            val = 1
            for _ in range(numWinning - 1):
                val += val

        print(f"{val = }")
        ret.append(val)



    return ret


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 4")

    data = input.readlines()
    input.close()

    # data = [
    #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    # ]

    answer = sum(getCardValues(data))

    print(f"{answer = }")


if __name__ == "__main__":
    main()
