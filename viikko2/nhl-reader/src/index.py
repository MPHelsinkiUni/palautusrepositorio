from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def display_players(players, season, search):
    table = Table(title=f"Season {season} players: {search}")

    table.add_column("Players", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name, player.teams,
            str(player.goals), str(player.assists), str(player.ga)
        )

    console = Console()
    console.print(table)


def search_players(stats):
    search_type = Prompt.ask(
        "Search by", choices=["nationality", "team"]
    )
    if search_type == "nationality":
        nationality = Prompt.ask(
            "Nationality [bold magenta][3-letter FIFA code][/bold magenta]"
        )
        return (
            stats.top_scorers_by_nationality(nationality),
            f"nationality {nationality}",
        )

    team = Prompt.ask("Team [bold magenta][3-letter NHL code][/bold magenta]")
    return stats.top_scorers_by_team(team), f"team {team.upper()}"


def run_season(season):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    players, search = search_players(stats)
    display_players(players, season, search)


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
        run_season(season)


if __name__ == "__main__":
    main()
