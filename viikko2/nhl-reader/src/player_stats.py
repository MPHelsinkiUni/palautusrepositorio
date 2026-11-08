class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        sorted_players = sorted(players, key=lambda x: x.ga, reverse=True)
        filtered_players = filter(
            lambda x: x.nationality == nationality, sorted_players
        )
        return filtered_players

    def top_scorers_by_team(self, team):
        players = self.reader.get_players()
        team = team.strip().upper()
        team_players = [
            player
            for player in players
            if team
            in {
                player_team.strip().upper()
                for player_team in player.teams.split(",")
            }
        ]
        return sorted(team_players, key=lambda player: player.ga, reverse=True)

    def top_goal_scorers(self, how_many):
        players = self.reader.get_players()
        sorted_players = sorted(players, key=lambda x: x.g, reverse=True)
        return sorted_players[:how_many]
