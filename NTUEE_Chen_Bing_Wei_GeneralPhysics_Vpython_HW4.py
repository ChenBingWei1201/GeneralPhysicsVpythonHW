from vpython import*
import numpy as np


N = 50          # 50 balls
A = 0.10        # Amplitude = 0.10 (m)
m = 0.1         # mass of each ball = 0.1 (kg)  
k = 10.0        # force constant of each spring = 10.0 (N/m)
d = 0.4         # length between two adjacent balls = 0.4 (m)

# some setting for illustrating the graph
scene = graph(title = 'Phonon Dispersion Relation', width=800, height = 300, align='center',\
              background = vec(0.5, 0.5, 0))
func1 = gdots(graph = scene, color = color.red, width = 4)

Unit_K, n = 2 * pi/(N*d), 10
for n in range(1, int(N/2-1)):
    rate(1000)
    Wavevector = n * Unit_K  
    phase = Wavevector * arange(N) * d      # sine function
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
    t, dt = 0, 3E-4
    
    while ball_pos[1] - ball_orig[1] > 0:
        
        t += dt
        spring_len[:-1] = ball_pos[1:N] - ball_pos[:N-1]
        spring_len[-1] = ball_pos[0] + N*d - ball_pos[-1]
        ball_v[1:] += k*(spring_len[1:]-d)/m*dt - k*(spring_len[:N-1]-d)/m*dt
        ball_pos += ball_v*dt
    
    func1.plot(pos = (Wavevector, 2* pi /(t * 4)))  # illustrate the graph!
