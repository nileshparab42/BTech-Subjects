import copy

# problem 
initial = [ [ 1, 3, 7 ],
            [ 4, 0, 6 ],
            [ 2, 5, 8 ] ]

final = [ [ 1, 3, 7 ],
            [ 4, 6, 8 ],
            [ 2, 5, 0 ] ]

n=3
queue=[]
queue.append(initial)

queue=[]
rank=[]
huristics=[]
visited=[]
deapth=0

def prmat(matrix):
    mat = copy.deepcopy(matrix)
    print(str(mat[0][0])+" "+str(mat[0][1])+" "+str(mat[0][2])+"\n"+str(mat[1][0])+" "+str(mat[1][1])+" "+str(mat[1][2])+"\n"+str(mat[2][0])+" "+str(mat[2][1])+" "+str(mat[2][2])+"\n")
                
def pos(matrix,n):
    mat = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            if mat[i][j]==0:
                return i,j

#up
def up(matrix,pos,crank):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[0]-1==-1:
        ele2=mat[pos[0]-1][pos[1]]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]-1][pos[1]]=ele1
        queue.append(mat)
        hu_val=huristic(mat)+crank+1
        huristics.append(hu_val)
        rank.append(crank+1)
        
#down
def down(matrix,pos,crank):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[0]+1==n:
        ele2=mat[pos[0]+1][pos[1]]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]+1][pos[1]]=ele1
        queue.append(mat)
        hu_val=huristic(mat)+crank+1
        huristics.append(hu_val)
        rank.append(crank+1)
        
#right
def right(matrix,pos,crank):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[1]+1==n:
        ele2=mat[pos[0]][pos[1]+1]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]][pos[1]+1]=ele1
        queue.append(mat)
        hu_val=huristic(mat)+crank+1
        huristics.append(hu_val)
        rank.append(crank+1)
        
#left
def left(matrix,pos,crank):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[1]-1==-1:
        ele2=mat[pos[0]][pos[1]-1]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]][pos[1]-1]=ele1
        queue.append(mat)
        hu_val=huristic(mat)+crank+1
        huristics.append(hu_val)
        rank.append(crank+1)
     
#check
def check(matrix1):
    mat1 = copy.deepcopy(matrix1)
    mat2 = copy.deepcopy(final)
    for i in range(n):
        for j in range(n):
            if mat1[i][j]!=mat2[i][j]:
                return False
    return True

def huristic(matrix1):
    hu=0
    mat1 = copy.deepcopy(matrix1)
    mat2 = copy.deepcopy(final)
    for i in range(n):
        for j in range(n):
            if mat1[i][j]!=mat2[i][j]:
                hu=hu+1
    return hu

def min_val():
    min_hu=100
    pos=100
    for i in range(len(huristics)):
        if huristics[i]<min_hu:
            if i not in visited:
                pos=i
                min_hu=huristics[i]
    return pos


queue.append(initial)
rank.append(deapth)
huristics.append(huristic(queue[0]))
power=0


flag=1
while flag == 1 :
    visited.append(power)
    crank=rank[power]
    position=pos(queue[power],n)
    
    left(queue[power],position,crank)
    right(queue[power],position,crank)
    up(queue[power],position,crank)
    down(queue[power],position,crank)
    
    
    power=min_val()
    
    if(check(queue[power])):
        visited.append(power)
        flag=0
    
for i in range(len(visited)):
       print("Huristic: "+str(huristics[visited[i]]))
       prmat(queue[visited[i]])
       

