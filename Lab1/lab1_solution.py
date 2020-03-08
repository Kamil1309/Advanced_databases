import math
import numpy as np
import matplotlib.pyplot as plt

# Ex 1
k = 1240 * math.sqrt(7)
m = 4467
l = complex (0 , 2)
d = k + m 
c = d + l

# Ex 2
print(d)
print( round( d, 3))
print( round( d, 12))

# Ex 3
r = 17
h = 33

P = 2 * math.pi * r**2 + 2 * math.pi * r * h

# Ex 5
x1 = 5 
t = 3
r = 2

B = (x1 + r)/(r * math.sin(2 * x1) + 3.3456) * x1 **(t*r)

# Ex 6
a = math.sqrt(2)
M = np.array([[ a, 1, -a],[ 0, 1, 1],[ -a, a, 1]])

inv_M = np.linalg.inv(M)
trans_M = M.transpose()
determinant = np.linalg.det(M)

print( inv_M )
print( trans_M )
print( determinant )

print("Random matrix 3x3:\n {0}".format(M))
print("Element 1x1: {0}".format(M[0,0]))
print("Element 3x3: {0}".format(M[2,2]))
print("Element 3x2: {0}".format(M[2,1]))

vector1 = M[2,:]
vector2 = M[:,1]

print("Vector 1:\n {0}".format(vector1))
print("Vector 2:\n {0}".format(vector2))

# Ex 7
p = [1, -7, -3, -43, -28, -60]
roots = np.roots(p)
print("Roots :\n {0}".format(roots))

# Ex 8
ar_str1 = np.arange( 0, 2, 0.1 )
ar_str2 = np.linspace(0, 2, num=20, endpoint=False)


print("Arithmetic strings (arange) :\n {0}".format(ar_str1))
print("Arithmetic strings (linspace) :\n {0}".format(ar_str2))

# Ex 9
def f(x):
    return x**3-3*x

def make_plot( f, range):
    x = np.linspace(range[0], range[1])
    y = f(x)   
    plt.plot(x, y)
    plt.title('Example chart')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend('Chart 1')
    plt.show()

# make_plot( f, [-1, 1])
# make_plot( f, [-5, 5])
# make_plot( f, [0, 5])


# Ex 10
m = 2.5
v = 60/3.6

Q_j = m * v**2/2
Q_kcal = m * v**2/2/4.184

print("Heat in joules :\n {0}".format(Q_j))
print("Heat in kcal :\n {0}".format(Q_kcal))

m = 3 

def Q_j(x):
    return m * x**2/(2* 3.6)

#make_plot( Q_j, [0, 200])


x = np.linspace(0, 200)
y = Q_j(x)   
plt.semilogy(x, y)
plt.title('log chart')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('Chart 1')
plt.show()


# Ex 11

#class Quaternion