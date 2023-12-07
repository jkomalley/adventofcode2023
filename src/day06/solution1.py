from math import prod
import click


def getTimesAndDistances(data: list[str]) -> (list[int], list[int]):
    try:
        times = [int(val) for val in data[0].split()[1:]]
        distances = [int(val) for val in data[1].split()[1:]]
    except Exception:
        print("Error: Malformed input")
        times = []
        distances = []

    return (times, distances)


def getNumberOfWaysToWin(times: list[int], distances: list[int]) -> list[int]:
    ret = []

    for time, distance in zip(times, distances):
        # calculate the number of ways to win
        win = 0
        for buttonTime in range(time):
            travelTime = time - buttonTime
            speed = buttonTime  # in mm per ms
            distanceTraveled = speed * travelTime
            if distanceTraveled > distance:
                win += 1
        ret.append(win)

    return ret


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 6")

    data = [line.strip() for line in input.readlines()]
    input.close()

    times, distances = getTimesAndDistances(data)

    nowtw = getNumberOfWaysToWin(times, distances)

    answer = prod(nowtw)

    print(f"{answer = }")


if __name__ == "__main__":
    main()
