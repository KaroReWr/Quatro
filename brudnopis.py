a = [0,0,0]
b = [1,1,1]
pionki = []
licznik = 0

for i in range(0,3):
    pionki.append(a.copy())
    pionki[licznik][i] = 1
    licznik += 1


zbior = []

for pion in range(0,16):
    liczba = '{0:04b}'.format(pion)
    zbior.append(list(liczba))




