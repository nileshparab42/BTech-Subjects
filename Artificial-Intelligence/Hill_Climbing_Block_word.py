import copy

start=["B","C","D","A"]
end=["A","B","C","D"]
buffer = [[],[],[],[]]
buffer[0]=start



def generate(buffer):
    movables=[]
    tops=[]
    for state in buffer:
        if len(state)>1:
            tops.append(state[-1])
        if len(state)==1:
            movables.append(state[0])
    return tops,movables

def pos(ele,buffer):
    i=0
    j=0
    for state in buffer:
        for block in state:
            if block==ele:
                return i,j
            j=j+1
        i=i+1

def huristic(buffer):
    pre_hu=0
    for state in buffer:
        if len(state)>1:
            for i in range(1,len(state)):
                if state[i]!=end[i]:
                    hu=-1*i
                    pre_hu=hu+pre_hu
                if state[i]==end[i]:
                    hu=1*i
                    pre_hu=hu+pre_hu
    return pre_hu
                    
        
        
def top_bottom(buffer):
    buf=copy.deepcopy(buffer)
    args=generate(buf)
    for block in args[0]:
        buf1=copy.deepcopy(buf)
        position=pos(block,buf1)
        buf1[position[0]].remove(block)
        for state in buf1:
            if len(state)==0:
                state.append(block)
                queue.append(buf1)
                huristics.append(huristic(buf1))
                return
                
            
def bottom_top(buffer):
    buf=copy.deepcopy(buffer)
    args=generate(buf)
    for block in args[1]:
        buf1=copy.deepcopy(buf)
        position=pos(block,buf1)
        buf1[position[0]].remove(block)
        for block1 in args[0]:
            buf2=copy.deepcopy(buf1)
            position=pos(block1,buf2)
            buf2[position[0]].append(block)
            queue.append(buf2)
            huristics.append(huristic(buf2))
        for block2 in args[1]:
            if block2!=block:
                buf2=copy.deepcopy(buf1)
                position=pos(block2,buf2)
                buf2[position[0]].append(block)
                queue.append(buf2)
                huristics.append(huristic(buf2))
                
def max_val(arr):
    maxi=-100
    pos=-100
    for i in range(len(arr)):
        if maxi<arr[i]:
            maxi=arr[i]
            pos=i
    return pos
   

queue=[]
huristics=[]
power=buffer
hu_end=6

flag =1
while flag==1:
    print("Huristic: "+str(huristic(power)))
    print(power)
    print("\n")
    if huristic(power)==hu_end:
        flag=0
    top_bottom(power)
    bottom_top(power)
    power=queue[max_val(huristics)]
    queue=[]
    huristics=[]