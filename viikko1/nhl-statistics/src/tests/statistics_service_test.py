import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self) :
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
    
    def test_search_non_existing_player(self) :
        player = self.stats.search("None")
        self.assertIsNone(player)

    def test_team_players(self) :
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        player_names = [player.name for player in team_players]
        self.assertIn("Semenko", player_names)
        self.assertIn("Kurri", player_names)
        self.assertIn("Gretzky", player_names)
    
    def test_top_scorers(self) :
        top_players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
    
    def test_top_scorers_goals(self) :
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")
    
    def test_top_scorers_assists(self) :
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Lemieux")

