code = """
int main()
{
  // 2 variables
  int a, b;
  a = 10;
 return 0;
}"""

Keywords = ["int","main()","return"]
Operators =  ["="]
Separators= ["{","}",",",";"]
comment=["//"]
a=[]
b=[]
c=[]
d=[]
e=[]

def com(line):
    for keyword in line:
        if keyword in comment:
            return True
    

lines = code.splitlines()


for line in lines:
    if com(line.split()):
        e.append(line.split())
    else:
        for keyword in line.split():
            if keyword in comment:
                e.append(keyword)
            else:
                if keyword in Keywords:
                    a.append(keyword)
                elif keyword in Operators:
                    b.append(keyword)
                elif keyword in Separators:
                    c.append(keyword)
                else:
                    d.append(keyword)
        
print("Keywords: "+str(a))
print("Operators: "+str(b))
print("Seperators: "+str(c))
print("Identifier: "+str(d))
print("Comments: "+str(e))
