import matplotlib.pyplot as plt
from random import random
import sys
import numpy as np

def iters_func(r, x0, n):
    if n == 0:
        return x0
    else:
        x0 = (r * x0) * (1 - x0)
        return iters_func(r, x0, n - 1)


# PODPUNKT A

# z = []
# xs = []
# c = ['red','blue','green','yellow','pink']
# for y in range(5):
# z.append([])
#  xs.append([])
#  x0 = random()
#  for x in range(100):
#      z[y].append(iters_func(1.1, x0, x))
#      xs[y].append(x)


# for x in range(5):
#  plt.scatter(xs[x], z[x], c=c[x])


# plt.show()

# PODPUNKT B

def sub_b(x0, w, c, r):
    t = 1
    while True:
        x0_result = iters_func(r, x0, t)
        if w - c <= x0_result and w + c >= x0_result:
            return t
        t += 1


# print(sub_b(0.5, 0.090909091, 1/(10**9), 1.1))


# PODPUNKT C

# z = []
# xs = []
# c = ['red','blue','green','yellow','pink']
# for y in range(5):
#   z.append([])
#   xs.append([])
#   x0 = random()
#   for x in range(100):
#       z[y].append(iters_func(3, x0, x))
#       xs[y].append(x)
#
#
# for x in range(5):
#   plt.scatter(xs[x], z[x], c=c[x])
#
# plt.show()

# PODPUNKT D
sys.setrecursionlimit(10000)
# z = []
# xs = []
# c = ['red', 'blue', 'green', 'yellow', 'pink']
# for y in range(2):
#     z.append([])
#     xs.append([])
#     x0 = random()
#     for x in range(10000):
#         z[y].append(iters_func(3.9, x0, x))
#         xs[y].append(x)
#
# for x in range(2):
#     plt.scatter(xs[x], z[x], c=c[x])
#
# plt.show()

#podpunkt E

def iters_func2(r, x0, n_min, n_max):
    if n_min == 0:
        return x0
    else:
        x0 = (r * x0) * (1 - x0)
        return iters_func(r, x0, n_max - 1)


z = []
r = np.linspace(2.8, 4, 100)
c = ['red', 'blue', 'green', 'yellow', 'pink']
id = 0
for x in r:
    z.append(iters_func(x, 0.4, 300))
    id += 1

for x in range(len(z)):
    plt.scatter(r, z, c='r')

plt.show()