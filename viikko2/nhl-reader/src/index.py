import requests
from player import Player
from rich import print
from rich.prompt import Prompt
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    accepted = ["2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26"]
    while True:
        season = Prompt.ask(f"\nSeason [bold magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/bold magenta]")
        if season not in accepted:
            continue
        nationality = Prompt.ask(f"\nNationality [bold magenta][Use standard 3-letter FIFA code][/bold magenta]")
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        for player in players:
            print(player)

if __name__ == "__main__":
    main()
