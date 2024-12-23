import networkx as nx

with open("input.txt", 'r') as file:
    datas = [line.split("-") for line in file.read().splitlines()]

def challenge1():
    liste_adj = {}
    for c1,c2 in datas:
        if c1 not in liste_adj:
            liste_adj[c1] = []
        if c2 not in liste_adj:
            liste_adj[c2] = []
        liste_adj[c1].append(c2)
        liste_adj[c2].append(c1)


    def intersect(l1,l2):
        return [e for e in l1 if e in l2]


    all_tri_connections = set()
    for c1,voisins in liste_adj.items():
        for c2 in voisins:
            i = intersect(voisins,liste_adj[c2])
            for c3 in i:
                tri_connection = sorted([c1,c2,c3])
                all_tri_connections.add((tri_connection[0],tri_connection[1],tri_connection[2]))

    count = 0
    for c1,c2,c3 in all_tri_connections:
        if c1[0] == "t" or c2[0] == "t" or c3[0] == "t":
            count += 1
    return count

print("Challenge 1:",challenge1())


def challenge2():
    graph = nx.Graph()
    for c1,c2 in datas:
        graph.add_edge(c1,c2)

    cliques = list(nx.find_cliques(graph))
    max_clique = sorted(max(cliques, key=len))

    res = ""
    for c in max_clique:
        res+= c + ","
    return res[:-1]

print("Challenge 2:",challenge2())



