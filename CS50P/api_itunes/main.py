import sys

import requests


def main():
    if len(sys.argv) != 2:
        sys.exit()

    repo = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
    )

    # print(json.dumps(repo.json(), indent = 3))

    o = repo.json()
    for res in o["results"]:
        print(res["trackName"])


main()
