# ----------- Binning Algorithm -----------#

from math import floor

data=[4,8,9,15,21,21,24,25,26,28,29,34]
min(data)
no=floor((max(data)-min(data))/len(data))

part=int(len(data)/no)
meanbin=list()
boundrybin=list()

# partitioning Data
for i in range(0,len(data),part):
    meanbin.append(data[i:i+part])

# Bin mean calculations
p=0
for bin in meanbin:
    avg=floor(sum(bin)/len(bin))
    q=0
    for num in bin:
        meanbin[p][q]=avg
        q=q+1
    p=p+1


for i in range(0,len(data),part):
    boundrybin.append(data[i:i+part])

# Boundry mean calculations
p=0
for bin in boundrybin:
    binmax=max(bin)
    binmin=min(bin)
    q=0
    for num in bin:
        if abs(boundrybin[p][q]-binmin)<=abs(boundrybin[p][q]-binmax):
            boundrybin[p][q]=binmin
        else:
            boundrybin[p][q]=binmax
        q=q+1
    p=p+1

# Printing bin mean :
print("Bin Mean :")
i=1
for bin in meanbin:
    print("Bin "+str(i)+":"+str(bin))
    i=i+1

print("\n")

# Printing bin boundry :
print("Bin Boundry :")
i=1
for bin in boundrybin:
    print("Bin "+str(i)+":"+str(bin))
    i=i+1
