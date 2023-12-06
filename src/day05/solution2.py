import re
import click


def getSeeds(data: str) -> list[int]:
    ret = []

    match = re.match(r"seeds:( \d+)+\n", data)

    if match:
        ret = [int(seed) for seed in match[0].split()[1:]]

    print(f"seeds: {ret}")

    return ret


def mapChunks(map: list[int], size: int):
    return (map[pos:pos + size] for pos in range(0, len(map), size))


def getMappings(data: str) -> list[tuple[tuple[int, int, int]]]:
    ret = []

    data = data.split("\n\n")[1:]

    for map in data:
        splitMap = [int(v) for v in map.split()[2:]]
        # print(f"{splitMap = }")
        if len(splitMap) % 3 != 0:
            print(f"Error: malformed mapping: {map}")
            return []
        cur = []
        for chunk in mapChunks(splitMap, 3):
            # print(f"{chunk = }")
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
        # print(f"seed: {seed}", end=" ")
        for mappingSet in mappings:
            print(f"Mapping set: {mappingSet}")
            print(f"Seed: {seed}")
            for map in mappingSet:
                # print(f"{map = } {seed = }")
                
                if seed in range(map[1], map[1] + map[2]):
                    # print("seed = map[0] + (seed - map[1])")
                    # print(f"seed = {map[0]} + ({seed} - {map[1]})")
                    print(map)
                    seed = map[0] + (seed - map[1])
                    break
            # print(f"Seed out: {seed}")
            # print(f"{seed}", end=" ")
        print(f"Final seed: {seed}")
        ret.append(seed)
        print()

    return ret


@click.command()
@click.option("-i", "--input", required=True, type=click.File("r"))
def main(input):
    print("Advent of Code Day 1")

    data = input.read()
    input.close()

    _data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
    seeds = getSeeds(data)

    # get the mappings
    mappings = getMappings(data)
    # print(mappings)

    # use the mappings to get the location numbers
    locations = getLocationsFromMappings(seeds, mappings)
    print(locations)

    # get the lowest location number
    answer = min(locations, default=0)

    print(f"{answer = }")


if __name__ == "__main__":
    main()
