code="a*b+c/d-e/f+g/f"
ncode=[]
variables="ZYXWVUTS"
operators="/*+-"

for operator in operators:
    for pos_res in range(len(code)):
        if code[pos_res]==operator:
            nvar=variables[0]
            ncode.append(nvar+"="+code[pos_res-1:pos_res+2])
            code=code[:pos_res-1]+nvar+code[pos_res+2:]
            code=code+"  "
            variables=variables[1:]
print(ncode)





        