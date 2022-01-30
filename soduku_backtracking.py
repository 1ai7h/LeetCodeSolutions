import numpy as np
grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
print(np.matrix(grid)) #Creates the Matrix using Numpy to make things easier

def check_valid(y,x,n): #Check if the number n can be fit in the graph with x,y position
    global grid
    for i in range(0,9):
        if grid[y][i] == n: #if the 9 columns have the number present then we cannot add it in
            return False
    for i in range(0,9): #if the 9 rows have the number in them we cannot add them in
        if grid[i][x] == n:
            return False
        '''
        This next piece of code was used in order to handle the boxes, one of the rules
        of soduku is that you cannot have the same number in the row, column, OR box. from our visualization
        we find that we have a set of 9 boxes grouped together which cannot have identical numbers.
        '''
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True
  
  def solve():
    global grid
    for y in range(9) : #for all y values (columns)
        for x in range(9) : #for all x values (rows)
            if grid[y][x] == 0 : #if there is an empty space
                for n in range(1,10) : #try out all numbers using brute force by passing the number through our function check_valud
                    if check_valid(y,x,n): #if found
                        grid[y][x] = n #set the number 
                        solve() #recursively do this all over again 
                        grid[y][x] = 0 #if the number is not valid, set it to 0 
                return 
    print(np.matrix(grid)) #show grid

solve()
