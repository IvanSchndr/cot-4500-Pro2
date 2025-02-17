import numpy as np

def neville(x_points, y_points, x):
    n = len(x_points)
    p = np.zeros((n, n))

    for i in range(n):
        p[i][0] = y_points[i]
    
    # Calculate interpolation values
    for i in range(1, n):
        for j in range(1, i + 1):
            t1 = (x - x_points[i-j]) * p[i][j-1]
            t2 = (x - x_points[i]) * p[i-1][j-1]
            p[i][j] = (t1 - t2) / (x_points[i] - x_points[i-j])
            

    print(p[n-1][n-1], "\n")

def newton(x_points, y_points, x):
    n = len(x_points)
    p = np.zeros((n,n))
    for i in range(n):
        p[i][0] = y_points[i]

    for j in range(1, n):
        for i in range(j, n):
            p[i][j] = (p[i][j-1] - p[i-1][j-1])/ (x_points[i] - x_points[i-j])
            

    for i in range(1,n):
        print(p[i][i])
    
    fin = p[0][0]
    for i in range(n-1):
        mult = p[i+1][i+1];
        for j in range(i+1):
            mult = mult*(x-x_points[j])

        fin = fin + mult
    print("")
    print( fin, "\n")

def herm(x_points, y_points, dx_points):
    n = len(x_points)
    p = np.zeros((n*2,n*2+1))
    for i in range(len(x_points)):
        p[i*2][0] = x_points[i]
        p[i*2+1][0] = x_points[i]
        p[i*2][1] = y_points[i]
        p[i*2+1][1] = y_points[i]

    
    
    for i in range(n):
        if(i != 0):
            p[i*2][2] = (p[i*2][1] - p[i*2-1][1])/ (x_points[i] - x_points[i-1])
        p[i*2+1][2] = dx_points[i]
    
    
    
    
    for j in range(3, n*2):
        for i in range(j-1, n*2):
            p[i][j] = (p[i][j-1] - p[i-1][j-1])/ (p[i][0] - p[i-j+1][0])

    for i in range(n*2):
        print("[", end="")
        for j in range(n*2-1):
            print( " ","{:e}".format(p[i][j]), end = "")
        print("]")

    
def spline(x_points, y_points):
    n = len(x_points) - 1
    h = np.diff(x_points)


    A = np.zeros((n+1, n+1))
    A[0][0] = 1
    A[n][n] = 1

    for i in range(1, n):
        A[i][i-1] = h[i-1]
        A[i][i] = 2*(h[i-1] + h[i])
        A[i][i+1] = h[i]

    
    b = np.zeros(n+1)
    for i in range(1, n):
        b[i] = 3*((y_points[i+1] - y_points[i])/h[i] - (y_points[i] - y_points[i-1])/h[i-1])

    x = np.linalg.solve(A, b)

    print("")
    print(A)
    print(b)
    print(x)


