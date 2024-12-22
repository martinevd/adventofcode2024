with open('input.txt', 'r') as file:
    secret_numbs = [int(v) for v in file.read().splitlines()]

N = len(secret_numbs)

def new_secred_number(secret_numb):
    #Step1
    secret_numb= ((secret_numb*64)^secret_numb)%16777216
    #Step2
    secret_numb= ((secret_numb//32)^secret_numb)%16777216
    #Step3
    return ((secret_numb*2048)^secret_numb)%16777216


def challenge1():
    count = 0
    for n in secret_numbs:
        for i in range(2000):
            n = new_secred_number(n)
        count += n
print("Challenge1:",challenge1())

def challenge2():
    save = [[0 for j in range(2000)] for i in range(N)]
    deja_vu = [set() for i in range(N)]
    bananas = dict()
    for i,n in enumerate(secret_numbs):
        for j in range(2000):
            n = new_secred_number(n)
            save[i][j] = n % 10
            if j>=4:
                seq = (save[i][j-3] - save[i][j-4],
                       save[i][j-2] - save[i][j-3],
                       save[i][j-1] - save[i][j-2],
                       save[i][j] - save[i][j-1]
                       )
                if seq not in deja_vu[i]:
                    if seq not in bananas:
                        bananas[seq] = 0
                    bananas[seq] += save[i][j]
                deja_vu[i].add(seq)

    max_bananas = 0
    for n_bananas in bananas.values():
        max_bananas = max(n_bananas,max_bananas)

    return max_bananas
print("Challenge2:",challenge2())