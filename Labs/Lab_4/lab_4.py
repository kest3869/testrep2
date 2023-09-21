
# import libraries
import numpy as np
import matplotlib.pyplot as plt
    
def driver():

# test functions 
     f1 = lambda x: (10/(x+4))**0.5
     Nmax = 100
     tol = 1e-10
     x_vals = []
     p_true = 1.3652300134140976
    
# test f1 '''
     x0 = 1.5
     [xstar,ier, x_vals] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('It takes', len(x_vals) - 1, 'iteration to converge')
     plot_con(x_vals, p_true)
     print("The convergence appears to be quadratic.")
     print("The value of the convergence constant is about:", calc_con(x_vals, p_true))

# function to make a plot of convergence
def plot_con(x_vals, p_true):
    x = range(len(x_vals))
    y = []
    for val in x_vals:
        y.append(abs(val - p_true))
    plt.plot(x, y)
    plt.title('Number of Iterations vs Distance from Ground Truth')
    plt.savefig('fig1.png')
    #plt.show()
    return

# calculates lambda 
def lamb(p_n, p_n1, p_true, alpha):
    l = abs(p_n1 - p_true)/abs(p_n - p_true)**alpha
    return l

# calculates the convergence constance 
def calc_con(x_vals, p_true):
    lambdas = []
    for i in range(len(x_vals) - 1):
        lambdas.append(lamb(x_vals[i], x_vals[i+1], p_true, 2))
    return np.mean(lambdas)
    
# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    x_vals = []
    x_vals.append(x0)
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       x_vals.append(x1)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, np.array(x_vals)]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, np.array(x_vals)]
    
driver()