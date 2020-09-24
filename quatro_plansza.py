from Pionek import Pionek

class Board:
    def __init__(self):
        self.pionki = []

        for pion in range(0, 16):
            liczba = '{0:04b}'.format(pion)
            color = int(list(liczba)[0])
            size = int(list(liczba)[1])
            shape = int(list(liczba)[2])
            is_hole = int(list(liczba)[3])
            pionek = Pionek(color,size,shape, is_hole)
            self.pionki.append(pionek)


    def __str__(self):
        pionki = ''
        for pion in self.pionki:
            pionki += str(pion) + '\n'
        return pionki

a = Board()
print(a)


