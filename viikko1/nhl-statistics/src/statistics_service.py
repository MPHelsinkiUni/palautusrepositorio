from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort=SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points
        def sort_by_goals(player):
            return player.goals
        def sort_by_assists(player):
            return player.assists

        if sort == SortBy.POINTS:
            sort_function = sort_by_points
        elif sort == SortBy.GOALS:
            sort_function = sort_by_goals
        elif sort == SortBy.ASSISTS:
            sort_function = sort_by_assists
# Some issue with the coverage report not recognising this even though test is present.
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_function
        )

        return sorted_players[0:how_many]
