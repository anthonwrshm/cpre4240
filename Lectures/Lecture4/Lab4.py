start = 1


def sqrt(x, initial_guess, kmax, tol):
    x = x*1.0
    if x < 0:
        print("error: negative argument to sqrt")
        return
    if x== 0:
        return 0.0

    s = initial_guess
    for k in range(kmax):
        sold = s
        #s equation "s - func(s)/derFunc(s)"
        s = .5*(s+x/s)
        if abs(s-sold)/abs(x) < tol:
            break
        
    return s

def factorial(n):
    if n < 0:
        print("error: negative argument to factorial")
        return
    if n == 0:
        return 1
    return n * factorial(n-1)

def expo(x, initial, kmax, tol):
    s = initial
    if x == 0:
        return 1.0

    for k in range(1, kmax):
        sold = s
        s = s + (x**k)/factorial(k)
        if(s != 0):
             if abs(s-sold)/abs(s) < tol:
                 break

    return s

def ln(x, kmax, tol):
    if x<=0.0:
        print("error: non-positive argument to ln")
        return -1.0
    elif x==1.0:
        return 0.0

    s = 1.0
    for k in range(kmax):
        sold = s
        s = s - 1 + x*expo(-s, 1.0, kmax, tol)
        if(s != 0):
            if(abs((s-sold)/abs(s)) < tol):
                 break
    return s

time = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def EulersForwardMethod(p0, t, totSteps, r, kcap):
    #dp(t)/dt = f(t, P(t)), t> 0
    #P(0) = p0
    #tk = k*changeinT
    #changeinT = time step size
    #pk = P(tk)
    dt = t / totSteps
    prev = p0
    for i  in range(totSteps):
        prev = prev + r * dt * prev *(1 - prev/kcap)

    return prev

def logGrowthFunc(r, kcap, Pinitial, t):

    pk = kcap / (1 + ((kcap - Pinitial)/Pinitial)*expo(-r*t, 1.0, 100, 1.0e-14))

    return pk

def halfExpected(r, kcap, Pinitial):
    t = ln(Pinitial/(kcap - Pinitial), 100, 1.0e-14)/-r
    return t

j = 0
while j < len(time):
    print(" ")
    print("Logistic Growth Model Population: " + str(logGrowthFunc(0.5, 100, 10, time[j]))+ " at time " + str(time[j]))
    print("Euler's Forward Method Population: " + str(EulersForwardMethod(10, time[j], 20, 0.5, 100)) + " at time " + str(time[j]))
    j += 1

print("Time to reach half of carrying capacity: " + str(halfExpected(0.5, 100, 10)))

print("sqrt(9.0) = %20.15f, actual = 3" % sqrt(9.0, 1.0, 100, 1.0e-14))
print("exp(2.0) = %20.15f, actual = 7.38905609893065" % expo(2.0, 1.0, 100, 1.0e-14))
print("ln(8.0) = %20.15f, actual = 2.07944154167983" % ln(8.0, 100, 1.0e-14))
print("factorial(5) = %20.15f, actual = 120" % factorial(5))

