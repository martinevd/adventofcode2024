import heapq

with open('input.txt', 'r') as file:
    datas = file.read().splitlines()
    graph = {}
    n,m = len(datas),len(datas[0])

    def in_the_limits(x,y):
        return 0 <= x < m and 0 <= y < n

    lifo = []
    def add_node(x,y,dirx,diry):

        #Deja dans le graph
        if (x,y,dirx,diry) in graph:
            return

        #Recherche des voisins et connection au sommet actuel
        voisins = [(-1,0),(0,-1),(1,0),(0,1)]
        connections = []
        for vx,vy in voisins:
            voisinx,voisiny = x + vx, y + vy
            if in_the_limits(voisinx,voisiny) and datas[voisiny][voisinx] != "#":
                if (vx,vy) == (dirx,diry):
                    connections.append((voisinx,voisiny,vx,vy,1))
                elif (vx,vy) == (-dirx,-diry):
                    connections.append((voisinx,voisiny,vx,vy,2001))
                else:
                    connections.append((voisinx,voisiny,vx,vy,1001))
                lifo.append((voisinx,voisiny,vx,vy))
        graph[(x,y,dirx,diry)] = connections

    #Initialisation du graphe et recherche de l'entrée et de la sortie
    for y in range(n):
        for x in range(m):
            if datas[y][x] == "S":
                xstart,ystart = x,y
                lifo.append((x,y,1,0))
            if datas[y][x] == "E":
                xend,yend = x,y

    #Création du graph
    while lifo != []:
        x,y,dirx,diry = lifo.pop()
        add_node(x,y,dirx,diry)


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: [] for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Ignorer si une meilleure distance est déjà trouvée
        if current_distance > distances[current_node]:
            continue

        # Explorer les voisins
        for voisinx,voisiny,vx,vy,weight in graph[current_node]:
            neighbor = (voisinx,voisiny,vx,vy)
            distance = current_distance + weight

            # Si une meilleure distance est trouvée
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = [current_node]
                heapq.heappush(priority_queue, (distance, neighbor))
            # Si un autre chemin potentielle est trouvé
            elif distance == distances[neighbor]:
                previous_nodes[neighbor] += [current_node]
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances, previous_nodes

def arg_min_list(distances,x,y):
    ends = [(xend,yend) + (dx,dy) for (dx,dy) in [(0,1),(1,0),(-1,0),(0,-1)] if (xend,yend) + (dx,dy) in distances]
    m = distances[ends[0]]
    i = []
    for j in range(1,len(ends)):
        if distances[ends[j]] < m:
            m = distances[ends[j]]
            i = [ends[j]]
        elif distances[ends[j]] == m:
            i.append(ends[j])
    return i,m

distances, previous_nodes = dijkstra(graph,(xstart,ystart,1,0), (xend,yend))
ends,mini = arg_min_list(distances,xend,yend)

#Challenge 1
print("Challenge 1:",mini)


#Challenge 2

#Recherche des tiles de chaque chemin minimale
tiles_in_a_path = set()
tiles = ends.copy()
deja_vu = {}
while tiles:
    current = tiles.pop()
    if current in deja_vu:
        continue
    deja_vu[current] = True
    tiles_in_a_path.add((current[0],current[1]))

    if previous_nodes[current]:
        tiles += previous_nodes[current]

#Comptage du nombre de tiles
count = 0
for _ in tiles_in_a_path:
    count += 1

def draw(datas,n,m,tiles_in_a_path):
    for y in range(n):
        l = ""
        for x in range(m):
            if (x,y) in tiles_in_a_path:
                l += "O"
            else:
                l += datas[y][x]
        print(l)

print("Challenge 2:", count)
draw(datas,n,m,tiles_in_a_path)


