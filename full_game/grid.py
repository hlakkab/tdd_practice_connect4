import numpy as np


class Grid:

    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))

    def placer_jeton(self, column, line, jeton):
        while True:
            try:
                if column is None:
                    raise ValueError('column should not be null')

                if jeton is None:
                    raise ValueError('jeton should not be null')

                if column < 0 or column > 6:
                    raise ValueError('column should be between 0 and 6')

                self.grid[line][column] = jeton
                return True
            except ValueError as e:
                print(f"Erreur: {e}")
                column = int(input("Veuillez entrer une nouvelle valeur pour la colonne: "))

    def placer_jetonn(self, column, line, jeton):
        if column is None:
            raise ValueError('column should not be null')

        if jeton is None:
            raise ValueError('jeton should not be null')

        if column < 0 or column > 6:
            raise ValueError('column should be between 1 and 6')

        self.grid[line][column] = jeton

        return True

    def num_du_case_vide(self, column):

        while True:
            try:
                if column is None:
                    raise ValueError('column should not be null')
                if column < 0 or column > 6 :
                    raise ValueError('La colonne doit être entre 0 et 6')
                for r in range(self.rows):
                    if self.grid[r][column] == 0:
                        return r
                raise ValueError('La colonne est pleine')
            except ValueError as e:
                print(f"Erreur: {e}")
                column = input("Veuillez entrer une nouvelle valeur pour la colonne: ")

    def print_grid(self):
        print(np.flip(self.grid, 0))