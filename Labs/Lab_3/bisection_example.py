# import libraries
import numpy as np

def driver():

    f = lambda x: np.sin(x)
    a = 0.5
    b = 0.75* np.pi

    tol = 1e-5

    [astar,ier] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))

    print("ANSWERS TO PROMPTS BELOW")
    print()
    print("PROBLEM 1:")
    print("Somewhat suprisingly it is failing to find the root at 0 but it is successfully finding the root at 1")
    print("It is probably not possible to find this root using this technique since there is not a change of sign at that point.")
    print()
    print("PROBLEM 2:")
    print("In each case it found the leftmost root and none of the others. Further, it did not find a root in the last case")
    print("In an ideal case, you would want a something that found all of the roots")
    print()

# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 
    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1

    astar = d
    ier = 0
    return [astar, ier]
      
driver()               
