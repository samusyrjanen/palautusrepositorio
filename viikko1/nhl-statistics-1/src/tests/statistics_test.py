import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_player(self):
        player = self.statistics.search('Kurri')
        self.assertEqual(player.name, 'Kurri')

    def test_search_absent_player(self):
        player = self.statistics.search('Kree')
        self.assertEqual(player, None)

    def test_search_team(self):
        team = self.statistics.team('EDM')
        self.assertEqual(len(team), 3)

    def test_search_top_player(self):
        player_list = self.statistics.top(1)
        self.assertEqual(player_list[0].name, 'Gretzky')