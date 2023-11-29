import click
import json

@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day X")

    raw_data = input.read()

    data = json.loads(raw_data)

    print(f"{data = }")

    input.close()

if __name__ == "__main__":
    main()