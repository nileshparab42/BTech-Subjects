import copy
initial = [0,0]  
cap = [5,4]
final = [0,2]

def empty_jug0(jugs):
    jugs_cpy = copy.deepcopy(jugs)
    jugs_cpy[0]=0
    return jugs_cpy

def empty_jug1(jugs):
    jugs_cpy = copy.deepcopy(jugs)
    jugs_cpy[1]=0
    return jugs_cpy

def full_jug0(jugs):
    jugs_cpy = copy.deepcopy(jugs)
    jugs_cpy[0]=cap[0]
    return jugs_cpy

def full_jug1(jugs):
    jugs_cpy = copy.deepcopy(jugs)
    jugs_cpy[1]=cap[1]
    return jugs_cpy

def trans_jug0(jugs):
    jugs_cpy = copy.deepcopy(jugs)
    jug0_space = cap[0]-jugs_cpy[0]
    if jug0_space <= jugs_cpy[1]:
        jugs_cpy[1] = jugs_cpy[1]-jug0_space 
        jugs_cpy[0] = jug0_space+jugs_cpy[0]
    else:
        jug1_store = copy.deepcopy(jugs_cpy[1])
        jugs_cpy[1] = 0
        jugs_cpy[0] = jug1_store+jugs_cpy[0]
    return jugs_cpy

def trans_jug1(jugs):
    jugs_cpy = copy.deepcopy(jugs)
    jug1_space = cap[1]-jugs_cpy[1]
    if jug1_space <= jugs_cpy[0]:
        jugs_cpy[0] = jugs_cpy[0]-jug1_space 
        jugs_cpy[1] = jug1_space+jugs_cpy[1]
    else:
        jug0_store = copy.deepcopy(jugs_cpy[0])
        jugs_cpy[0] = 0
        jugs_cpy[1] = jug0_store+jugs_cpy[1]
    return jugs_cpy

exp=[]
stack = []
stack.append(initial)

flag=1
while flag==1:
    
    top=len(stack)-1
    
    if(stack[top] in exp):
        stack=stack[:-1]
        top=len(stack)-1
    else:
        exp.append(stack[top])
        stack.append(empty_jug0(stack[top]))
        stack.append(empty_jug1(stack[top]))
        stack.append(trans_jug0(stack[top]))
        stack.append(trans_jug1(stack[top]))
        stack.append(full_jug0(stack[top]))
        stack.append(full_jug1(stack[top]))
        top=len(stack)-1

        
    if(stack[top]==final):
        flag=0

print(exp)