f = open("euler13.data","r")
num = 0
for i in f.readlines():
    num = num + int(i.strip())
print(str(num)[0:10])
