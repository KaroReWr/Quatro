p1 = [0,1,3,4,5,6]
p2 = [1,2,3,4,5]
p3 = [0,1,3,6,5]
p4 = [1,3,5,7,8]

pionki = [p2,p3,p4]

wspolne_cechy = []
for cecha in p1:
    wspolnaDlaWszystkich = True
    for pion in pionki:
        cechaJestWPionku = False
        for cecha_innego_pionka in pion:
            if cecha == cecha_innego_pionka:
                cechaJestWPionku = True
                break
        if cechaJestWPionku is False:
            wspolnaDlaWszystkich = False
            break
    if wspolnaDlaWszystkich == True:
        wspolne_cechy.append(cecha)

print("wspolne dla wszystkich pionków",wspolne_cechy)