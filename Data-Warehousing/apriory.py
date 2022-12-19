# ----------- Apriory Algorithm -----------#

t=[
    ["I1","I2","I5"],
    ["I2","I4"],
    ["I2","I3"],
    ["I1","I2","I4"],
    ["I1","I3"],
    ["I2","I3"],
    ["I1","I3"],
    ["I1","I2","I3","I5"],
    ["I1","I2","I3"]
]

sc=2
cf=50

c1i=["I1","I2","I3","I4","I5"]
c1c=[0,0,0,0,0]


for i in t:
    for j in i:
        if j=="I1":
            c1c[0]=c1c[0]+1
        if j=="I2":
            c1c[1]=c1c[1]+1
        if j=="I3":
            c1c[2]=c1c[2]+1
        if j=="I4":
            c1c[3]=c1c[3]+1
        if j=="I5":
            c1c[4]=c1c[4]+1



c2i=["I1I2","I1I3","I1I4","I1I5","I2I3","I2I4","I2I5","I3I4","I3I5","I4I5"]
c2c=[0,0,0,0,0,0,0,0,0,0]

for i in t:

    if "I1" in i:
        if "I2" in i:
            c2c[0]=c2c[0]+1

    if "I1" in i:
        if "I3" in i:
            c2c[1]=c2c[1]+1

    if "I1" in i:
        if "I4" in i:
            c2c[2]=c2c[2]+1

    if "I1" in i:
        if "I5" in i:
            c2c[3]=c2c[3]+1

    if "I2" in i:
        if "I3" in i:
            c2c[4]=c2c[4]+1

    if "I2" in i:
        if "I4" in i:
            c2c[5]=c2c[5]+1

    if "I2" in i:
        if "I5" in i:
            c2c[6]=c2c[6]+1

    if "I3" in i:
        if "I4" in i:
            c2c[7]=c2c[7]+1

    if "I3" in i:
        if "I5" in i:
            c2c[8]=c2c[8]+1

    if "I4" in i:
        if "I5" in i:
            c2c[9]=c2c[9]+1


c3i=["I1I2I3","I1I2I4","I1I2I5","I1I3I4","I1I3I5","I1I4I5","I2I3I4","I2I3I5","I2I4I5","I3I4I5"]
c3c=[0,0,0,0,0,0,0,0,0,0]

for i in t:

    if "I1" in i:
        if "I2" in i:
            if "I3" in i:
                c3c[0]=c3c[0]+1

    if "I1" in i:
        if "I2" in i:
            if "I4" in i:
                c3c[1]=c3c[1]+1

    if "I1" in i:
        if "I2" in i:
            if "I5" in i:
                c3c[2]=c3c[2]+1

    if "I1" in i:
        if "I3" in i:
            if "I4" in i:
                c3c[3]=c3c[3]+1

    if "I1" in i:
        if "I3" in i:
            if "I5" in i:
                c3c[4]=c3c[4]+1

    if "I1" in i:
        if "I4" in i:
            if "I5" in i:
                c3c[5]=c3c[5]+1

    if "I2" in i:
        if "I3" in i:
            if "I4" in i:
                c3c[6]=c3c[6]+1

    if "I2" in i:
        if "I3" in i:
            if "I5" in i:
                c3c[7]=c3c[7]+1

    if "I2" in i:
        if "I4" in i:
            if "I5" in i:
                c3c[8]=c3c[8]+1

    if "I3" in i:
        if "I4" in i:
            if "I5" in i:
                c3c[9]=c3c[9]+1


rules=[]
rulec=[]
frules=""

print("------------------------------------------")

# PRINTING C1 AND L1:
print("C1 :")
print("Items\tCount")
for i in range(len(c1i)):
    if c1c[i]!=0:
        print(c1i[i]+"\t\t"+str(c1c[i]))

print("\n")
print("L1 :")
print("Items\tCount")
for i in range(len(c1i)):
    if c1c[i]>=sc:
        print(c1i[i]+"\t\t"+str(c1c[i]))

print("------------------------------------------")


# PRINTING C2 AND L2:
print("C2 :")
print("Items\tCount")
for i in range(len(c2i)):
    if c2c[i]!=0:
        print(c2i[i]+"\t\t"+str(c2c[i]))

print("\n")
print("L1 :")
print("Items\tCount")
for i in range(len(c2i)):
    if c2c[i]>=sc:
        print(c2i[i]+"\t\t"+str(c2c[i]))

print("------------------------------------------")

# PRINTING C3 AND L3:
print("C3 :")
print("Items\tCount")
for i in range(len(c3i)):
    if c3c[i]!=0:
        print(c3i[i]+"\t\t"+str(c3c[i]))

print("\n")
print("L3 :")
print("Items\tCount")
for i in range(len(c3i)):
    if c3c[i]>=sc:
        rules.append(c3i[i])
        rulec.append(c3c[i])
        print(c3i[i]+"\t\t"+str(c3c[i]))

print("------------------------------------------")
print("\n")
print("Rules:")
print(rules)
print("\n")
print("------------------------------------------")
a=rulec[0]
b=0
for i in t:
    if str(rules[0][:2]) in i:
        if str(rules[0][2:4]) in i:
            b=b+1
print("For Itemset {"+str(rules[0])+"} :")
c=(a/b)*100
if c>=cf:
    frules=frules+" Rule 1 "

print(str(rules[0][:2])+str(rules[0][2:4])+"->"+str(rules[0][4:6])+" Confidence= "+str((a/b)*100)+"%")

print("------------------------------------------")

a=rulec[0]
b=0
for i in t:
    if str(rules[0][2:4]) in i:
        if str(rules[0][4:6]) in i:
            b=b+1
print("For Itemset {"+str(rules[0])+"} :")
c=(a/b)*100
if c>=cf:
    frules=frules+" Rule 2 "

print(str(rules[0][2:4])+str(rules[0][4:6])+"->"+str(rules[0][:2])+" Confidence= "+str((a/b)*100)+"%")

print("------------------------------------------")

a=rulec[0]
b=0
for i in t:
    if str(rules[0][4:]) in i:
        if str(rules[0][:2]) in i:
            b=b+1
print("For Itemset {"+str(rules[0])+"} :")
c=(a/b)*100
if c>=cf:
    frules=frules+" Rule 3 "

print(str(rules[0][4:])+str(rules[0][:2])+"->"+str(rules[0][2:4])+" Confidence= "+str((a/b)*100)+"%")

print("------------------------------------------")

a=rulec[0]
b=0
for i in t:
    if str(rules[0][:2]) in i:
        b=b+1
print("For Itemset {"+str(rules[0])+"} :")
c=(a/b)*100
if c>=cf:
    frules=frules+" Rule 4 "

print(str(rules[0][:2])+"->"+str(rules[0][2:4])+str(rules[0][4:])+" Confidence= "+str((a/b)*100)+"%")

print("------------------------------------------")

a=rulec[0]
b=0
for i in t:
    if str(rules[0][2:4]) in i:
        b=b+1
print("For Itemset {"+str(rules[0])+"} :")
c=(a/b)*100
if c>=cf:
    frules=frules+" Rule 5 "

print(str(rules[0][2:4])+"->"+str(rules[0][:2])+str(rules[0][4:])+" Confidence= "+str((a/b)*100)+"%")


print("------------------------------------------")

a=rulec[0]
b=0
for i in t:
    if str(rules[0][4:]) in i:
        b=b+1
print("For Itemset {"+str(rules[0])+"} :")
c=(a/b)*100
if c>=cf:
    frules=frules+" Rule 6 "

print(str(rules[0][4:])+"->"+str(rules[0][:2])+str(rules[0][2:4])+" Confidence= "+str((a/b)*100)+"%")

print("------------------------------------------")

print("So, we are selecting :")
print(frules)

    



