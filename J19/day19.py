with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    paterns = lines[0].split(", ")
    designs = [d for d in lines[2:]]

def count_combinaisons(design):
    n = len(design)
    nb_suffixe = [0]*(n+1)
    nb_suffixe[n] = 1
    for i in range(n-1,-1,-1):
        for patern in paterns :
            if design[i:i+len(patern)] == patern:
                nb_suffixe[i] += nb_suffixe[i+len(patern)]
    return nb_suffixe[0]

print("Challenge 1 :", sum([count_combinaisons(design) > 0 for design in designs]))
print("Challenge 2 :", sum([count_combinaisons(design) for design in designs]))