import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time 


def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''
     for N in [100, 1000, 10000]:

          print('####################')
          print('N =', N)
          '''' N = size of system'''
          #N = 100
     
          ''' Right hand side'''
          b = np.random.rand(N,1)
          A = np.random.rand(N,N)
          
          print()
          # LU Factorization
          tic = time.time()
          lu, piv = scila.lu_factor(A)
          x_lu = scila.lu_solve([lu, piv], b)
          test = np.matmul(A,x_lu)
          r = la.norm(test-b)
          toc = time.time()
          print('LU Factorization')
          print('error', r)
          time_1 = toc - tic
          print('time LU:', time_1)

          print()
          # Direct Invert
          tic = time.time()
          x = scila.solve(A,b)
          test = np.matmul(A,x)
          r = la.norm(test-b)
          toc - time.time()
          time_2 = toc - tic
          print('Direct Invert')
          print('error', r)
          print('time invert:', time_2)
          print()

          # QR decomposition
          tic = time.time()
          Q, R = scila.qr(A)
          Qb = np.dot(Q.T, b)
          v_qr = scila.solve(R, Qb)
          test_qr = np.matmul(A, v_qr)
          r_ar = la.norm(test_qr - b)
          toc = time.time()
          time_qr = toc - tic

          print('QR decomposition:')
          print('Error:', r_ar)
          print('Time QR:', time_qr)
          print()

          ''' Create an ill-conditioned rectangular matrix '''
          N = 10
          M = 5
          A = create_rect(N,M)     
          b = np.random.rand(N,1)

          # QR  Rect
          tic = time.time()
          Q, R = scila.qr(A)
          Qb = np.dot(Q.T, b)
          v_qr = scila.lstsq(R, Qb)[0]
          test_qr = np.matmul(A, v_qr)
          r_ar = la.norm(test_qr - b)
          toc = time.time()
          time_qr = toc - tic

          print('QR decomposition rectangle:')
          print('Error:', r_ar)
          print('Time QR:', time_qr)
          print()

def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
