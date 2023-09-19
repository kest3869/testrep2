import numpy as np
import matplotlib.pyplot as plt

# Exercises: The Basics 

# 1. 
x = np.linspace(0, 9, num=10)
y = np.arange(0, 10, 1)
print(len(x)==len(y))

# 2.
print(x[:3])

# 3.
print("The first three entries of x are", x[:3])

# 4. 
w = 10**(-np.linspace(1,10,10))
x = np.arange(1, len(w) + 1)
plt.semilogy(x, w)
plt.xlabel('x')
plt.ylabel('w')
plt.title('Semilog plot of x vs w')
plt.close()

# 5. 
s = 3 * w
w = 10**(-np.linspace(1,10,10))
x = np.arange(1, len(w) + 1)
plt.semilogy(x, w)
plt.semilogy(x, s)
plt.xlabel('x')
plt.ylabel('w')
plt.title('Semilog plot of x vs w and s')

# 6. 
plt.savefig('semilog.jpg')
plt.close()

# Exercises using the d
# I learned how to use lambda notation to define one line functions in python 
