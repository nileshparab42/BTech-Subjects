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
     
#check
def check(matrix1,matrix2):
    mat1 = copy.deepcopy(matrix1)
    mat2 = copy.deepcopy(matrix2)
    for i in range(n):
        for j in range(n):
            if mat1[i][j]!=mat2[i][j]:
                return True
    return False

queue.append(initial)

loop=0
while loop==0:
    position=pos(queue[0],n)
    left(queue[0],position)
    right(queue[0],position)
    up(queue[0],position)
    down(queue[0],position)
    queue=queue[1:]
    if check(queue[0],final):
        print(queue[0])
        print("\n")
    else:
        print("Final ans:")
        print(queue[0])
        loop=1