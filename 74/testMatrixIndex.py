
def matrixindexer(m,i):
    print(f"{(i//3)}  {i%3} {m[(i//3)][i%3]}")
    
m = [[0,1,2],[3,4,5]]



for x in range(5):
    print(matrixindexer(m,x))