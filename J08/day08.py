import numpy as np

pos_antennas = []
with open('input.txt', 'r') as fichier:
    datas = fichier.readlines()
    n = len(datas)
    m = len(datas[0]) - 1

    for j in range(n):
        for i in range(m):
            if datas[j][i] != ".":
                pos_antennas.append((i,j))


N = len(pos_antennas)

#Challenge1
antinodes = np.zeros((n,m),dtype=int)
for i in range(N):
    x1,y1 = pos_antennas[i]
    for j in range(i):
        x2,y2 = pos_antennas[j]
        if datas[y1][x1] == datas[y2][x2]:
            dx,dy = x2-x1,y2-y1
            if 0 <= x1-dx < m and 0 <= y1-dy < n:
                antinodes[y1-dy][x1-dx] = 1
            if 0 <= x2+dx < m and 0 <= y2+dy < n:
                antinodes[y2+dy][x2+dx] = 1

print("Challenge1 :",np.sum(antinodes))

#Challenge2
antinodes = np.zeros((n,m),dtype=int)
for i in range(N):
    x1,y1 = pos_antennas[i]
    antinodes[y1][x1] = 1 #Antennas are also antinodes
    for j in range(i):
        x2,y2 = pos_antennas[j]
        if datas[y1][x1] == datas[y2][x2]:
            dx,dy = x2-x1,y2-y1
            x1_,y1_ = x1-dx,y1-dy
            while 0 <= x1_ < m and 0 <= y1_ < n:
                antinodes[y1_][x1_] = 1
                x1_ -= dx
                y1_ -= dy
            x2_,y2_ = x2+dx,y2+dy
            while 0 <= x2_ < m and 0 <= y2_ < n:
                antinodes[y2_][x2_] = 1
                x2_ += dx
                y2_ += dy

print("Challenge2 :",np.sum(antinodes))


