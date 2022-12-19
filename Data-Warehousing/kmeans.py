# ---------- k means Algorithm ----------#

data=[2,10,15,3,4,25,30,26]

# Spliting data for initial cluster
k1=[data[0]]
k2=data[1:]

# calculating mean of each cluster
m1=sum(k1)/len(k1)
m2=sum(k2)/len(k2)

# Taking temporary list 
temp1=[]
temp2=[]

# Generating clusters
for z in range(10):
    for j in k1:
        if abs(m1-j)<=abs(m2-j):
            temp1=temp1+[j]
        else:
            temp2=temp2+[j]

    for j in k2:
        if abs(m1-j)<=abs(m2-j):
            temp1=temp1+[j]
        else:
            temp2=temp2+[j]

    m1=sum(temp1)/len(temp1)
    m2=sum(temp2)/len(temp2)
    k1=temp1
    k2=temp2
    temp1=[]
    temp2=[]


print(k1)
print(k2)