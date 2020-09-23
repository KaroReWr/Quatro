from Pionek import Pionek

class Board:
    def __init__(self):
        self.pionki = []


    def getParameters(self):
        prm = []
        for pion in range(0, 16):
            liczba = '{0:04b}'.format(pion)
            prm.append(list(liczba))
        return prm

    def getStringWithParameters(self):
        strng = ''
        for paramteres_in_list in self.getParameters():
            for p in paramteres_in_list:
                strng += p
        return strng





    def __str__(self):
        pionki = ''
        for pion in self.pionki:
            pionki += str(pion) + '\n'
        return pionki

a = Board()
print(a.getStringWithParameters())


