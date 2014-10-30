import copy, random

matrix = [[0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]

"""
Rules: 

each cell next generation: 
- under-pop: <2 neighbors: dies
- 2 or 3 neighbors: live 
- overcrowding: >3 neighbors: dies
- reproduction: every dead cell with exactly 3 neighbors: live

"""

def show_matrix(mat):
	for row in mat:
		print " ".join(str(x) for x in row)

def neighborhood(x,y, matrix):
    nbs = 0
    for i in range(y-1,y+1):
        for j in range(x-1,x+1):
            if matrix[i][j]:
                nbs+=1
    if matrix[x][y]:
        nbs-=1
    return nbs

def makenext(height, width, init=1):
    nextm = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(init)
        nextm.append(row)
    return nextm

def nextgen(matrix):
    plusgen = makenext(8,8)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            nbs = neighborhood(x,y,matrix)
            if (nbs < 2) or (nbs > 3):
                plusgen[x][y] = 0
    return plusgen

if __name__ == "__main__":
    start = makenext(8,8, init=0)
    for i in range(15):
    	x = random.randint(0,7)
    	y = random.randint(0,7)
    	start[x][y] = 1

    show_matrix(start)
    show_matrix(nextgen(start))


		
