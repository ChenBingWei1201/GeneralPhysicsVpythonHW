import numpy as np
from vpython import *
A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = canvas(title='Spring Wave', width=800, height=300,
               background=vec(0.5, 0.5, 0), center=vec((N-1)*d/2, 0, 0))
# balls = [sphere(radius=size, color=color.red, pos=vector(
#     i*d, 0, 0), v=vector(0, 0, 0)) for i in range(N)]  # 3
# springs = [helix(radius=size/2.0, thickness=d/15.0, pos=vector(i*d,
#                  0, 0), axis=vector(d, 0, 0)) for i in range(N-1)]  # 3
# 1
c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)
# 5
# ball_pos = np.arange(N)*d  # 這五十顆球的瞬時位置 arange 0*d --> 49*d
# ball_orig = np.arange(N)*d  # 這五十顆球的沒受到外力時的位置 arange 0*d --> 49*d
# ball_v = np.zeros(N)       # 這五十顆球的瞬時速度,全部放成0的array
# spring_len = np.ones(N)*d  # 這五十顆球的彈簧身長量,全部放成1* d的array

Unit_K, n = 2 * pi/(N*d), 10
Wavevector = n * Unit_K
phase = Wavevector * arange(N) * d
ball_pos = np.arange(N)*d + A*np.sin(phase)
ball_orig = np.arange(N)*d
ball_v = np.zeros(N)
spring_len = np.ones(N)*d

t, dt = 0, 0.001
while True:
    rate(1000)
    t += dt
    # ball_pos[0] = A * sin(omega * t)  # 4
    spring_len[:-1] = ball_pos[1:] - ball_pos[:-1] # spring.axis = ball[i+1].pos + ball[i].pos
    spring_len[-1] = ball_pos[0] + N*d - ball_pos[-1]
    ball_v[1:] += k*(spring_len[1:] - d)/m * dt - \
        k*(spring_len[0:-1] - d)/m * dt  # 6
    ball_v[0] = k*(spring_len[0] - d)/m * dt - \
        k*(spring_len[N-1] - d)/m * dt  # the last one connect to the zeroth one
    ball_pos += ball_v*dt
#    for i in range(N): balls[i].pos.x = ball_pos[i] #3
#    for i in range(N-1): #3
#       springs[i].pos = balls[i].pos #3
#       springs[i].axis = balls[i+1].pos - balls[i].pos #3
    # 2
    ball_disp = ball_pos - ball_orig  # 球的位移 = 球的瞬時位置減球原來的位置
    for i in range(N):
        c.modify(i, y=ball_disp[i]*4+1)  # 改變第i顆球的y座標
                   
