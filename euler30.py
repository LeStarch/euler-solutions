num = 2
sum = 0
while num <= 2480058:
    p = 5
    val = 0
    for c in str(num):
        val = val + pow(int(c),p)
    if val == num:
        sum = sum + num
    num = num + 1
print(sum)
