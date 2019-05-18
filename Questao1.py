#Autor: Pablo Gullith
#Bibliotecas
from numpy import empty, zeros, sin
from banded import banded
from pylab import plot,show
import vpython as vp
import time as tm
#Constantes
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k-m*omega*omega

A = empty([3,N],float)

for i in range(N):

    A[0,i] = -k

    A[1,i] = alpha

    A[2,i] = -k

A[1,0] = alpha - k

A[1,N-1] = alpha - k


v = zeros(N,float)

v[0] = C

x = banded(A,v,1,1)

s = []
delta = 2
for i in range(len(x)):
	p = (i - len(x)/2)*delta
	s.append(vp.sphere(pos = vp.vector(p, 0, 0), radius = 0.3))
t0 = tm.time()
while True:
	t = tm.time()
	for i in range(len(s)):
		p = (i - len(s)/2)*delta + x[i]*sin(omega*(t - t0))
		s[i].pos = vp.vector(p, 0, 0)
	tm.sleep(0.05)


