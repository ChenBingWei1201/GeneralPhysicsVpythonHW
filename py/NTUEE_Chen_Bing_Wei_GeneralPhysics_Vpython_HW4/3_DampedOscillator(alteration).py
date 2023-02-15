from vpython import *
size, m = 0.02, 0.2 # ball size = 0.02 m, ball mass = 0.2kg
L, k = 0.2, 20 # spring original length = 0.2m, force constant = 20 N/m
amplitude = 0.03
w = sqrt(k/m) 
b = 0.05 * m * w
fa = 0.1
# scene = canvas(width=600, height=400, range = 0.3, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0))
# wall_left = box(length=0.005, height=0.3, width=0.3, color=color.blue) # left wall
# ball = sphere(radius = size, color=color.red) # ball
# spring = helix(radius=0.015, thickness =0.01)
# oscillation1 = graph(width = 600, align = 'right', background = vec(0.5, 0.5, 0), xtitle = 't', ytitle = 'x')
# func1 = gcurve(graph = oscillation1, color = color.red, width = 4)
oscillation2 = graph(width = 600, align = 'right', background = vec(0.5, 0.5, 0), xtitle = 't', ytitle = 'average power')
func2 = gdots(graph = oscillation2, color=color.cyan, size=0.001)
class obj: pass
ball, spring = obj(), obj()

ball.pos = vec(L, 0 , 0)
ball.v = vec(0, 0, 0)
ball.m = m
spring.pos = vec(0, 0, 0)

n, t, dt = 1, 0, 0.001
T = 2* pi/w
power = 0.0
while True:
    # rate(1000)
    spring.axis = ball.pos - spring.pos
    springForce = -k * (mag(spring.axis)-L) * norm(spring.axis)
    dampingForce = -b * ball.v
    sinusoidalForce = fa*sin(w*t) *norm(spring.axis)
    ball.a = (springForce + dampingForce + sinusoidalForce) / ball.m
    ball.v += ball.a * dt
    ball.pos += ball.v * dt
    t += dt
    power += dot(sinusoidalForce, ball.v)*dt
    averagePower = power/T
    if t/T >= n:
        # func1.plot(pos = (t, ball.pos.x - L))
        func2.plot(pos = (t, averagePower))
        n += 1.0
        power = 0 # remember to reset to zero!

    
