with open('input.txt', 'r') as fichier:
    ligne = fichier.readline()
    datas = [int(v) for v in ligne.split(" ")]

def regle1(p):
    return p == 0

def regle2(p):
    return len(str(p))%2 == 0

#Challenge1
def challenge1(n,datas): #Methode naive
    for i in range(n):
        datas_ = []
        for p in datas:
            if regle1(p):
                datas_.append(1)
            elif regle2(p):
                str_p = str(p)
                nP = len(str_p)
                datas_.append(int(str_p[:nP//2]))
                datas_.append(int(str_p[nP//2:]))
            else:
                datas_.append(p*2024)
        datas = datas_.copy()
    return len(datas)
print("Challenge 1:", challenge1(25,datas))


#Challenge2
deja_vu = {} #Programmation dynamique

def update_dict(n,p):
    if (p,n) in deja_vu:
        return deja_vu[(p,n)]
    res_p = cligner(n,p)
    deja_vu[(p,n)] = res_p
    return res_p

def cligner(n,p):
    if n == 0:
        return 1
    if (p,n) in deja_vu: #Pas besoin de tout recalculer !
        return deja_vu[(p,n)]
    if regle1(p):
        return update_dict(n-1,1)
    if regle2(p):
        str_p = str(p)
        nP = len(str_p)

        p1,p2 = int(str_p[:nP//2]), int(str_p[nP//2:])
        return update_dict(n-1,p1) + update_dict(n-1,p2)
    return update_dict(n-1,p*2024)

def challenge2(n,datas): #Methode dynamique
    count = 0
    for p in datas:
        count += cligner(n,p)
    return count

print("Challenge 2:", challenge2(75,datas))