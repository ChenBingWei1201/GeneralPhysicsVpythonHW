from vpython import*

# background
N = 2                    # the balls are lifted
g = vector(0, -9.8, 0)   # g = 9.8 (m/s^2)
m = 1                    # mass = 1 (kg) 
size = 0.2               # ball radius = 0.2 (m)
dt = 0.0001              # the time step of the simulation
k = 150000               # the force constant of the rope
L = 2 - m* mag(g)/k      # the origin length of the rope
scene = canvas(width = 450, height = 400, center = vec(0, -1, 0), background = vec(0.6, 0.7, 0.98), align  = "left")

# the object 
pivots = []
balls = []
ropes = []
for i in range(5):
    pivot = sphere(radius = 0.05, pos = vec((i-2)*0.4, 0, 0), color = color.black)
    pivots.append(pivot)

    ball = sphere(radius = size, pos = vec((i-2)*0.4, -2.0, 0), color = color.magenta)
    ball.v = vector(0, 0, 0)
    balls.append(ball)

    rope = cylinder(pos = vec((i-2)*0.4, 0, 0), radius = 0.03, color = color.orange)
    rope.axis = vector(0, -2, 0)
    ropes.append(rope)

# collision    
# collision origin
def af_col_v( v1, v2, x1, x2, m1 = 1, m2 = 1):                                       # function after collision
    v1_prime = v1 + 2* (m2/(m1+m2))*(x1-x2)  * dot(v2-v1, x1-x2) / dot(x1-x2, x1-x2) # dot:two numbers mutiply together
    v2_prime = v2 + 2* (m1/(m1+m2))*(x2-x1)  * dot(v1-v2, x2-x1) / dot(x2-x1, x2-x1) 
    return (v1_prime, v2_prime)


# the graph and function 
E_instant = graph(width = 350, height = 200, align = 'right')
E_average = graph(width = 350, height = 200, align = 'right')

func_K_i = gcurve(graph = E_instant, color = color.red, size = 1)
func_U_i = gcurve(graph = E_instant, color = color.blue, size = 1)

func_K_a = gcurve(graph = E_average, color = color.red, size = 1)
func_U_a = gcurve(graph = E_average, color = color.blue, size = 1)

K_i, U_i, K_a, U_a = 0, 0, 0, 0

# stimulation
# lift N balls up 0.05m 
x = sqrt(2**2 -1.95**2) # ball go to left
for i in range(N):
    balls[i].pos += vector(-x, 0.05, 0)
    ropes[i].axis = balls[i].pos - pivots[i].pos

# balls become moving
t = 0
while True:
    rate(5000)
    t += dt
   
    # ball dropping
    for i in range(5):
        rope_force = -k*(mag(ropes[i].axis) - L)* ropes[i].axis.norm()
        balls[i].a = g + rope_force/m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        ropes[i].axis = balls[i].pos - pivots[i].pos
    
    # collision start
    for i in range(4):
        if mag(balls[i].pos - balls[i+1].pos) <= 0.4 and balls[i].v.x - balls[i+1].v.x > 0 :
            (balls[i].v, balls[i+1].v) = af_col_v(balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
            # balls[i].v, balls[i+1].v = balls[i+1].v, balls[i].v

    # draw graphs
    # calculate five balls total instant energy
    K_i, U_i = 0, 0
    for n in range(5):
        K_i += (0.5 * m * mag(balls[n].v)**2)
        U_i += (m * mag(g) * (balls[n].pos.y + 2))
    
    # accumulate total kinetic/potential energy of all time
    K_a += K_i
    U_a += U_i

    # draw function
    func_K_i.plot(pos = (t, K_i))
    func_U_i.plot(pos = (t, U_i))
    func_K_a.plot(pos = (t, K_a*dt/t))
    func_U_a.plot(pos = (t, U_a*dt/t))
