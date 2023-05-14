import numpy as np

R1, R2 = 0.12, 0.06 # 12, 6 (cm)
z1, z2 = 0, 0.10 
N = 1 # one loop
i = 1 # 1 (A)
pi = np.pi

class Loop:
    def __init__(self, R, z):
        self.R = R
        self.z = z
        self.dp = self.R/1000
        self.dt = 2*pi/1000

    def B_feild(self, L, p):
        A = np.arange(0, 2*pi, L.dt)
        ds = np.array([-L.R*np.sin(A), L.R*np.cos(A), 0*A])
        ds = np.transpose(ds)
        r = np.array([p -L.R*np.cos(A), -L.R*np.sin(A), (self.z- L.z) + 0*A])   
        r = np.transpose(r)
    
        g = np.cross(ds, r) # function g
    
        for i in range(1000):
            dis = np.dot(r[i], r[i])
            g[i] = g[i] / (dis**(3/2))
        g = np.transpose(g)
    
        B = np.sum(g[2])*(10**(-7))*self.dt
        return B

    def mInductance(self, L):
        p = 0
        Flux = 0
        while p <= self.R:
            Flux += self.B_feild(L, p)*p*self.dp
            p += self.dp
        return N*2*pi*Flux/i

L1 = Loop(R = R1, z = z1)
L2 = Loop(R = R2, z = z2)

M12 = L2.mInductance(L1)
M21 = L1.mInductance(L2)

print("M12 =", M12, "H")
print("M21 =", M21, "H")