from unittest import TestCase
from full_game.grid import Grid


class TestGrid(TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_default_initialising(self):
        grid = Grid()
        self.assertEqual(grid.rows, 6)
        self.assertEqual(grid.cols, 7)

    def test_given_initialising(self):
        grid = Grid(8, 9)
        self.assertEqual(grid.rows, 8)
        self.assertEqual(grid.cols, 9)

    def tester_placer_jeton(self):
        for i in range(self.grid.cols):
            print(i)
        self.assertTrue(self.grid.placer_jeton(1, 1, 1))
        self.assertEqual(self.grid.grid[1][1], 1)

    def test_placer_jeton(self):
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                self.assertTrue(self.grid.placer_jeton(col, row, 1))
                self.assertEqual(self.grid.grid[row][col], 1)

    def test_placer_jeton_out_of_range(self):
        with self.assertRaises(ValueError):
            self.grid.placer_jeton(0, 2, 1)
            self.grid.placer_jeton(9, 2, 1)

    def test_placer_dans_une_colon_null(self):
        with self.assertRaises(ValueError) as context:
            self.grid.placer_jeton(None, 2, 1)
        self.assertEqual(str(context.exception), 'column should not be null')

    def tester_placer_un_jeton_null(self):
        with self.assertRaises(ValueError) as context:
            self.grid.placer_jeton(3, 2, None)
        self.assertEqual(str(context.exception), 'jeton should not be null')

    def tester_placer_dans_une_colon_plein(self):
        self.grid.placer_jeton(1, 0, 1)
        self.grid.placer_jeton(1, 1, 1)
        self.grid.placer_jeton(1, 2, 1)
        self.grid.placer_jeton(1, 3, 1)
        self.grid.placer_jeton(1, 4, 1)
        self.grid.placer_jeton(1, 5, 1)

        with self.assertRaises(ValueError) as context:
            self.grid.num_du_case_vide(1)
        self.assertEqual(str(context.exception), 'column is full')
