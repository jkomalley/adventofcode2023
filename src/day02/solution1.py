import click


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 2 Part A")


if __name__ == "__main__":
    main()
