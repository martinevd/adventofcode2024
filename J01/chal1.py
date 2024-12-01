# Créé par Martin, le 01/12/2024 en Python 3.7


tab1 = [3,4,2,1,3,3]
tab2 = [4,3,5,3,9,3]

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

print("Distance:",dist)

#Challenge2

i = 0
j = 0
sim = 0

while i < n :
    count_i = 1
    count_j = 0
    while (i < n-1) and (tab1[i] == tab1[i+1]):
        count_i +=1
        i+=1
    while (j < n) and (tab1[i] > tab2[j]) :
        j+=1
    while (j < n) and (tab1[i] == tab2[j]):
        count_j+=1
        j+=1
    sim += tab1[i] * count_j * count_i
    i+=1

print("Similarité :",sim)