from unittest import TestCase
from full_game.grid import *
from full_game.arbitre import *
from full_game.joueur import *

class TestArbitre(TestCase):

    def setUp(self):
        self.grid = Grid()
        self.j1 = Joueur("hamza")
        self.j1.choix_couleur_jeton(1)

    def test_check_if_player_win_line(self):
        arbitre = Arbitre
        for i in range(4):
            self.grid.placer_jeton(0, i, 1)

        self.assertTrue(arbitre.check_if_player_win(self.grid, self.j1))

    def test_check_if_player_win_col(self):
        arbitre = Arbitre
        for i in range(4):
            self.grid.placer_jeton(i, 0, 1)

        self.assertTrue(arbitre.check_if_player_win(self.grid, self.j1))

    def test_check_if_player_win_diagonals(self):
        arbitre = Arbitre
        for i in range(4):
            self.grid.placer_jeton(i, i, 1)

        self.assertTrue(arbitre.check_if_player_win(self.grid, self.j1))

    def test_check_if_player_win_anti_diagonals(self):
        arbitre = Arbitre
        for i in range(4):
            self.grid.placer_jeton(4-i, i, 1)

        self.assertTrue(arbitre.check_if_player_win(self.grid, self.j1))

    def test_donner_la_main(self):
        self.fail()
