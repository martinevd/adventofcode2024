with open("input.txt", 'r') as file:
    datas = file.read().splitlines()


n = len(datas)
wires_status = {}

i = 0
while datas[i] != "":
    wire,value = datas[i].split(": ")
    wires_status[wire] = int(value)
    i+=1

i+=1

gates_waiting = []
z_wires = []

def apply_gate(w1,w2,logic,woutput):
    if w1 in wires_status and w2 in wires_status:
        if logic == "AND":
            wires_status[woutput] = wires_status[w1] & wires_status[w2]
        elif logic == "OR":
            wires_status[woutput] = wires_status[w1] | wires_status[w2]
        elif logic == "XOR":
            wires_status[woutput] = wires_status[w1] ^ wires_status[w2]

        if woutput[0] == "z":
            z_wires.append(woutput)
    else:
        gates_waiting.append((w1,logic,w2,woutput))

while i < n:
    w1,logic,w2,_,woutput = datas[i].split(" ")
    apply_gate(w1,w2,logic,woutput)
    i += 1

while gates_waiting:
    w1,logic,w2,woutput = gates_waiting.pop(0)
    apply_gate(w1,w2,logic,woutput)


z_wires.sort(reverse=True)
res = ""
for wz in z_wires:
    res += str(wires_status[wz])


print("Challenge1 :",int(res,2))
