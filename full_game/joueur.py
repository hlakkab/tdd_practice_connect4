from full_game.jeton import Jeton


class Joueur:

    def __init__(self, name):
        self.name = name
        self.jeton = None

    def choix_couleur_jeton(self, couleur):
        self.jeton = Jeton(couleur)

    def choix_colonne(self):
        while True:
            try:
                entree = int(input(f"{self.name} Entrez le num de colunne : "))
                return entree
            except ValueError:
                print("Erreur : Veuillez entrer un entier valide.")


