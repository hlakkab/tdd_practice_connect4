from full_game.joueur import Joueur
from full_game.game import Game
from full_game.arbitre import Arbitre
from full_game.grid import Grid
import sys

name = input("name of p1 : ")
J1 = Joueur(name)
nbr1 = input("choose 1 or 2 : ")
J1.choix_couleur_jeton(int(nbr1))

name1 = input("name of p2 : ")
J2 = Joueur(name1)

if int(nbr1) == 1:
    J2.choix_couleur_jeton(2)
else:
    J2.choix_couleuar_jeton(1)

arbitre = Arbitre
grid = Grid()

"""game = Game(arbitre, J1, J2, grid)
game.start_game()

rejouer = input("rejouer ? (o/n)")

if rejouer == "o":
    game.start_game()
elif rejouer == "n":
    print("à la prochaine")"""
while True:
    game = Game(arbitre, J1, J2, grid)
    game.start_game()

    rejouer = input("Voulez-vous rejouer ? (o/n) : ")
    if rejouer.lower() != "o":
        print("Au revoir !")
        sys.exit()
