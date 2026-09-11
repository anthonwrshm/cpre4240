#main functionality
#file mylinalg.py

#def GE(A,b)
#if__name__ == "__main__":

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

#solve gaussian elimination
def gaussian_elimination(A, b):
    
    num_cols = np.shape(A)[0]
    num_rows = np.shape(A)[1]

    for col in range(num_cols - 1):
        for row in range(col + 1, num_rows):
            multi = (A[row][col] / A[col][col])
            A[row][col:] =  A[row][col:] - multi*A[col][col:]
            b[row] = b[row] - multi*b[col]

    x = np.zeros(np.shape(b))
    x[num_rows-1] = b[num_rows-1]/A[num_rows-1][num_cols-1]
    for row in range(num_rows-2,-1,-1):
        x[row] = (b[row] - np.dot(A[row][row+1:], x[row+1:]))/A[row][row]

    #print(x)
    return x
    

def cubic_interpolate(x, y):
    matrix = np.array([[x[0]**3, x[0]**2, x[0], 1], [x[1]**3, x[1]**2, x[1], 1], [x[2]**3, x[2]**2, x[2], 1], [x[3]**3, x[3]**2, x[3], 1]], dtype=float)
    
    return(gaussian_elimination(matrix, y))

def leastSquares(x, y, m, n):
    m = len(x)
    if len(y) != m:
        print ("Error")
        return
    if m < n+1:
        print ("Error")
        return

    V = np.zeros((m, n+1), dtype=float)
    for k in range(n+1):
        V[:, k] = x**(n-k)

    a = V.T @ V
    b = V.T @ y

    return gaussian_elimination(a, b)

if __name__ == '__main__':


    #print("test")
    #npts = 4
    #xpts = np.array([-.1, -.02, .02, .1], dtype=float)
    #ypts = np.cos(xpts)

    #A = np.ones((npts, npts), dtype=float)
    #A[:, 0] = xpts**3
    #A[:, 1] = xpts**2
    #A[:, 2] = xpts

    #b = np.ones((npts), dtype=float)
    #b = np.cos(xpts)

    #x = gaussian_elimination(A, b)

    m = 51
    n = 5

    xgrid = np.linspace(-np.pi, np.pi, m)
    f = np.cos(xgrid)
    p = np.zeros(m)

    coefficients = leastSquares(xgrid, f, m, n)
    p = np.zeros(m)
    for k in range(n + 1):
        p = p + xgrid**(n - k) * coefficients[k]

    plt.plot(xgrid, f, 'r-', label='cos(x)', linewidth=4)
    plt.plot(xgrid, p, 'k--', label='cubic interpolation', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()
    