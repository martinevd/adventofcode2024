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
                    x,y=i*2,j
                if c == "O":
                    l += ["[","]"]
                else:
                    l += [c]*2
            area.append(l)
        else:
            for c in line:
                movments.append(c)

    n,m = len(area),len(area[0])

def move_box(x,y,dirx,diry):
    area[y][x] = "."
    area[y][x+1] = "."
    area[y+diry][x+dirx] = "["
    area[y+diry][x+dirx+1] = "]"

def move_box_in_line(x,y,dirx,diry):
    global area

    #Se placer sur le début de la boite
    x1,x2 = x,x+1
    if area[y][x] == "]":
        x1,x2 = x-1,x

    if diry != 0 :
        #Il y a au moins un mur
        if area[y+diry][x1+dirx] == "#" or area[y+diry][x2+dirx] == "#":
            return False

        #Il n'y a pas de murs
        elif area[y+diry][x1+dirx] == "." and area[y+diry][x2+dirx] == "." :
            move_box(x1,y,dirx,diry)
            return True

        #Il y a une boite pile au dessus (ou en dessous)
        elif area[y+diry][x1+dirx] == "[" and area[y+diry][x2+dirx] == "]" and move_box_in_line(x1+dirx,y+diry,dirx,diry):
            move_box(x1,y,dirx,diry)
            return True

        #Il y a une boite pile au dessus (ou en dessous) à gauche
        elif area[y+diry][x1+dirx] == "]" and area[y+diry][x2+dirx] == "." and move_box_in_line(x1+dirx,y+diry,dirx,diry):
            move_box(x1,y,dirx,diry)
            return True

        #Il y a une boite pile au dessus (ou en dessous) à droite
        elif area[y+diry][x1+dirx] == "." and area[y+diry][x2+dirx] == "[" and move_box_in_line(x2+dirx,y+diry,dirx,diry):
            move_box(x1,y,dirx,diry)
            return True

        #Il y a deux boites
        elif area[y+diry][x1+dirx] == "]" and area[y+diry][x2+dirx] == "[":
            area_save = [[c for c in line] for line in area]
            if move_box_in_line(x1+dirx,y+diry,dirx,diry) and move_box_in_line(x2+dirx,y+diry,dirx,diry):
                move_box(x1,y,dirx,diry)
                return True
            area = area_save
            return False
    elif dirx == 1:
        #Il y a un mur à droite
        if area[y+diry][x2+dirx] == "#":
            return False

        #Il n'y a pas de mur à droite
        elif area[y+diry][x2+dirx] == ".":
            move_box(x1,y,dirx,diry)
            return True

        #Il y a une boite à droite
        elif move_box_in_line(x2+dirx,y+diry,dirx,diry):
            move_box(x1,y,dirx,diry)
            return True
    elif dirx == -1 :
        #Il y a un mur à gauche
        if area[y+diry][x1+dirx] == "#":
            return False

        #Il n'y a pas de mur à gauche
        elif area[y+diry][x1+dirx] == ".":
            move_box(x1,y,dirx,diry)
            return True

        #Il y a une boite à gauche
        elif move_box_in_line(x1+dirx,y+diry,dirx,diry):
            move_box(x1,y,dirx,diry)
            return True
    return False

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

for symb in movments:
    dirx,diry = directions[symb]
    newx,newy = x + dirx, y + diry
    if area[newy][newx] == ".":
        x,y = newx,newy
    elif area[newy][newx] == "[" or area[newy][newx] == "]":
        move_box_in_line(newx,newy,dirx,diry)
        if area[newy][newx] == ".":
            x,y = newx,newy

count = 0
for j in range(n):
    for i in range(m):
        if area[j][i] == "[":
            count += 100*j +i

print("Challenge 2:",count)


