"""
CP1404 - Practical 5
Program that: Reads wimbledon.csv file, process the data and display processed information for:
- the champions and how many times they have won.
- the countries of the champions in alphabetical order
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read csv file and print details"""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_records(champion_to_count, countries)


def get_records(filename):
    """Get records from the file in list-of-lists format"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Process champions and set of countries from list of lists into dictionary"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_records(champion_to_count, countries):
    """Prints champions and countries with fancy format"""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(name, count)
    print(
        f"""\nThese {len(countries)} countries have won Wimbledon: \n{', '.join(country for country in sorted(countries))}""")


main()
