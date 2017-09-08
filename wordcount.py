

file=open("/home/atanu/Desktop/lab1" , "r+")
count={}
for i in file.read().split():
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for a,b in count.items():
    print(a,b )