code=["+ a b X","* c d Y","- X Y Z","= Z ? W"]
ncode=[]

for line in code:
    if line[0]=="+":
        ncode.append("MOV"+" R0,"+line[2])
        ncode.append("ADD"+" R0,"+line[4])
        ncode.append("MOV"+" "+line[6]+","+"R0")

    if line[0]=="-":
        ncode.append("MOV"+" R0,"+line[2])
        ncode.append("SUB"+" R0,"+line[4])
        ncode.append("MOV"+" "+line[6]+","+"R0")

    if line[0]=="*":
        ncode.append("MOV"+" R0,"+line[2])
        ncode.append("MUL"+" R0,"+line[4])
        ncode.append("MOV"+" "+line[6]+","+"R0")

    if line[0]=="=":
        ncode.append("MOV "+line[2]+","+" R0")
        ncode.append("MUL"+" R0,"+line[2])
        ncode.append("MOV"+" "+line[6]+","+"R0")

print("Input:")
for line in code:
    print(line)
print("\n")
print("Output:")
for line in ncode:
    print(line)