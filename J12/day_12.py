with open('input.txt', 'r') as fichier:
    lignes = fichier.readlines()
    datas = [[v for v in ligne if v != "\n"] for ligne in lignes]

n = len(datas)
m = len(datas[0])

def new_union_find():
    return {"regions" : [y*m+ x  for y in range(n) for x in range(m)], "hauteurs" : [0 for _ in range(n*m)], "perimetres" : [0 for _ in range(n*m)], "aires" : [1 for _ in range(n*m)]}

def trouver(uf,v):
    region = uf["regions"][v]
    if region == v:
        return v
    representant = trouver(uf,region)
    uf["regions"][v] = representant
    return representant

def unir(uf,v1,v2):
    region1 = trouver(uf,v1)
    region2 = trouver(uf,v2)
    if region1 != region2:
        h1,h2 = uf["hauteurs"][region1],uf["hauteurs"][region2]
        if h1 < h2:
            uf["regions"][region1] = region2
            uf["aires"][region2] += uf["aires"][region1]
            uf["perimetres"][region2] += uf["perimetres"][region1]
        else :
            if h1 == h2:
                uf["hauteurs"][region1] += 1
            uf["regions"][region2] = region1
            uf["aires"][region1] += uf["aires"][region2]
            uf["perimetres"][region1] += uf["perimetres"][region2]

def est_dans_la_zone(x,y):
    return 0<= x < m and 0 <= y < n

def cherche_voisins(x,y):
    voisins = []
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for (dirx,diry) in dirs:
        x_,y_ = x + dirx,y + diry
        if est_dans_la_zone(x_,y_) :
            voisins.append((x_,y_))
    return voisins

def challenge(uf):
    #Creation des regions
    for y in range(n):
        for x in range(m):
            v = y*m + x
            voisins = cherche_voisins(x,y)
            for vx,vy in voisins:
                if datas[vy][vx] == datas[y][x]:
                    v_ = vy*m + vx
                    unir(uf,v,v_)

    #Recherche des regions
    regions = set()
    for v in range(n*m):
        regions.add(trouver(uf,v))

    #Calcul du resultat
    cout = 0
    for r in regions:
        cout += uf["perimetres"][r] * uf["aires"][r]
    return cout

#Challenge 1
uf1 = new_union_find()

#Calcul des perimètres
for y in range(n):
    for x in range(m):
        v = y*m + x
        voisins = cherche_voisins(x,y)
        uf1["perimetres"][v] += (4-len(voisins))
        for vx,vy in voisins:
            if datas[vy][vx] != datas[y][x]:
                uf1["perimetres"][v] += 1

print("Challenge1:",challenge(uf1))

#Challenge 2
uf2 = new_union_find()

def est_un_cote_conc(x,y,x1,y1,x2,y2):
    c1 = not(est_dans_la_zone(x1,y1)) or datas[y1][x1] != datas[y][x]
    c2 = not(est_dans_la_zone(x2,y2)) or datas[y2][x2] != datas[y][x]
    return c1 and c2

def est_un_cote_conv(x,y,x1,y1,x2,y2,xf,yf):
    c1 = est_dans_la_zone(x1,y1) and datas[y1][x1] == datas[y][x]
    c2 = est_dans_la_zone(x2,y2) and datas[y2][x2] == datas[y][x]
    c3 = not(est_dans_la_zone(xf,yf)) or datas[yf][xf] != datas[y][x]
    return c1 and c2 and c3

#Calcul des nouveaux perimètres (qui sont des cotes maintenant)
for y in range(n):
    for x in range(m):
        v = y*m + x


        # Ligne | de gauche
        if est_un_cote_conc(x,y,x-1,y,x,y-1) or est_un_cote_conv(x,y,x-1,y-1,x,y-1,x-1,y) :
            uf2["perimetres"][v] += 1

        # Ligne - du bas
        if est_un_cote_conc(x,y,x-1,y,x,y+1) or est_un_cote_conv(x,y,x-1,y,x-1,y+1,x,y+1) :
            uf2["perimetres"][v] += 1

        # Ligne | de droite
        if est_un_cote_conc(x,y,x,y+1,x+1,y) or est_un_cote_conv(x,y,x,y+1,x+1,y+1,x+1,y) :
            uf2["perimetres"][v] += 1

        # Ligne - du haut
        if est_un_cote_conc(x,y,x,y-1,x+1,y) or est_un_cote_conv(x,y,x+1,y-1,x+1,y,x,y-1) :
            uf2["perimetres"][v] += 1


print("Challenge2:",challenge(uf2))






