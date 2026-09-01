#sqrt, exponential, natural log, factorial

#sqrt....................
def sqrt(x, kmax=100):
    x=1.0*x
    if x==0.0:
        return 0.0
    elif  x<0.0:
        print("Error: negative argument to sqrt")
        return -1.0

    s = 1.0
    for k in range(kmax):
        #print("Before %2d iterations, s = %20.15f" % (k, s))
        sold = s
        s = .5*(s + x/s)
        if(abs((s-sold)/x) < 1.0e-14):
            #print("Converged") 
            break
        #print("After %2d iterations, s = %20.15f" % (k+1, s))

    return s

#factorial....................
def factorial(n):
    if n<0:
        print("Error: negative argument to factorial")
        return -1.0
    elif n==0: 
        return 1.0
    s = 1.0
    for k in range(1,n):
        s = s*(k+1)
    #print("after %2d iterations, s = %20.15f" % (n, s))
    return s

e = 2.718281828459045
#exponential....................
def exp(x, kmax):
    x0 = int(round(x))
    z = x-x0
    s = 1.0
    

    for k in range(kmax):
        sold = s
        s = s + z**(k+1)/factorial(k+1)
        #print("after %2d iterations, s = %20.15f" % (k+1, s))
        if(abs((s-sold)/s) < 1.0e-14):
            break

    return s * e**x0
    
#ln....................
def ln(x, kmax):
    if x<=0.0:
       # print("Error: negative argument to ln")
        return -1.0
    elif x==1.0:
        return 0.0

    s = 1.0
    for k in range(kmax):
        sold = s
        s = s - 1 + x*exp(-s, kmax)
        if(abs((s-sold)/s) < 1.0e-14):
            break
    return s
        
        
print("factorial(5) = %20.15f, actual = 120" % factorial(5))
print("sqrt(9.0) = %20.15f, actual = 3" % sqrt(9.0))
print("exp(2.0) = %20.15f, actual = 7.38905609893065" % exp(2.0, 10))
print("ln(8.0) = %20.15f, actual = 2.07944154167983" % ln(8.0, 10))