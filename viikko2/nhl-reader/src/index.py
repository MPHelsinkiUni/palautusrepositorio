import requests
from player import Player

def is_nation(player):
    return player.nationality == "FIN"

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)
    sorted_players = sorted(players, key=lambda x: x.ga, reverse=True)

    print("Players from FIN:")
    filtered_players = filter(is_nation, sorted_players)

    for player in filtered_players:
        print(player)

if __name__ == "__main__":
    main()
