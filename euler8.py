
file = open("euler8.data","r")
nums = []
nums.append(int(file.read(1)))
nums.append(int(file.read(1)))
nums.append(int(file.read(1)))
nums.append(int(file.read(1)))
nums.append(int(file.read(1)))
mult = nums[0]*nums[1]*nums[2]*nums[3]*nums[4]
chr = file.read(1)
while chr != '\n' :
  del nums[0]
  nums.append(int(chr))
  mult = max(mult,nums[0]*nums[1]*nums[2]*nums[3]*nums[4]) 
  chr = file.read(1)
print(mult)
