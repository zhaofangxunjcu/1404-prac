"""
Word Occurrences
Estimate: 20 minutes
Actual:   64 minutes
"""
def read_file(filename):
    """Read  file and return a list excluding header"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]  # Skip header
    data = [line.strip().split(",") for line in lines]
    return data


def count_champions(data):
    """Count how many times the champion has won."""
    champion_count = {}
    for row in data:
        champion = row[2]
        champion_count[champion] = champion_count.get(champion, 0) + 1
    return champion_count


def get_countries(data):
    """Get a list of countries of champions."""
    countries = {row[1] for row in data}
    return sorted(countries)


def main():
    filename = "wimbledon.csv"
    data = read_file(filename)

    champion_count = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == '__main__':
    main()
