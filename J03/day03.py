datas =""

with open('input.txt', 'r') as fichier:
    while True:
        c = fichier.read(1)
        if not c :
            break
        datas += c


n = len(datas)

#Challenge1
res1 = 0
i = 0
while i < n - 4 :
    if datas[i:(i+4)] == "mul(":

        i += 3
        n1 = ""
        n2 = ""

        i+= 1
        while i < n and datas[i].isdigit():
            n1 += datas[i]
            i += 1

        if i >= n : break

        if n1 == "" or datas[i] != ',':
            continue

        i+= 1
        while i < n and datas[i].isdigit():
            n2 += datas[i]
            i += 1

        if n2 == "" or datas[i] != ')':
            continue

        res1 += int(n1)*int(n2)
    i+=1
print("Challenge 1:",res1)


#Challenge2
res2 = 0
i = 0
do = True
while i < n - 4 :
    if datas[i:(i+4)] == "do()":
        do = True
        i+=3
    elif i < n - 7 and datas[i:(i+7)] == "don't()":
        do = False
        i+=6
    elif do and datas[i:(i+4)] == "mul(":

        i += 3
        n1 = ""
        n2 = ""

        i+= 1
        while i < n and datas[i].isdigit():
            n1 += datas[i]
            i += 1

        if i >= n : break

        if n1 == "" or datas[i] != ',':
            continue

        i+= 1
        while i < n and datas[i].isdigit():
            n2 += datas[i]
            i += 1

        if n2 == "" or datas[i] != ')':
            continue

        res2 += int(n1)*int(n2)
    i+=1
print("Challenge 2:",res2)