import math
import numpy as np
import matplotlib.pyplot as plt

#Ex 1
k = 1240 * math.sqrt(7)
m = 4467
l = complex (0 , 2)
d = k + m 
c = d + l

#Ex 2
print(d)
print( round( d, 3))
print( round( d, 20))

#Ex 3
r = 17
h = 33

P = 2 * math.pi * r**2 + 2 * math.pi * r * h
print(P)

#Ex 4
"""
Multiline comments
"""
#line comment

# Ex 5
x1 = 5 
t = 3
r = 2

B = (x1 + r)/(r * math.sin(2 * x1) + 3.3456) * x1 **(t*r)
print(B)

# Ex 6
a = math.sqrt(2)
M = np.array([[ a, 1, -a],[ 0, 1, 1],[ -a, a, 1]])

inv_M = np.linalg.inv(M)
trans_M = M.transpose()
determinant = np.linalg.det(M)

print( inv_M )
print( trans_M )
print( determinant )

print("Element 1x1: {0}".format(M[0,0]))
print("Element 3x3: {0}".format(M[2,2]))
print("Element 3x2: {0}".format(M[2,1]))

vector1 = M[2,:]
vector2 = M[:,1]

print("Vector 1:\n {0}".format(vector1))
print("Vector 2:\n {0}".format(vector2))

#Ex 7
p = [1, -7, -3, -43, -28, -60]
roots = np.roots(p)
print("Roots :\n {0}".format(roots))

#Ex 8
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

make_plot( f, [-1, 1])
make_plot( f, [-5, 5])
make_plot( f, [0, 5])


#Ex 10

m = 2.5
v = 60/3.6

Q_j = m * v**2/2
Q_kcal = m * v**2/2/4.184

print("Heat in joules :\n {0}".format(Q_j))
print("Heat in kcal :\n {0}".format(Q_kcal))

m = 3 

def f_Q_j(x):
    return m * x**2/2

make_plot( f_Q_j, [0, 200/3.6])

x = np.linspace(0, 200)
y = f_Q_j(x)   
plt.semilogy(x, y)
plt.title('log chart')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('Chart 1')
plt.show()


#Ex 11

class Quaternion:
    def __init__(self, a, b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        
    def conjugate(self):
        return Quaternion( self.__a, -self.__b, -self.__c, -self.__d )
            
    def normalise(self):
        d = math.sqrt(self.__a ** 2 + self.__b ** 2 + self.__c ** 2 + self.__d ** 2)
        return Quaternion( self.__a/d, self.__b/d, self.__c/d, self.__d/d )
    
    def __str__(self):
        return '{0} + {1}i + {2}j + {3}k'.format(self.__a, self.__b, self.__c, self.__d)
    
    def __add__(self, another_q):
        return Quaternion( self.__a + another_q.__a,\
                           self.__b + another_q.__b,\
                           self.__c + another_q.__c,\
                           self.__d + another_q.__d)

    def __sub__(self, another_q):
        return Quaternion( self.__a - another_q.__a,\
                           self.__b - another_q.__b,\
                           self.__c - another_q.__c,\
                           self.__d - another_q.__d)
    
    def __mul__(self, another_q):
        if type(another_q) == Quaternion:
            return Quaternion( self.__a * another_q.__a - self.__b * another_q.__b - self.__c * another_q.__c - self.__d * another_q.__d,\
                               self.__a * another_q.__b + self.__b * another_q.__a + self.__c * another_q.__d - self.__d * another_q.__c,\
                               self.__a * another_q.__c - self.__b * another_q.__d + self.__c * another_q.__a + self.__d * another_q.__b,\
                               self.__a * another_q.__d + self.__b * another_q.__c - self.__c * another_q.__b + self.__d * another_q.__a)
        elif type(another_q) == int:
            return Quaternion( self.__a * another_q, self.__b * another_q, self.__c * another_q, self.__d * another_q  )
        
    def __truediv__(self, another_q):
        if type(another_q) == Quaternion:
            t0 = (self.__a * another_q.__a + self.__b * another_q.__b + self.__c * another_q.__c + self.__d * another_q.__d)/  \
                    ( another_q.__a ** 2 + another_q.__b ** 2 + another_q.__c ** 2 + another_q.__d ** 2)
            t1 = (self.__b * another_q.__a - self.__a * another_q.__b - self.__d * another_q.__c + self.__c * another_q.__d)/  \
                    ( another_q.__a ** 2 + another_q.__b ** 2 + another_q.__c ** 2 + another_q.__d ** 2)
            t2 = (self.__c * another_q.__a + self.__d * another_q.__b - self.__a * another_q.__c - self.__b * another_q.__d)/  \
                    ( another_q.__a ** 2 + another_q.__b ** 2 + another_q.__c ** 2 + another_q.__d ** 2)
            t3 = (self.__d * another_q.__a - self.__c * another_q.__b + self.__b * another_q.__c - self.__a * another_q.__d)/  \
                    ( another_q.__a ** 2 + another_q.__b ** 2 + another_q.__c ** 2 + another_q.__d ** 2)
            return Quaternion( t0, t1, t2, t3 )
        elif type(another_q) == int:
            t0 = self.__a/another_q
            t1 = self.__b/another_q
            t2 = self.__c/another_q
            t3 = self.__d/another_q
            return Quaternion( t0, t1, t2, t3 )
    
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, a):
        self.__a = a
        
    @property
    def b(self):
        return self.__b
    @a.setter
    def b(self, b):
        self.__b = b
        
    @property
    def c(self):
        return self.__c
    @a.setter
    def c(self, c):
        self.__c = c
        
    @property
    def d(self):
        return self.__d
    @a.setter
    def d(self, d):
        self.__d = d

q1 = Quaternion( 5, 4, 3, -6)
q2 = Quaternion( 12, 4, 2, -12)
print(q1)
print(q2)
print(q1 + q2) 
print(q1 - q2) 
print(q1 * q2) 
print(q2 * q1) 
print(q1 * 5) 
print(q2 * 1) 
print(q1 / q2) 
print(q2 / q1) 
print(q1 / 5) 
print(q2 / 3) 
print(q1.conjugate())
print(q2.conjugate())
print(q1.normalise())
print(q2.normalise())