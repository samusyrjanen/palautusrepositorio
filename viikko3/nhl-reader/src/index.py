import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = []
        for player_dict in self.response:
            player = Player(
                player_dict
            )
            self.players.append(player)

    def get_players(self):
        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        players = list(filter(lambda a: a.nationality==nationality, self.players))


        print(f"Players from {nationality}:")
            
        players.sort(reverse=True, key=lambda a: a.goals+a.assists)

        return players

if __name__ == "__main__":
    main()
