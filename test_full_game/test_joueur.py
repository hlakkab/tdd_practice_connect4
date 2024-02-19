from unittest import TestCase
from full_game.joueur import Joueur
from unittest.mock import patch


class TestJoueur(TestCase):
    def setUp(self):
        self.mock_input_choix_colonne = patch('builtins.input', return_value='5')
        self.mock_input_choix_colonne_non_valid = patch('builtins.input', return_value='1B')
        self.mock_input_choix_colonne.start()
        self.mock_input_choix_colonne_non_valid.start()

    def tearDown(self):
        self.mock_input_choix_colonne.stop()
        self.mock_input_choix_colonne_non_valid.stop()

    def test_choix_couleur_jeton(self):
        j1 = Joueur("hamza")
        j1.choix_couleur_jeton("rouge")
        self.assertEqual(j1.jeton.couleur,"rouge")

    def test_choix_colonne(self):
        joueur = Joueur("hamza")
        colonne = joueur.choix_colonne()
        self.assertEqual(colonne, '5')

    def test_choix_colonne_non_valid(self):
        with self.assertRaises(ValueError):
            joueur = Joueur("hamza")
            joueur.choix_colonne()

