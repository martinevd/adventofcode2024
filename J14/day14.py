import re
import numpy as np
import matplotlib.pyplot as plt
import copy

datas = []
with open('input.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for ligne in lignes:
        datas.append([int(v) for v in re.findall(r'-?\d+', ligne)])

def move(x,y,dx,dy,width,length,k):
    return (x + k * dx ) % width, (y + k*dy) % length

def quadrant(x,y,width,length):
    if 0 <= x < width//2:
        if 0 <= y < length//2:
            return 1
        elif length//2 < y < length:
            return 3
    elif width//2 < x < width:
        if 0 <= y < length//2:
            return 2
        elif length//2 < y < length:
            return 4
    return 0

def challenge1(datas,width,length,k):
    quadrants=[0,0,0,0]
    for x,y,dx,dy in datas:
        x_,y_ = move(x,y,dx,dy,width,length,k)
        q = quadrant(x_,y_,width,length)
        if q :
            quadrants[q-1] += 1
    return quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]


#print("Challenge 1:",challenge1(datas,101,103,100))


def draw_matrix(matrix,width,length):
    fig, ax = plt.subplots()
    for i, ligne in enumerate(matrix):
        for j, val in enumerate(ligne):
            if val == 1:
                ax.add_patch(plt.Circle((j, -i), 0.4, color="blue"))
    ax.set_aspect('equal')
    plt.xlim(-1, width)
    plt.ylim(-length, 1)
    plt.gca().invert_yaxis()
    plt.show()


def has_a_cluster(matrix, width, length, seuil, dx, dy):

    sum_matrix = [[0] * width for _ in range(length)]

    # Somme cumulative
    for y in range(length):
        for x in range(width):
            sum_matrix[y][x] = matrix[y][x]
            if 0 <= y - 1 :
                sum_matrix[y][x] += sum_matrix[y-1][x]
            if 0 <= x - 1 :
                sum_matrix[y][x] += sum_matrix[y][x-1]
            if 0 <= x - 1 and 0 <= y - 1 :
                sum_matrix[y][x] -= sum_matrix[y-1][x-1]

    #Calcul par sous-région d'aire dx*dy
    for y in range(length-dy):
        for x in range(width-dx):
            total = sum_matrix[y+dy][x+dx]
            if 0 <= x-1:
                total -= sum_matrix[y+dy][x-1]
            if 0 <= y-1:
                total -= sum_matrix[y-1][x+dx]
            if 0 <= x-1 and 0<= y-1:
                total += sum_matrix[y-1][x-1]

            #Verification
            if total/(dx*dy) > seuil:
                return True
    return False


def challenge2(datas,width,length,klim):
    datas_init = copy.deepcopy(datas)
    n = len(datas)
    for k in range(1,klim):
        matrix = np.zeros((length,width),dtype = int)
        for i in range(n):
            r = datas[i]
            r[0],r[1] = move(r[0],r[1],r[2],r[3],width,length,1)
            matrix[r[1]][r[0]] = 1
        if has_a_cluster(matrix,width,length,0.40,20,20):
            print(k)
            draw_matrix(matrix,width,length)

challenge2(datas,101,103,10000)


