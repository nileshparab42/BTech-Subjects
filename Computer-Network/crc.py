#------------- Cyclic Redundancy Check -------------

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

# Sender Side operations
print("--- Sender Side --- \n")
# Se=input("Data word :")
# Dd=input("Key :")
Se="110010101"
Dd="10101"
m=len(Dd)
Dv=Se

for i in range(m-1):
    Dv=Dv+"0"
n=len(Dv)
rem=Dv[:m]

for i in range(m,n+1):
    if rem[0]=="1":
        for j in range(m):
            chr=xor(rem[j],Dd[j])
            rem = rem[:j] + chr + rem[j+1:]
    if i==n:
        rem=rem[1:]                       
    else:
        rem=rem[1:]
        rem=rem+Dv[i]
   
se_code=Se+rem[:]
print("Data sent :"+se_code)

# Receiver Side operations
print("\n--- Receiver Side --- \n")
m=len(Dd)
Dv=input("Enter codeword :")
n=len(Dv)
rem=Dv[:m]

for i in range(m,n+1):
    if rem[0]=="1":
        for j in range(m):
            chr=xor(rem[j],Dd[j])
            rem = rem[:j] + chr + rem[j+1:]
    if i==n:
        rem=rem[1:]                       
    else:
        rem=rem[1:]
        rem=rem+Dv[i]
   
Re_code=rem[:]
Cr=""
print("Remainder:"+Re_code)
for i in range(m-1):
    Cr=Cr+"0"

# Final Conclusion
print("\n--- Conclusion ---")
if Re_code==Cr:
    print("Correct data received !")
else:
     print("Wrong data received !")

#------------- End of program -------------