#-------------- Bit Stuffing --------------#

code="00111111001"
codeword=""
c=0
for i in range(0,len(code)-1):
    if code[i]=="0":
        c=0
        codeword=codeword+"0"
    if code[i]=="1":
        c=c+1
        if(c==6):
            codeword=codeword+"01"
        else:
            codeword=codeword+"1"

print("Codeword (before stuffing) :"+code)
print("Codeword (after stuffing):"+codeword)
