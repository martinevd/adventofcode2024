with open('input.txt', 'r') as file:
    datas = file.read().splitlines()

n = len(datas)
m = len(datas[0])

for c in range(n*m):
    x,y = c % m, c // m
    if datas[y][x] == "S":
        xstart,ystart = x,y
        break

def in_the_limits(x,y):
        return 0 <= x < m and 0 <= y < n

deja_vu = {(x,y): False for y in range(n) for x in range(m)}
path = [(xstart,ystart)]
deja_vu[(xstart,ystart)] = True

while datas[path[-1][1]][path[-1][0]] != "E":
    x,y = path[-1]
    neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    for nx,ny in neighbors:
        if in_the_limits(nx,ny) and datas[ny][nx] != "#" and not deja_vu[(nx,ny)]:
            path.append((nx,ny))
            deja_vu[(nx,ny)] = True
            break

def save_pico_sec(cheat_dist,threshold):
    N = len(path)
    count = 0
    for i in range(N):
        for j in range(i+ 1 + threshold,N):
            xi,yi = path[i]
            xj,yj = path[j]
            dx,dy = abs(xi-xj),abs(yi-yj)

            if dx + dy <= cheat_dist and j - i - dx - dy >= threshold:
                count += 1
    return count

print("Challenge 1:", save_pico_sec(2,100))
print("Challenge 2:", save_pico_sec(20,100))