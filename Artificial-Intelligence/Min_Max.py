arr=[3,5,2,9,12,5,23,23]
import math

n=len(arr)
m=int(math.log(8,2))
print(m)
ans=[]

def mini(a,b):
    if a<b:
        return a
    else: 
        return b
    
def maxi(a,b):
    if a>b:
        return a
    else: 
        return b
    
for i in range(m):
    if i%2==0:
        for z in range(0,len(arr)-1,2):
            ele=maxi(arr[z],arr[z+1])
            ans.append(ele)
            
            
    else:
        for z in range(0,len(arr)-1,2):
            ans.append(mini(arr[z],arr[z+1]))
            
    arr=ans    
    ans=[]

print(arr)
