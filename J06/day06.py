import numpy as np

with open('input.txt', 'r') as fichier:
    lignes = fichier.readlines()
    n = len(lignes)
    m = len(lignes[0]) - 1

    matrix = np.zeros((n,m),dtype=int)
    for j in range(n):
        for i in range(m):
            if lignes[j][i] == "#":
                matrix[j][i] = 1
            elif lignes[j][i] == "^":
                x,y = i,j

def tourner(dirx,diry):
    return -diry, dirx

dirx,diry = 0,-1

#Challenge1
def visit(x,y,dirx,diry):
    visited = set()
    is_inside = True
    while is_inside:
        newx,newy = x+dirx,y+diry
        if not(0 <= newx < m and 0 <= newy < n):
            visited.add((x,y))
            is_inside = False
        elif matrix[newy][newx]:
            dirx,diry = tourner(dirx,diry)
        else:
            visited.add((x,y))
            x = newx
            y = newy

    return visited

print("Challenge 1:",len(visit(x,y,dirx,diry)))

#Challenge 2 (long a l'exec)
def is_a_loop(x,y,dirx,diry):
    save_positions=[]
    while True:
        newx,newy = x+dirx,y+diry
        if (x,y,dirx,diry) in save_positions:
            return 1
        elif not(0 <= newx < m and 0 <= newy < n):
            return 0
        elif matrix[newy][newx]:
            dirx,diry = tourner(dirx,diry)
        else:
            save_positions.append((x,y,dirx,diry))
            x = newx
            y = newy

count2 = 0
visited = visit(x,y,dirx,diry)
for (xobs,yobs) in visited:
    matrix[yobs][xobs] = 1
    count2 += is_a_loop(x,y,dirx,diry)
    matrix[yobs][xobs] = 0

print("Challenge 2:",count2)





