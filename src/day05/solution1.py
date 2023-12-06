import re
import click


def getSeeds(data: str) -> list[int]:
    ret = []

    match = re.match(r"seeds:( \d+)+\n", data)

    if match:
        ret = [int(seed) for seed in match[0].split()[1:]]

    return ret


def mapChunks(map: list[int], size: int):
    return (map[pos:pos + size] for pos in range(0, len(map), size))


def getMappings(data: str) -> list[tuple[tuple[int, int, int]]]:
    ret = []

    data = data.split("\n\n")[1:]

    for map in data:
        splitMap = [int(v) for v in map.split()[2:]]
        if len(splitMap) % 3 != 0:
            print(f"Error: malformed mapping: {map}")
            return []
        cur = []
        for chunk in mapChunks(splitMap, 3):
            cur.append(tuple(chunk))
        ret.append(tuple(cur))
    return ret


def getLocationsFromMappings(seeds: list[int], mappings: list[tuple[tuple[int, int, int]]]) -> list[int]:
    ret = []

    #for each seed
    #   for each mapping set
    #       for each mapping
    #           check if the current seed is in the source range
    #           if it is, map it
    #           otherwise is remains the same
    #   append the final value to ret

    for seed in seeds:
        for mappingSet in mappings:
            for map in mappingSet:
                if seed in range(map[1], map[1] + map[2]):
                    seed = map[0] + (seed - map[1])
                    break

        ret.append(seed)

    return ret


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 1")

    data = input.read()
    input.close()

    seeds = getSeeds(data)

    # get the mappings
    mappings = getMappings(data)

    # use the mappings to get the location numbers
    locations = getLocationsFromMappings(seeds, mappings)

    # get the lowest location number
    answer = min(locations, default=0)

    print(f"{answer = }")


if __name__ == "__main__":
    main()
