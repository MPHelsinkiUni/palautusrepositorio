class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.teams = dict['team']
        self.games = dict['games']
        self.id = dict['id']
    
    def __str__(self):
        if self.nationality == "FIN":
            return f"{self.name} {self.teams} goals {self.goals} assists {self.assists}" 
        else: 
            return None 
