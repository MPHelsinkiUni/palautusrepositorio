from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def iterator(players, season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Players", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("G/A", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name, player.teams,
            str(player.goals), str(player.assists), str(player.ga)
        )

    console = Console()
    console.print(table)


def main():
    accepted = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
        "2025-26",
    ]
    while True:
        season = Prompt.ask(
            "Season [bold magenta][season from 2018 to 2026][/bold magenta]"
        )
        if season not in accepted:
            continue
        nationality = Prompt.ask(
            "Nationality [bold magenta][3-letter FIFA code][/bold magenta]"
        )
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        players = PlayerStats(reader).top_scorers_by_nationality(nationality)
        iterator(players, season, nationality)


if __name__ == "__main__":
    main()
