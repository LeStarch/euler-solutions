num = 100
fact = 1
while num != 0:
   fact = fact * num
   num = num - 1 
st = str(fact)
sum = 0
for c in st:
    sum = sum + int(c)
print(sum)
