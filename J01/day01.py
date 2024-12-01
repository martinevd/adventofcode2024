# Créé par Martin, le 01/12/2024 en Python 3.7


tab1 = []
tab2 = []

with open('input1.txt', 'r') as fichier:
    for ligne in fichier:
        valeurs = ligne.strip().split()
        tab1.append(int(valeurs[0]))
        tab2.append(int(valeurs[1]))

n = len(tab1)

#Challenge1

tab1.sort()
tab2.sort()

dist = 0

for i in range (0,n):
    dist += abs(tab1[i] - tab2[i])

print(dist)

#Challenge2

j = 0
sim = 0

for i in range (0,n):
    count = 0
    while (j < n) and (tab1[i] > tab2[j]) :
        j+=1
    while (j < n) and (tab1[i] == tab2[j]):
        count+=1
        j+=1
    sim += tab1[i] * count

print(sim)