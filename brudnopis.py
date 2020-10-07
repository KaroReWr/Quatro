a = [0,0,0]
b = [1,1,1]
pionki = []
licznik = 0

for i in range(0,3):
    pionki.append(a.copy())
    pionki[licznik][i] = 1
    licznik += 1


zbiory = []

for pion in range(0,16):
    liczba = '{0:04b}'.format(pion)
    #print(liczba)








def sthg():
    zbior = []
    for pion in range(0, 16):
        liczba = '{0:04b}'.format(pion)
        color = int(list(liczba)[0])
        size = int(list(liczba)[1])
        shape = int(list(liczba)[2])
        is_hole = int(list(liczba)[3])
        pionek = color,size,shape, is_hole
        zbior.append(pionek)
    return zbior


z = []
je = []
d = []
t = []

pj = [[0, 1, 2], [0, 1, 3], [0, 1], [0, 2, 3], [0, 2], [0, 3], [0], [1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], [], [0, 1], [0, 1, 3], [0, 2], [0, 2, 3], [0], [0, 3], [1, 2]]

for i in pj:
    for j in i:
        if j == 0:
            z.append(pj.index(i))
        if j == 1:
            je.append(pj.index(i))
        if j == 2:
            d.append(pj.index(i))
        if j == 3:
            t.append(pj.index(i))

print(z, je)
