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
                similarities += f'Color is the same - index: 0 , value: {pionek1.color}\n'
            if pionek1.size == pionek2.size:
                similarities += f'Size is the same - index: 1, value: {pionek1.size}\n'
            if pionek1.shape == pionek2.shape:
                similarities += f'Shape is the same - index: 2, value: {pionek1.shape}\n'
            if pionek1.is_hole == pionek2.is_hole:
                similarities += f'Is_hole is the same - index: 3, value: {pionek1.is_hole}'
            return similarities if len(similarities) > 0 else "nothing in common"


    def checkPionki2(self,pionki):
        for p in range(0, len(pionki) - 1):
            start = p +1
            for r in range(start, len(pionki)):
                pionek_p = pionki[p]
                pionek_r = pionki[r]
                print(self.checkPionki(pionek_p,pionek_r))


b = Pionek(0,0,0,0)
c = Pionek(0,1,1,0)
d = Pionek(0,1,1,1)
e = Pionek(0,1,0,0)

proba = [b,c,d,e]
a = Board()

print(a.checkPionki2(proba))



