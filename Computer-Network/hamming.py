#-------------- Humming Code --------------# 

# XOR Function
def xor(a,b):
    a=str(a)
    b=str(b)
    if a=="0" and b=="0":
        return "0"
    elif a=="0" and b=="1":
        return "1"
    elif a=="1" and b=="0":
        return "1"
    elif a=="1" and b=="1":
        return "0"

# patrity generator at sender        
a="x0000101"
b=""
print("Codeword :"+a[7]+a[6]+a[5]+a[3])
cr=xor(a[1],a[3])
cr=xor(a[5],cr)
b=b+xor(a[7],cr)
cr=xor(a[2],a[3])
cr=xor(a[6],cr)
b=b+xor(a[7],cr)
b=b+a[3]
cr=xor(a[4],a[5])
cr=xor(a[6],cr)
b=b+xor(a[7],cr)
b=b+a[5]
b=b+a[6]
b=b+a[7]
print("Hamming code : "+b[::-1])

# Codeword at received at receiver 
p="1100101"
print("Codeword at receiver : "+p[::-1])

# Error detection
if p[0]==b[0]:
    x=0
else :
    x=1
    
if p[1]==b[1]:
    y=0
else :
    y=1
    
if p[3]==b[3]:
    z=0
else :
    z=1

pos=(x*1)+(y*2)+(z*4)
print("Error found at position : "+str(pos))

# Error correction
index = pos-1
if p[index]=="0":
    chr="1"
if p[index]=="1":
    chr="0"

p = p[:index] + chr + p[index+1:]

print("Corrected codeword : "+p[::-1])

#------------- End of program -------------






