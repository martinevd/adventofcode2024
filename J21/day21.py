import functools

with open('input.txt', 'r') as file:
    codes = file.read().splitlines()

def is_valid(sign,x,y,current):
    for direct in current:
        dx,dy = 0,0
        if direct == "^":
            dy = -1
        elif direct == "v":
            dy = 1
        elif direct == ">":
            dx = 1
        elif direct == "<":
            dx = -1
        x,y = x+dx,y+dy
        if (x,y) not in sign:
            return False
    return True

def all_permutation(sign,xstart,ystart,nup,ndown,nleft,nright,current,res):
    if nup == 0 and ndown == 0 and nleft == 0 and nright == 0 :
        if is_valid(sign,xstart,ystart,current):
            res.append(current)
        return res
    if nup > 0:
        all_permutation(sign,xstart,ystart,nup - 1,ndown,nleft,nright,current + "^",res)
    if ndown > 0:
        all_permutation(sign,xstart,ystart,nup,ndown - 1,nleft,nright,current + "v",res)
    if nleft > 0:
        all_permutation(sign,xstart,ystart,nup,ndown,nleft - 1,nright,current + "<",res)
    if nright > 0:
        all_permutation(sign,xstart,ystart,nup,ndown,nleft,nright - 1,current + ">",res)
    return res

def init_pad(sign):
    pad = {}
    for (x1,y1),val1 in sign.items():
        for (x2,y2),val2 in sign.items():
            dx,dy = x1-x2,y1-y2
            nup,ndown,nleft,nright = 0,0,0,0
            if dy < 0:
                ndown = (-1)*dy
            else:
                nup = dy
            if dx < 0:
                nright = (-1)*dx
            else:
                nleft = dx
            pad[(val1,val2)] = all_permutation(sign,x1,y1,nup,ndown,nleft,nright,"",[])
    return pad

nums_seq = init_pad({(0,0):"7",(1,0):"8",(2,0):"9",(0,1):"4",(1,1):"5",(2,1):"6",(0,2):"1",(1,2):"2",(2,2):"3",(1,3):"0",(2,3):"A"})
dirs_seq = init_pad({(1,0):"^",(2,0):"A",(0,1):"<",(1,1):"v",(2,1):">"})

@functools.cache
def solve_one(n,is_num,start,end):
    if n == 0:
        return 1

    if is_num:
        pad_seq = nums_seq
    else:
        pad_seq = dirs_seq

    best_res = float("inf")
    for seq in pad_seq[(start,end)]:
        seq += "A"
        res = 0
        act = "A"
        for i in range(len(seq)):
            res += solve_one(n-1,False,act,seq[i])
            act = seq[i]
        best_res = min(res,best_res)
    return best_res

def solve(n,code):
    res = 0
    act = "A"
    for i in range(len(code)):
        res += solve_one(n+1,True,act,code[i])
        act = code[i]
    return res

print("Challenge 1:",sum([solve(2,code)*int(code[:-1]) for code in codes]))
print("Challenge 2:",sum([solve(25,code)*int(code[:-1]) for code in codes]))