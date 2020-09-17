from Pionek import Pionek

class Board:
    def __init__(self):
        p1 = Pionek()
        p2 = Pionek()
        self.pionki = []
        self.pionki.append(Pionek(0,0,0,0))
        self.pionki.append(Pionek(0,0,0,1))
        self.pionki.append(Pionek(0,0,1,1))
        self.pionki.append(Pionek(0, 1,1,1))
        self.pionki.append(Pionek(0, 1, 0, 1))
        self.pionki.append(Pionek(0, 1,1,0))
        self.pionki.append(Pionek(0, 0, 1, 0))
        self.pionki.append(Pionek(0, 1, 0, 0))
        self.pionki.append(Pionek(1, 0, 0, 0))
        self.pionki.append(Pionek(1, 0, 0, 1))
        self.pionki.append(Pionek(1, 0, 1, 1))
        self.pionki.append(Pionek(1, 1, 1, 1))
        self.pionki.append(Pionek(1, 1, 0, 1))
        self.pionki.append(Pionek(1, 1, 1, 0))
        self.pionki.append(Pionek(1, 0, 1, 0))
        self.pionki.append(Pionek(1, 1, 0, 0))

    def __str__(self):
        pionki = ''
        for pion in self.pionki:
            pionki += str(pion) + '\n'
        return pionki



