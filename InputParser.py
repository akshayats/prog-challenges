import numpy as np


ip = [[6, 2], [0, 0, 0], [0, 3, 3,], [-2, 5, 5], [0, 7, 7], [2, 5, 9], [0, 3, 11]]

n = None
dt = None
for i,  l in enumerate(ip):
    if not (n or dt):
        n, dt = l
        print(n)
        print(dt)
        print(i)
        p = np.zeros((n, 2))
        t = np.zeros((n, 1))
    else:
        p[i-1, :] = l[0:2]
        t[i-1] = l[2]






