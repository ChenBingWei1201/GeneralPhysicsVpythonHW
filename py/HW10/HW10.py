from vpython import*
import numpy as np

# constants
fd = 120 # 120 (Hz)
w = 2* np.pi* fd # omega(rad/s)
T = 1/fd 
R, L, C = 30, 200E-3, 20E-6 # 30 (ohm), 200 (mH), 20 (μF)
v, v_c, v_l = 0, 0, 0
i = 0
Engery = 0

pre_i = 0
pre2_i = 0
mCount = 0 # maximum count
nineth_i_max_T = 0
nineth_i_max_Mag = 0

E_10percent_t = 0
E_10percent_Mag = 0

# phasor 
Vs = 36 # voltage source's magnitude
theta_V = 0 # phase of source
Xc = -1/(w*C)
Xl = w*L
X = Xc + Xl # total reactance
M = (R**2 + X**2)**(1/2) # magnitude
theta_Z = np.arctan(X/R) # phase
I = Vs/M # Magnitude of i
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
    if t < 12*T:
        v = Vs*np.sin(w*t)
    else:
        v = 0
    
    v_l = v - v_c - i*R
    i += 1/L*v_l*dt
    v_c += 1/C*i*dt
    Engery = 1/2*C*(v_c**2) + 1/2*L*(i**2)
    
    if mCount < 9:
        if pre_i-i > 0 and pre_i - pre2_i > 0:
            mCount += 1
           
        if mCount == 9:
            nineth_i_max_Mag = pre_i 
            nineth_i_max_T = (t-dt)/T
            print("Magnitude of i")
            print("Numerical:", nineth_i_max_Mag)
            print("Theoretical:", I)

            print("Phase const. of i")
            print("Numerical:", 2*np.pi*(floor(nineth_i_max_T) + 0.25 - nineth_i_max_T))
            print("Theoretical:", theta_I)
            
    pre2_i = pre_i
    pre_i = i
    
    if t >= 12*T:
        if E_10percent_Mag == 0:
            E_10percent_Mag = Engery/10
        if Engery <= E_10percent_Mag and E_10percent_t == 0:
            E_10percent_t = t
            print("the energy decays to 0.1E(t = 12T) at t = ", t/T, "T.")            
        
    
    v_t.plot(pos = (t/T, v/100))
    i_t.plot(pos = (t/T, i))
    E_t.plot(pos = (t/T, Engery))
    
        