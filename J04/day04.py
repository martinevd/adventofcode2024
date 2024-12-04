datas = []

with open('input.txt', 'r') as fichier:
    for ligne in fichier:
        ligne_tab = [c for c in ligne if c != '\n']
        datas.append(ligne_tab)


n = len(datas)
m = len(datas[0])
count = 0

#Challenge 1
def searchFromPos(matrix,x,y,dirx,diry):
    word = "MAS"
    while word != "":
        if not(0 <= x + dirx < m and 0<= y + diry < n):
            return False
        if matrix[y + diry][x + dirx] == word[0]:
            word = word[1::]
            x += dirx
            y += diry
        else:
            return False
    return True

for y in range(n):
    for x in range(m):
        if (datas[y][x] == 'X'):
            for i in range (-1,2):
                for j in range (-1,2):
                    if (i,j) != (0,0) and searchFromPos(datas,x,y,i,j):
                        count += 1
print("Challenge 1 :", count)

#Challenge 2
count2 = 0
def searchFromPos2(matrix,x,y):
    return 0 < x < m - 1 and 0 < y < n-1 and (matrix[y -1][x - 1], matrix[y + 1][x + 1]) in [("M","S"),("S","M")] and (matrix[y + 1][x - 1], matrix[y - 1][x + 1]) in [("M","S"),("S","M")]

for y in range(n):
    for x in range(m):
        if (datas[y][x] == 'A') and searchFromPos2(datas,x,y):
            count2 +=1

print("Challenge 2 :", count2)





