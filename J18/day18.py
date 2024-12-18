import heapq

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

n = len(lines)
def datas(nSteps):
    corrupted = set()
    for i in range(nSteps):
        coo = lines[i].split(",")
        corrupted.add((int(coo[0]),int(coo[1])))
    return corrupted


def in_the_limits(x,y,dim):
        return 0 <= x < dim and 0 <= y < dim

def dijkstra(corrupted, dim):
    distances = {(x,y): float('inf') for y in range(dim) for x in range(dim) if (x,y) not in corrupted}
    #previous_nodes = {node: [] for node in graph}
    distances[(0,0)] = 0
    priority_queue = [(0,0,0)]

    while priority_queue:
        current_distance, x,y = heapq.heappop(priority_queue)

        if (x,y) == (dim-1,dim-1):
            break

        # Ignorer si une meilleure distance est déjà trouvée
        if current_distance > distances[(x,y)]:
            continue

        voisins = [(-1,0),(0,-1),(0,1),(1,0)]
        # Explorer les voisins
        for vx,vy in voisins:
            voisinx,voisiny = (x+vx,y+vy)
            if not(in_the_limits(voisinx,voisiny,dim) and (voisinx,voisiny) not in corrupted):
                continue

            distance = current_distance + 1
            neighbor = (voisinx,voisiny)

            # Si une meilleure distance est trouvée
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                #previous_nodes[neighbor] = [(x,y)]
                heapq.heappush(priority_queue, (distance, voisinx,voisiny))
    return distances[(dim-1,dim-1)]

print("Challenge 1:", dijkstra(datas(1024),71))


def challenge2(dim):
    beg,end = 0,n
    while beg <= end:
        mid = (beg+end)//2
        if dijkstra(datas(mid +1),dim) != float("inf") :
            beg = mid + 1
        else:
            end = mid - 1
    return lines[beg]

print("Challenge 2:", challenge2(71))

