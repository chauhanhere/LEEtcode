#This is valid on a 1D array to reshape it into different dimensional matrix 1*6
#We are giving input 1D Array and output is matrix with r=3 and column=2 2*3
"""
import numpy as np
a=[1,2,3,6,3,5]
r=3
c=2
if len(a)==(r*c):
    print(np.reshape(a,(r, c)).tolist())
else:
    print(a)
"""
#This is valid on a any dimensional matrix to reshape it into different dimensional matrix
#We are giving input 3*4 matrix and output is matrix with r=2 and column=6 2*6
import numpy as np
def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    try:
        return np.reshape(mat, (r, c)).tolist()
    except:
        return mat
print(matrixReshape([[1,2,3,4],[5,4,6,9],[5,8,9,4]],2,6))
