from vpython import *
import math
m = 1
size = 0.2
N = 2
k = 150000
g = vector(0,-9.8,0)
L = 2.0 - m*mag(g)/k
theta = math.acos(1.95/2)

scene = canvas(width=475, height=475, center=vec(1.0, 1.0, 0), background=vec(0.5,0.5,0), align = "left")

balls = []
springs = []
pivots = []
for i in range(5):
    
    ball = sphere(radius = size, color = color.red, pos = vec(0.4*i, 0, 0))
    ball.m = m
    ball.v = vec(0, 0, 0)
    balls.append(ball)
    
    pivot = sphere(radius = 0.05, color = color.black, pos = vec(0.4*i, 2.0, 0))
    pivots.append(pivot)
    
    spring = cylinder(radius = 0.025, pos = vec(0.4*i, 2.0, 0), color = color.white)
    spring.axis = ball.pos - spring.pos
    spring.k = k
    springs.append(spring)

for i in range(N):
    balls[i].pos = vec(0.4 * i - 2.0 * math.sin(theta), 0.05, 0)
    springs[i].axis = balls[i].pos - pivots[i].pos
 
def af_col_v(m1, m2, v1, v2, x1, x2): # function after collision velocity
   v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot(v2-v1, x1-x2) / dot(x1-x2, x1-x2) # 投影
   v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot(v1-v2, x2-x1) / dot(x2-x1, x2-x1) # 投影 
   return (v1_prime, v2_prime)  
  
nCradle1 = graph(width = 375, height = 250, align = "right", xtitle = "t", ytitle = "J")
funct1 = gcurve(graph = nCradle1, color=color.red, width=4)
funct2 = gcurve(graph = nCradle1, color=color.blue, width=4)

nCradle2 = graph(width = 375, height = 250, align = "right", xtitle = "t", ytitle = "J")      
funct3 = gcurve(graph = nCradle2, color=color.orange, width=4)
funct4 = gcurve(graph = nCradle2, color=color.green, width=4)

iE,iU = 0.0, 0.0
aE,aU = 0.0, 0.0 
dt = 0.0001
t = 0.0
while True:
    rate(5000)
    t += dt
     
    for i in range(5):
        spring_force = -k * (mag(springs[i].axis) - L) * springs[i].axis.norm()
        balls[i].a = g + spring_force/m 
        balls[i].v += balls[i].a * dt
        balls[i].pos += balls[i].v * dt
        springs[i].axis = balls[i].pos - springs[i].pos
        
    for i in range(4):    
        if (mag(balls[i].pos - balls[i+1].pos) <= 0.4) and balls[i].v.x - balls[i+1].v.x > 0:
            (balls[i].v, balls[i+1].v) = af_col_v(m, m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos) 
    
    for i in range(5):
        iE += 1/2 * m * (mag(balls[i].v))**2
        iU += m * mag(g) * balls[i].pos.y
    
    aE += iE
    aU += iU
    
    funct1.plot(pos=(t, iE))
    funct2.plot(pos=(t, iU))
    funct3.plot(pos=(t, aE*dt/t)) 
    funct4.plot(pos=(t, aU*dt/t)) 
    
    iE = 0.0
    iU = 0.0