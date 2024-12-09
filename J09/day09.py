
with open('input.txt', 'r') as fichier:
    lignes = fichier.readlines()
    datas = [int(v) for v in lignes[0]]

to_compact = []
ids = 0
n = len(datas)
for i in range(n):
    if i%2 == 1:
        to_compact += ["."]*datas[i]
    else:
        to_compact += [ids]*datas[i]
        ids += 1

N = len(to_compact)

def decaler(j):
    while j>= 0 and to_compact[j] == ".":
        j-=1
    return j

#Challenge 1
compacted = []
j = decaler(N - 1)
for i in range(N):
    if j<i:
            break
    elif to_compact[i] != ".":
        compacted += [to_compact[i]]
    else:
        j = decaler(j)
        if j<i:
            break
        compacted += [to_compact[j]]
        j-= 1
print("Challenge 1:",sum([compacted[i]*i for i in range(len(compacted))]))

#Challenge 2
def has_free_space(j,nFile):
    i = 0
    while i <j and i < N-nFile:
        if to_compact[i:i+nFile] == ["."]*nFile:
            return i
        i += 1
    return -1

def decaler2(j,idFile):
    while j>= 0 and to_compact[j] != idFile:
        j-=1
    return j

#Challenge 2
j = decaler(N-1)
idFile = to_compact[j]
while j >= 0:
    print(j)
    nFile = 1
    i = j-1
    while i>=0 and to_compact[i] == idFile:
        nFile += 1
        i -=1
    iNext = has_free_space(j,nFile)
    if iNext == -1:
        j -= nFile
    else:
        for k in range(nFile):
            to_compact[iNext+k] = idFile
            to_compact[j-k] = "."
    idFile -=1
    j = decaler2(j,idFile)
print("Challenge 2:",sum([to_compact[i]*i for i in range(len(to_compact)) if to_compact[i] != "."]))

