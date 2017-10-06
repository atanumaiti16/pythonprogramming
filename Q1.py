import re


ip=input("enter the sentence")

ip2=re.sub("[^\w]", " ",  ip).split()
print(ip2)
ip3=list()
print(type(ip3))

for i in ip2:
    if i not in ip3:
        ip3.append(i)

ip3.sort()
print(ip3)
#ip_list=[str(n) for n in ip.split()]