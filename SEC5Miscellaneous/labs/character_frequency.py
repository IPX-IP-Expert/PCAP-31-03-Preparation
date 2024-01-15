import io


def character_frequency_ordered():
    with open("inputs/data.txt", "rt") as input:
        mapAlpha = {chr(ch): 0 for ch in range(ord("a"), ord("z") + 1)}

        lines = input.readline()
        for i in range(len(lines)):
            if str(lines[i]).lower() in mapAlpha:
                mapAlpha[str(lines[i]).lower()] += 1
                continue
            mapAlpha[lines[i]] = 1
        # Print in order and format like a -> 1
        for char in sorted(mapAlpha.keys(), key=lambda k: mapAlpha[k], reverse=True):
            if mapAlpha[char] > 0:
                print(f"{char} -> {mapAlpha[char]}")


if __name__ == "__main__":
    character_frequency_ordered()
