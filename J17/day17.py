import re

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    regA = [int(re.findall(r'-?\d+', lines[0])[0])]
    regB = [int(re.findall(r'-?\d+', lines[1])[0])]
    regC = [int(re.findall(r'-?\d+', lines[2])[0])]


    program = [int(v) for v in re.findall(r'-?\d+', lines[4])]

def adv(_,comb):
    global regA
    regA[0] >>= comb
    return ""

def bxl(lit,_):
    global regB
    regB[0] ^= lit
    return ""

def bst(_,comb):
    global regB
    regB[0] = comb & 7
    return ""

def bxc(_,comb):
    global regB
    regB[0]  ^= regC[0]
    return ""

def out(_,comb):
    return str(comb & 7) + ","

def bdv(_,comb):
    global regA,regB
    regB[0] = regA[0] >> comb
    return ""

def cdv(_,comb):
    global regA,regC
    regC[0] = regA[0] >> comb
    return ""

n = len(program)

inst_sign = {0:adv,1:bxl,2:bst,4:bxc,5:out,6:bdv,7:cdv}
comb_sign = {0:[0],1:[1],2:[2],3:[3],4:regA,5:regB,6:regC}

def challenge1():
    i = 0
    output = ""

    while i < n :
        inst = program[i]

        lit = program[i+1]
        #Definition du combo
        comb = comb_sign[lit][0]

        if inst != 3:
            output += inst_sign[inst](lit,comb)
            i += 2
        else:
            if regA[0] == 0:
                i += 2
            else:
                i = lit
    return output[:-1]

print("Challenge 1:",challenge1())

def code_number(currentA,numb):
    global regA

    poss = []
    for d in range(8):
        regA[0] = currentA<< 3 | d
        regB[0],regC[0] = 0,0
        i = 0
        output = ""
        while i < n and len(output) == 0:
            inst = program[i]
            lit = program[i+1]
            comb = comb_sign[lit][0]
            if inst != 3:
                output = inst_sign[inst](lit,comb)
                i += 2
            else:
                if regA[0] == 0:
                    i += 2
                else:
                    i = lit
        if output[:-1] == numb:
            poss.append(currentA<< 3 | d)
    return poss

def challenge2():
    regA_build = {i:[] for i in range(n+1)}
    regA_build[n] = [0]
    for i in range(n-1,-1,-1):
        for last_regA in regA_build[i+1]:
            regA_build[i] += code_number(last_regA,str(program[i]))
    return min(regA_build[0])


print("Challenge 2:",challenge2())