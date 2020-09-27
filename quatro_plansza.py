from Pionek import Pionek
import copy

class Board:
    def __init__(self):
        self.pionki = []

    def sthg(self):
        for pion in range(0, 16):
            liczba = '{0:04b}'.format(pion)
            liczba_l = list(liczba)
            liczba_l.copy()
            color = int(liczba_l[0])
            size = int(liczba_l[1])
            shape = int(liczba_l[2])
            is_hole = int(liczba_l[3])
            pionek = Pionek(color,size,shape, is_hole)
            self.pionki.append(pionek)
        return self.pionki



    def __str__(self):
        pionki = ''
        for pion in self.pionki:
            pionki += str(pion) + '\n'
        return pionki

a = Board()
print(a.sthg())



