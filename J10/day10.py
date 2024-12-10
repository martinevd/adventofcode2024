import numpy as np

with open('input.txt', 'r') as fichier:
    lignes = fichier.readlines()
    datas = [[int(v) for v in ligne if v != "\n"] for ligne in lignes ]

n = len(datas)
m = len(datas[0])


def next_nodes(x,y):
    res = []
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for dirx,diry in dirs:
        x_,y_ = x + dirx, y + diry
        if 0<= x_ < m and 0 <= y_ < n and datas[y][x] + 1 == datas[y_][x_]:
            res.append((x_,y_))
    return res

#Challenge1
def cherche_trailheads(x,y,xgoal,ygoal):
    if (xgoal,ygoal) == (x,y):
        return 1
    nodes = next_nodes(x,y)
    for (i,j) in nodes:
        if cherche_trailheads(i,j,xgoal,ygoal):
            return 1
    return 0


count1 = 0
loc0 = []
loc9 = []

for y in range(n):
    for x in range(m):
        if datas[y][x] == 0:
            loc0.append((x,y))
        if datas[y][x] == 9:
            loc9.append((x,y))

for xstart,ystart in loc0:
    for xgoal,ygoal in loc9:
            count1 += cherche_trailheads(xstart,ystart,xgoal,ygoal)
print("Challenge 1:", count1)


#Challenge 2
def cherche_trailheads_distinct(x,y):
    if datas[y][x] == 9:
        return 1
    nodes = next_nodes(x,y)
    return sum([cherche_trailheads_distinct(i,j) for (i,j) in nodes])


count2 = 0
for y in range(n):
    for x in range(m):
        if datas[y][x] == 0:
            count2 += cherche_trailheads_distinct(x,y)
print("Challenge 2:",count2)