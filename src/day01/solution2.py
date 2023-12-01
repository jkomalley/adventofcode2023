import re
import click


def convertSpelledNums(line: str) -> str:
    ret = ""
    strs_to_nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "eno": "1",
        "owt": "2",
        "eerht": "3",
        "ruof": "4",
        "evif": "5",
        "xis": "6",
        "neves": "7",
        "thgie": "8",
        "enin": "9",
    }
    strsRegex = "".join([s + "|" for s in strs_to_nums.keys()])

    while line:
        matches = re.search(strsRegex, line)
        if matches[0] == "":
            ret += line[0]
            line = line[1:]
        else:
            ret += strs_to_nums[matches[0]]
            line = line[matches.end() :]

    return ret


def getNumber(line: str) -> int:
    convertedLine = convertSpelledNums(line)
    digits = [c for c in convertedLine if c.isdigit()]
    firstDigit = digits[0]

    convertedLine = convertSpelledNums(line[::-1])
    digits = [c for c in convertedLine if c.isdigit()]
    secondDigit = digits[0]

    ret = int(firstDigit + secondDigit)

    return ret


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
