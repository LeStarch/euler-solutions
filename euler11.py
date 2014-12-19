file = open("euler11.data","r")
lines = file.readlines()
grid = []
for line in lines:
    grid.append( [int(elem) for elem in line.strip("\n").split()])
    
xlen = len(grid[0])
ylen = len(grid)

def down(grid, i,j):
   if j+3 >= len(grid):
       return 0
   return grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]

def right(grid, i,j):
   if i+3 >= len(grid[0]):
       return 0
   return grid[j][i]*grid[j][i+1]*grid[j][i+2]*grid[j][i+3]
def dwri(grid, i,j):
   if i+3 >= len(grid[0]):
       return 0
   if j+3 >= len(grid):
       return 0
   return grid[j][i]*grid[j+1][i+1]*grid[j+2][i+2]*grid[j+3][i+3]
def dwlf(grid, i,j):
   if i-3 < 0:
       return 0
   if j+3 >= len(grid):
       return 0
   return grid[j][i]*grid[j+1][i-1]*grid[j+2][i-2]*grid[j+3][i-3]
ma = 0
for i in range(0,xlen):
   for j in range(0,ylen):
       ma = max([ma,down(grid,i,j),right(grid,i,j),dwri(grid,i,j),dwlf(grid,i,j)])
print(ma) 
