file = open("euler18.data","r")
lines = file.readlines()
lines.reverse()
tmp = None
for line in lines:
    nums = [int(elem) for elem in line.strip("\n").split()]
    if not tmp is None:
        for i in range(0,len(nums)):
            nums[i] = nums[i]+ max(tmp[i],tmp[i+1])
    print(nums)
    tmp = nums
