import copy

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

def neighborhood(x,y, matrix):
    nbs = 0
    for i in range(y-1,y+1):
        for j in range(x-1,x+1):
            if matrix[i][j]:
                nbs+=1
    if matrix[x][y]:
        ngs-=1
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
                nmat[x][y] = 0
            

if __name__ == "__main__":
    print makenext(8,8)
	
