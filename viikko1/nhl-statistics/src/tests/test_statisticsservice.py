import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_finds_no_one(self):
        player = self.stats.search("Selanne")
        self.assertIsNone(player)

    def test_search_finds_partial_name(self):
        player = self.stats.search("Gret")
        self.assertEqual(player.name, "Gretzky")

    def test_team_returns_players(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty(self):
        players = self.stats.team("XXX")
        self.assertEqual(players, [])

    def test_players_points_order(self):
        players = self.stats.top(3)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_returns_all_players(self):
        players = self.stats.top(4)
        self.assertEqual(len(players), 4)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[-1].name, "Kurri")

    def test_string_output(self):
        string = self.stats.search("Lemieux")

        self.assertEqual(
            str(string),
            "Lemieux PIT 45 + 54 = 99"
        )

### sort
    def test_sort_points(self):
        players = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )
        ## DEFAULT as well
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )


    def test_sort_goals(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"]
        )


    def test_sort_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )
