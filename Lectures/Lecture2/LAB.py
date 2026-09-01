#from math import sqrt

#s = sqrt(2.0)

def sqrt(x, kmax=100):
    x=1.0*x
    if x==0.0:
        return 0.0
    elif  x<0.0:
        print("Error: negative argument to sqrt")
        return -1.0

    s = 1.0
    for k in range(kmax):
        print("Before %2d iterations, s = %20.15f" % (k, s))
        sold = s
        s = .5*(s + x/s)
        if(abs((s-sold)/x) < 1.0e-14):
            #print("Converged") 
            break
        print("After %2d iterations, s = %20.15f" % (k+1, s))

    return s

s = sqrt(9.0)