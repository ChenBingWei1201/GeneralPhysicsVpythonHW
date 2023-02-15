import math
# 1. range(). Notice the number in range should be integer (int)
L1 = range(5) # list(L) = [0, 1, 2, 3, 4].
L2 = range(4, 9) # list(L) = [4, 5, 6, 7, 8]
L3 = range(1, 6, 2) # list(L) = [1, 3, 5] 1 to 6 every other 2 numbers
print(list(L1), list(L2), list(L3))

# 2. list representation. Sometimes we want to generate a list with some conditions, e.g.
L4 = [i**2 for i in range(5)] # = [0, 1, 4, 9, 16]
L5 = [0.1*i*math.pi for i in range(-3, 3)] # = [-0.3*pi, -0.2*pi, -0.1*pi, 0, 0.1*pi, 0.2*pi]
L6 = [i**2 for i in range (5) if i != 3] # = [0, 1, 4, 16]
print(list(L4), list(L5), list(L6))

# 3. List representation can be used in a nested structure, or for dictionary or tuple. e.g.
L = [i*10 + j for i in range(3) for j in range(5) ] # = [0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24]
D = {i:i**2 for i in [0, 1, 2]} # = {0:0, 1:1, 2:4}
print(list(L), D)