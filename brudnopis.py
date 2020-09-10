a = [0,0,0]
b = [1,1,1]
pionki = []
licznik = 0

for i in range(0,3):
    pionki.append(a)
    pionki[licznik][i] = 1
    licznik += 1

print(pionki)



