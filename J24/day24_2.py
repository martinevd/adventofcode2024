"""
J'ai résolu le problème 2 manuellement en utilisant le code ci-dessous, qui
identifie automatiquement un interrupteur permuté. Étant donné qu'il y en a
quatre, il ne me reste plus qu'à déterminer manuellement le second interrupteur
permuté pour chacun des interrupteurs identifiés.
"""

with open("input.txt", 'r') as file:
    datas = file.read().splitlines()


n = len(datas)
wires_status = {}
i = 0
N = 0
while datas[i] != "":
    wire,value = datas[i].split(": ")
    wires_status[wire] = int(value)
    if wire[0] == "x":
        N += 1
    i+=1

i+=1

gates = dict()

while i < n:
    w1,logic,w2,_,woutput = datas[i].split(" ")
    gates[woutput] = (w1,logic,w2)
    i+=1

#Trouver les permutation de z
for i in range(2,N):
    z = "z" + "0"*(2-len(str(i))) + str(i)
    w1,logic,w2 = gates[z]
    if logic != "XOR":
        print(z)

permutated = []

for woutput,(w1,logic,w2) in gates.items():
    #Verifie xi XOR yi -> ai (ai != z00)
        # => ai XOR _ -> _ (OR) _ XOR ai -> _, ai AND _ -> _ (OR) _ AND ai -> _
    if (w1[0],w2[0]) in [("x","y"),("y","x")] and logic == "XOR" and woutput != "z00":
        is_permuted = 2
        for woutput_,(w1_,logic,w2_) in gates.items():
            if (w1_ == woutput or w2_ == woutput) and logic == "XOR":
                is_permuted -= 1
            elif (w1_ == woutput or w2_ == woutput) and logic == "AND":
                is_permuted -= 1
        if is_permuted != 0 :
            print(woutput)

