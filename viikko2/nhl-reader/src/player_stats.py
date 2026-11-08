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
