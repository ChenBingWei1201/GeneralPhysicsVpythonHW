from numpy import *
from vpython import *
epsilon = 8.854E-12
N = 101  # N*N dots on x-y plane
h = 1E-2/(N-1)  # distance between two adjacent dots
# The distance between the plates is d
# the width of both plates is L
L, d = 4E-3, 1E-3
V0 = 200  # delta V (voltage difference)


def solve_laplacian(u, u_cond, h, Niter=5000):  # Nth iteration
    V = array(u)  # V is a deep copy of u
    for i in range(Niter):
        V[u_cond] = u[u_cond]  # refresh the voltage of two plates
        # V(x, y) = (1/4)*[V(x-h, y) + V(x+h, y) + V(x, y-h) + V(x, y+h)]
        V[1:-1, 1:-1] = (1/4)*(V[:-2, 1:-1] + V[2:, 1:-1] + V[1:-1, :-2] + V[1:-1, 2:])
    return V


def get_field(V, h):
    # gradient will return two N*N "delta V" matrices
    Ex, Ey = gradient(V)  # delta Vx and Vy
    # get true Ex = -dVx/dx, Ey = -dVy/dy (E = - divergence of V)
    Ex, Ey = -Ex/h, -Ey/h
    return Ex, Ey


# N*N points on x-y plane
# u is a N*N matrix, storing the voltage of each point
u = zeros([N, N])
# two parallel plates have been given +100 and -100 voltages respectively.
u[int(N/2)-int(L/h/2.0):int(N/2)+int(L/h/2.0), int(N/2) - int(d/h/2.0)] = -V0/2  # -100(V)
u[int(N/2)-int(L/h/2.0):int(N/2)+int(L/h/2.0), int(N/2) + int(d/h/2.0)] = V0/2  # 100(V)
# u_cond is a N*N matrix, storing a bool:"Whether the point's voltage == 0"
u_cond = not_equal(u, 0)  # u != 0 -> true / u == 0 -> falses

# return the N*N voltage matrix
V = solve_laplacian(u, u_cond, h)

scene = canvas(title='non-ideal capacitor', height=1000, width=1000, center=vec(N*h/2, N*h/2, 0))
scene.lights = []
scene.ambient = color.gray(0.99)
box(pos=vec(N*h/2, N*h/2 - d/2 - h, 0), length=L, height=h/5, width=h)
box(pos=vec(N*h/2, N*h/2 + d/2 - h, 0), length=L, height=h/5, width=h)

for i in range(N):
    for j in range(N):
        point = box(pos=vec(i*h, j*h, 0), length=h, height=h, width=h/10,
                    color=vec((V[i, j]+100)/200, (100-V[i, j])/200, 0.0))  # colors have somthing todo with volatges
# return the N*N matrix Ex, Ey
# V's distribution and distance between two adjacent points
Ex, Ey = get_field(V, h)

# drawing settings for tiny arrows
for i in range(0, N):
    for j in range(0, N):
        ar = arrow(pos=vec(i*h, j*h, h/10),
                   axis=vec(Ex[i, j]/2E9, Ey[i, j]/2E9, 0), shaftwidth=h/6.0, color=color.black)

# find Q, find C_nonideal = Q/(delta V)
# Compare C_nonideal to C_ideal

# close integral E dot dA = Q / epsilon
# => Q = close integral E dot dA * epsilon

dA = h*1
tEx = 0  # total Ex
tEy = 0  # total Ey
for i in range(25, 76):
    tEy = tEy - Ey[i][int(N/2)] + Ey[i][int(N/2) + int(d/h)]
for j in range(int(N/2), int(N/2) + int(d/h) + 1):
    tEx = tEx - Ex[25][j] + Ex[76][j]

Q_enclosed = (tEx + tEy) * dA * epsilon
C_nonideal = Q_enclosed / V0
C_ideal = L*epsilon/d
print("the nonideal capacitor is ", C_nonideal)
print("the error percentage is ", ((C_nonideal - C_ideal) / (C_ideal))*100, "%")
