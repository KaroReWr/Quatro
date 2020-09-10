from Pionek import Pionek

class Board:
    def __init__(self):
        p1 = Pionek()
        p2 = Pionek()
        self.pionki = []
        self.pionki.append(p1)
        self.pionki.append(p2)

    def __str__(self):
        pionki = ''
        for pion in self.pionki:
            pionki += str(pion) + '\n'
        return pionki

