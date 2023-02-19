import numpy as np
from vpython import *
A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = graph(title = 'Phonon Dispersion Relation', width=800, height = 300, align='center',\
              background = vec(0.5, 0.5, 0), ytitle = "angular frequency", xtitle = "wavevector")

func = gdots(graph = scene, color = color.red, size = 3)

Unit_K, n = 2 * pi/(N*d), 10

for n in range(1, int(N/2 - 1)): # obtain the angular frequency (omega) for n from 1 to N/2-1.
    rate(1000)
    Wavevector = n * Unit_K
    phase = Wavevector * arange(N) * d
    ball_pos = np.arange(N)*d + A*np.sin(phase)
    ball_orig = np.arange(N)*d # balls' original position
    ball_v = np.zeros(N) # balls' initail velocity == 0
    spring_len = np.ones(N)*d # springs' length
    t, dt = 0, 0.0003 # 當while結束然後再次for時，t又會被重新設定成0! Oh, wow!
    while ball_pos[1] - ball_orig[1] > 0: # 位移大於0 (不要用振幅為A去判斷，是否有到四分之一個週期!)
        t += dt
        spring_len[:-1] = ball_pos[1:] - ball_pos[:-1] # spring.axis = ball[i+1].pos - ball[i].pos
        spring_len[-1] = ball_pos[0] + N*d - ball_pos[-1] # 頭尾相接
        ball_v[1:] += k*(spring_len[1:] - d)/m * dt - k*(spring_len[:-1] - d)/m * dt
        ball_pos += ball_v*dt
    # 當位移從正的變成0時，就跳出while迴圈
    func.plot(pos = (Wavevector, 2* pi/ (t* 4))) # t is period/4 !!!