from vpython import*
import numpy as np

# constants
fd = 120 # 120 (Hz)
w = 2* np.pi* fd # omega(rad/s)
T = 1/fd 
R, L, C = 30, 200E-3, 20E-6 # 30 (ohm), 200 (mH), 20 (μF)
v, i, Engery = 0, 0, 0

# phasor 
Vs = 36 # voltage source's magnitude
theta_V = -np.pi/2 # phase of source
Xc = -1/(w*C)
Xl = w*L
X = Xc + Xl # total reactance
M = (R**2 + X**2)**(1/2) # magnitude
theta_Z = np.arctan(X/R) # phase
I = Vs/M
theta_I = theta_V - theta_Z

t=0
dt = 1.0/(fd * 5000)# 5000 simulation points per cycle

scene1 = graph(align = 'left', xtitle='t', ytitle='i (A) blue, v (100V) red,', background=vector(0.2, 0.6, 0.2))
scene2 = graph(align = 'left', xtitle='t', ytitle='Energy (J)', background=vector(0.2, 0.6, 0.2))
i_t = gcurve(color=color.blue, graph = scene1) # total current
v_t = gcurve(color=color.red, graph = scene1) # sorce voltage
E_t = gcurve(color=color.red, graph = scene2)  # total energy

while t < 20*T:
    rate(5000)
    t += dt
    v = Vs*np.sin(w*t)
    i = I*np.cos(w*t + theta_I)
    Engery = 1/2*Vs*np.sin(w*t)*I*np.cos(w*t + theta_I)
    
    if t < 12*T:
        v_t.plot(pos = (t, v/100))
        i_t.plot(pos = (t, i))
        E_t.plot(pos = (t, Engery))
    else:
        v_t.plot(pos=(t, 0))
        i_t.plot(pos = (t, 0))
        