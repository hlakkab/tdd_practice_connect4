
class Game:

    def __init__(self, arbitre, joueur1, joueur2, grid):
        self.arbitre = arbitre
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.grid = grid
        self.game_over = False




    def start_game(self):
        turn = 0
        while not self.game_over:

            if turn == 0:

                self.arbitre.donner_la_main(self.arbitre, self.grid, self.joueur1)
                if self.arbitre.check_if_player_win(self.grid, self.joueur1):
                    print(f"{self.joueur1.jeton.couleur} won")
                    self.game_over = True

            else:

                self.arbitre.donner_la_main(self.arbitre, self.grid, self.joueur2)
                if self.arbitre.check_if_player_win(self.grid, self.joueur2):
                    print(f"{self.joueur2.jeton.couleur} won")
                    self.game_over = True

            turn += 1
            turn = turn % 2

