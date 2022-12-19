#-------- Ip class identification --------#

# Taking ip address from user
ip=input("Enter ip address :")
x = ip.split(".")
z=x[0]
y =int(z)

# Classifing ip address
if(y<=127 and y>=0):
    print("Ip address is in class A")
    net_id=x[0]
    host_id=x[1]+"."+x[2]+"."+x[3]
    print("Network id :"+net_id)
    print("Host id :"+host_id)
if(y<=191 and y>=128):
    print("Ip address is in class B")
    net_id=x[0]+"."+x[1]
    host_id=x[2]+"."+x[3]
    print("Network id :"+net_id)
    print("Host id :"+host_id)
if(y<=223 and y>=192):
    print("Ip address is in class C")
    net_id=x[0]+"."+x[1]+"."+x[2]
    host_id=x[3]
    print("Network id : "+net_id)
    print("Host id : "+host_id)
if(y<=239 and y>=224):
    print("Ip address is in class D")
    print("Class D does not contain netid and hostid")
if(y<=255 and y>=240):
    print("Ip address is in class E")
    print("Class E does not contain netid and hostid")
    
    
    