import re

AButtons,BButtons,Prizes = [],[],[]
with open('input.txt', 'r') as fichier:
    lignes = fichier.readlines()
    for i in range(0,len(lignes),4):
        AButtons.append([int(v) for v in re.findall(r'\d+', lignes[i])])
        BButtons.append([int(v) for v in re.findall(r'\d+', lignes[i+1])])
        Prizes.append([int(v) for v in re.findall(r'\d+', lignes[i+2])])
    n = len(Prizes)


def min_tokens(prize,buttonA,buttonB):
    xA,yA = buttonA[0],buttonA[1]
    xB,yB = buttonB[0],buttonB[1]
    xP,yP = prize[0],prize[1]

    det = yA*xB-xA*yB
    if det == 0:
        return 0

    a,b= (yP*xB - xP*yB)/det, (xP*yA-xA*yP)/det

    return 3*int(a)+int(b) if (int(a) == a and int(b) == b) else 0

def challenge(AButtons,BButtons,Prizes):
    return sum([min_tokens(Prizes[i],AButtons[i],BButtons[i]) for i in range(n)])

print("Challenge1 :",challenge(AButtons,BButtons,Prizes))

newPrizes = [[10000000000000+prizeX,10000000000000+prizeY] for [prizeX,prizeY] in Prizes]
print("Challenge2 :",challenge(AButtons,BButtons,newPrizes))