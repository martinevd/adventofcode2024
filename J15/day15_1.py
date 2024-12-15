movments = []
area = []
directions = {"^": (0, -1),"v": (0, 1),">": (1, 0),"<": (-1, 0)}
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

    for j,line in enumerate(lines):
        if line != "" and line[0] == "#" :
            l = []
            for i,c in enumerate(line):
                if c == "@":
                    c = "."
                    x,y=i,j
                l.append(c)
            area.append(l)
        else:
            for c in line:
                movments.append(c)

    n,m = len(area),len(area[0])

def move_box(x,y,dirx,diry):
    area[y][x] = "."
    area[y+diry][x+dirx] = "O"

def move_box_in_line(x,y,dirx,diry):
    if area[y+diry][x+dirx] == "#":
        return False
    elif not area[y+diry][x+dirx] or move_box_in_line(x+dirx,y+diry,dirx,diry):
        move_box(x,y,dirx,diry)
        return True
    return False

for symb in movments:
    dirx,diry = directions[symb]
    newx,newy = x + dirx, y + diry
    if not area[newy][newx]:
        x,y = newx,newy
    elif area[newy][newx] == "O":
        move_box_in_line(newx,newy,dirx,diry)
        if area[newy][newx] == ".":
            x,y = newx,newy


def draw_area():
    for j in range(n):
        c = ""
        for i in range(m):
            if (i,j) == (x,y):
                c += "@"
            else:
                c += area[j][i]
        print(c)
    print("")

count = 0
for j in range(n):
    for i in range(m):
        if area[j][i] == "O":
            count += 100*j + i

print("Challenge 1:",count)


