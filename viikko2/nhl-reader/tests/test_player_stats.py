from types import SimpleNamespace

from player_stats import PlayerStats


class StubReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def test_top_scorers_by_team_returns_matching_players_by_points():
    players = [
        SimpleNamespace(name="Lower scorer", teams="DAL", ga=5),
        SimpleNamespace(name="Top scorer", teams="DAL, PIT", ga=12),
        SimpleNamespace(name="Different team", teams="NYI", ga=30),
    ]
    stats = PlayerStats(StubReader(players))

    result = stats.top_scorers_by_team(" dal ")

    assert [player.name for player in result] == ["Top scorer", "Lower scorer"]
