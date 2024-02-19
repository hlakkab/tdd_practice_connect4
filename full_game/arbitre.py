class Arbitre:

    def check_if_player_win(grid, joueur):
        for r in range(grid.rows):
            for c in range(grid.cols):
                if c <= grid.cols - 4:
                    if all(grid.grid[r][c + i] == joueur.jeton.couleur for i in range(4)):
                        return True

                if r <= grid.rows - 4:
                    if all(grid.grid[r + i][c] == joueur.jeton.couleur for i in range(4)):
                        return True

                if c <= grid.cols - 4 and r <= grid.rows - 4:
                    if all(grid.grid[r + i][c + i] == joueur.jeton.couleur for i in range(4)):
                        return True

                if c >= 3 and r <= grid.rows - 4:
                    if all(grid.grid[r + i][c - i] == joueur.jeton.couleur for i in range(4)):
                        return True

        return False

    def donner_la_main(self,my_grid, joueur):

        column_nbr_str = joueur.choix_colonne()
        place_vide = my_grid.num_du_case_vide(column_nbr_str)
        column_nbr = int(column_nbr_str)
        placer = my_grid.placer_jeton(column_nbr, place_vide, joueur.jeton.couleur)
        my_grid.print_grid()

