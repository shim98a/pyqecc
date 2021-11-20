import numpy as np

def depolarizing_noise(n,p):
    e = np.zeros(2*n,dtype='i1')
    r = np.random.random(n)
    x = np.where(r<=p/3)[0]
    y = np.intersect1d(np.where(r<p)[0], np.where(r>2*p/3)[0])
    z = np.intersect1d(np.where(r<2*p/3)[0], np.where(r>p/3)[0])
    e[x]=1 #Z
    e[n+z]=1 #Z
    e[y] = 1;e[n+y] = 1 #Z
    return e

def amplitude_damping(n,p):
    pass

def one_bit_noise(n,p):
    e = np.zeros(2*n,dtype='i1')
    e[np.random.randint(0,n,1)]=1
    print(e)
    return e