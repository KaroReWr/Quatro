from Pionek import Pionek
import copy

class Board:
    def __init__(self):
        self.pionki = []
        self.init_pionki()

    def init_pionki(self):
        for pion in range(0, 16):
            liczba = '{0:04b}'.format(pion)
            liczba_l = list(liczba)
            color = int(liczba_l[0])
            size = int(liczba_l[1])
            shape = int(liczba_l[2])
            is_hole = int(liczba_l[3])
            pionek = Pionek(color,size,shape, is_hole)
            self.pionki.append(pionek)
        return self.pionki



    def __str__(self):
        pionki_string_output = ''
        for pion in self.pionki:
            pionki_string_output += str(pion) + '\n'
        return pionki_string_output


    def plansza_to_string(self):
        for i in self.pionki:
            print(str(i.color) + str(i.size) + str(i.shape) + str(i.is_hole))


    def checkPionki(self, pionek1, pionek2):
        similarities = ''
        for i in range(0,4):
            if pionek1.color == pionek2.color:
                similarities += 'Color is the same - index: 0\n'
            if pionek1.size == pionek2.size:
                similarities += 'Size is the same - index: 1\n'
            if pionek1.shape == pionek2.shape:
                similarities += 'Shape is the same - index: 2\n'
            if pionek1.is_hole == pionek2.is_hole:
                similarities += 'Is_hole is the same - index: 3'
            return similarities if len(similarities) > 0 else "nothing in common"

b = Pionek(0,1,1,1)
c = Pionek(1,0,0,0)
a = Board()
print(a.checkPionki(c,b))


