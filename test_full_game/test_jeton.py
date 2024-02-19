import unittest
from full_game.jeton import Jeton

class MyTestCase(unittest.TestCase):


    def test_with_given_color(self):
        jeton = Jeton()
        self.assertEqual(jeton.couleur, "rouge")
    def test_with_default_color(self):
        jeton = Jeton("bleu")
        self.assertEqual(jeton.couleur, "bleu")

if __name__ == '__main__':
    unittest.main()
