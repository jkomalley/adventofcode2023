import click

def getNumber(line: str) -> int:
    digits = [c for c in line if c.isdigit()]

    return int("".join([digits[0], digits[-1]]))

@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 1")

    data = input.readlines()
    input.close()

    total = sum(map(getNumber, data))

    print(f"Answer: {total}")

if __name__ == "__main__":
    main()
