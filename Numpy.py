# Numpy.py
# First matplotlib basic plot with numpy

# data generation

import numpy as np

# 1. linspace(a, b, total_points)
x = np.linspace(2, 8, 4)
print(x) # 2, 4, 6, 8

# 2. sin(x)
sinx = np.sin(x) # x is considered a radian
print(sinx)

# 3. cos(x)
cosx = np.cos(x)
print(cosx)

# 4. rand: uniform random variables
ur = np.random.rand(4)
print(ur)

# 5. randn: normal random variables
nr = np.random.randn(4)
print(nr)
