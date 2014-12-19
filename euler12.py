#Return triangle numbers
def triangleGen():
    num = 1
    tri = 0
    while True:
        tri = tri + num
        yield tri
        num = num + 1

#Check all triangle numbers
for tri in triangleGen():
    count = 0
    num = 1
    while num <= tri:
        if tri % num == 0:
            count = count + 1
        if count  >= 500:
            break
        if count == 200 or count == 300 or count == 400 or count == 450:
            print("Found: ",count)
        num = num + 1
    if count == 500:
        break    
print(tri)  
