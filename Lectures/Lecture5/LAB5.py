import numpy as np
import numpy.linalg as la

#solve gaussian elimination
def gaussian_elimination(A, b):
    
    num_cols = np.shape(A)[0]
    num_rows = np.shape(A)[1]

    for col in range(num_cols - 1):
        for row in range(col + 1, num_rows):
            multi = (A[row][col] / A[col][col])
            A[row][col:] =  A[row][col:] - multi*A[col][col:]
            b[row] = b[row] - multi*b[col]
       # print(A)
       # print(b)

    x = np.zeros(np.shape(b))
    x[num_rows-1] = b[num_rows-1]/A[num_rows-1][num_cols-1]
    for row in range(num_rows-2,-1,-1):
        x[row] = (b[row] - np.dot(A[row][row+1:], x[row+1:]))/A[row][row]

    #print(x)
    return x
    


#given f(x) at x0, x1, x2, x3
#((x0, f(x0)) , (x1, f(x1)) , ......)
#find a polynomial of degree = 3  -> P(x2) = f(x2)
#f(x) = cos(x) at (-.1, cos(-.1))
def cubic_interpolate(x, y):
    matrix = np.array([[x[0]**3, x[0]**2, x[0], 1], [x[1]**3, x[1]**2, x[1], 1], [x[2]**3, x[2]**2, x[2], 1], [x[3]**3, x[3]**2, x[3], 1]], dtype=float)
    
    return(gaussian_elimination(matrix, y))

#4x4
matrix = np.array([[1, 1, 1, 1], [1, 2, 4, 8], [1, 3, 9, 27], [1, 4, 16, 64]], dtype=float)
b = np.array([1, 2, 3, 4], dtype=float)
print("My solution:", gaussian_elimination(matrix, b))
print("Solution using NumPy:", la.solve(matrix, b))

#cubic interpolation
x = np.array([-0.1, -0.02, 0.02, 0.1], dtype=float)
y = np.array([np.cos(-0.1), np.cos(0.02), np.cos(0.02), np.cos(0.1)], dtype=float)

print("Cubic interpolate:", cubic_interpolate(x, y))

