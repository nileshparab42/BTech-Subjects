import copy
initial = [ [ 1, 3, 7 ],
            [ 4, 0, 6 ],
            [ 2, 5, 8 ] ]
final = [ [ 1, 3, 7 ],
            [ 4, 6, 8 ],
            [ 2, 5, 0 ] ]
n=3
queue=[]

def pos(matrix,n):
    mat = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            if mat[i][j]==0:
                return i,j
            
def check(matrix1,matrix2):
    mat1 = copy.deepcopy(matrix1)
    mat2 = copy.deepcopy(matrix2)
    for i in range(n):
        for j in range(n):
            if mat1[i][j]!=mat2[i][j]:
                return False
    return True
            
#up
def up(matrix,pos):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[0]-1==-1:
        ele2=mat[pos[0]-1][pos[1]]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]-1][pos[1]]=ele1
        queue.append(mat)
        
#down
def down(matrix,pos):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[0]+1==n:
        ele2=mat[pos[0]+1][pos[1]]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]+1][pos[1]]=ele1
        queue.append(mat)
        
#right
def right(matrix,pos):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[1]+1==n:
        ele2=mat[pos[0]][pos[1]+1]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]][pos[1]+1]=ele1
        queue.append(mat)
        
#left
def left(matrix,pos):
    mat = copy.deepcopy(matrix)
    ele1=mat[pos[0]][pos[1]]
    if not pos[1]-1==-1:
        ele2=mat[pos[0]][pos[1]-1]
        mat[pos[0]][pos[1]]=ele2
        mat[pos[0]][pos[1]-1]=ele1
        queue.append(mat)
    

def huristic(matrix1):
    hv=0
    mat1 = copy.deepcopy(matrix1)
    mat2 = copy.deepcopy(final)
    for i in range(n):
        for j in range(n):
            if mat1[i][j]!=mat2[i][j]:
                hv=hv+1
    return hv

def min_hu(hu_vals,parent_hu):
    pos=-1
    for i in range(4):
        if hu_vals[i]<parent_hu:
            pos = i
            return pos
    return pos


hu_vals=[]
parent=initial
parent_hu = huristic(initial)
print(parent)
print("Huristic value:"+str(parent_hu))
print("\n")

flag=1
while flag==1:
    position=pos(parent,n)
    left(parent,position)
    right(parent,position)
    up(parent,position)
    down(parent,position)
    hu_vals.append(huristic(queue[0]))
    hu_vals.append(huristic(queue[1]))
    hu_vals.append(huristic(queue[2]))
    hu_vals.append(huristic(queue[3]))

    hu_pos = min_hu(hu_vals,parent_hu)

    parent=queue[hu_pos]
    parent_hu = huristic(queue[hu_pos])
    
    if(check(parent,final)):
        flag=0
        
    print(parent)
    print("Huristic value:"+str(parent_hu))
    print("\n")


    