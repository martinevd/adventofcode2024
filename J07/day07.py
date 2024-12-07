
datas = []

with open('input.txt', 'r') as fichier:
    for ligne in fichier:
        res,nombres_non_form = ligne.split(": ")
        nombres =  [int(n) for n in nombres_non_form.split(" ")]
        datas.append((int(res),nombres))


#Challenge1
count1 =0
for res,nombres in datas :
    n_op = len(nombres) - 1
    for i in range(2**n_op):
        b_i = bin(i)[2:]
        b = "0"*(n_op-len(b_i)) + b_i

        res_ops = nombres[0]
        k = 1
        for j in b :
            if j == "0" :
                res_ops = res_ops + nombres[k]
            else:
                res_ops = res_ops * nombres[k]
            k += 1

        if res_ops == res :
            count1 += res
            break
print("Challenge1:", count1)

#Challenge2

def next_(nombre):
    nombre_fin = str((int(nombre[0]) + 1)%3)
    r = (int(nombre[0]) + 1)//3
    n= len(nombre)

    k = 1
    while r and k < n:
        nombre_fin = nombre_fin +  str((int(nombre[k]) + 1)%3)
        r = (int(nombre[k]) + 1)//3
        k+=1
    return nombre_fin + nombre[len(nombre_fin):]

count2 =0
for res,nombres in datas :
    n_op = len(nombres) - 1
    code = "0" * n_op
    for i in range(3**n_op):

        res_ops = nombres[0]
        k = 1
        for j in code :
            if j == "0" :
                res_ops = res_ops + nombres[k]
            elif j == "1":
                res_ops = int(str(res_ops) + str(nombres[k]))
            else:
                res_ops = res_ops * nombres[k]

            if res_ops > res:
                break
            k += 1

        if res_ops == res :
            count2 += res
            break

        code = next_(code)

print("Challenge2:", count2)
