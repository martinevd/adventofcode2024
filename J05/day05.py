import numpy as np


l = 100

matrix = np.zeros((l,l),dtype=int)

rules = []
with open('input.txt', 'r') as fichier:
    isrule = True
    for ligne in fichier:
        if isrule and ligne == "\n":
            isrule = False
        elif isrule:
            i1,i2 = ligne.split("|")
            matrix[int(i1)][int(i2)] = 1
        else:
            rules.append([int(i) for i in ligne.split(",")])


def is_correct(rule):
    n = len(rule)
    for i in range(n):
        for j in range(i):
            if matrix[rule[i]][rule[j]]:
                return False
        for j in range(i+1,n):
            if matrix[rule[j]][rule[i]]:
                return False
    return True

#Challenge1
count1 = 0
for rule in rules:
    if is_correct(rule):
        count1 += rule[len(rule)//2]
print(count1)

#Challenge2
def tri(rule):
    n = len(rule)
    for i in range(n):
        for j in range(0, n - i - 1):
            if matrix[rule[j + 1]][rule[j]]:
                rule[j], rule[j + 1] = rule[j + 1], rule[j]
    return rule

count2 = 0
for rule in rules:
    if not is_correct(rule):
        rule = tri(rule)
        count2 += rule[len(rule)//2]
print(count2)

