from vpython import *
g=9.8 
size = 0.25 
height = 15.0 
C_drag = 0.9
theta = pi/4

scene = canvas(width=600, height=400, center =vec(0,height/2,0), background=vec(0.5,0.5,0), align = "left")
floor = box(length=30, height=0.01, width=10, color=color.blue)
ball = sphere(radius = size, color=color.red, make_trail = True)
ball.pos = vec(-15, size, 0)
ball.v = vec(20*cos(theta), 20*sin(theta), 0)

a1 = arrow(color = color.green, shaftwidth = size/3, length = 3*size)
a1.pos = ball.pos
a1.axis = ball.v / ball.v.mag * 2

v_t = graph(title = "v-t graph", xtitle = "t", ytitle = "v", align = "right", width = 600)
f1 = gcurve(graph = v_t, color = color.red, width = 4)

t = 0  # tatal time
c = 0  # times of hitting ground
td = 0 # total distance
lh = 0 # largest height

dt = 0.001 
while c < 3: 
    rate(1000) 
    ball.v += vec(0, -g*dt, 0) - C_drag*ball.v*dt
    ball.pos += ball.v*dt
    a1.pos = ball.pos
    a1.axis = ball.v / ball.v.mag * 2
    if ball.pos.y <= size:
        ball.v.y = -ball.v.y
        c += 1

    t += 0.001
    f1.plot(pos = (t, ball.v.mag))

    td += ball.v.mag*dt # total distance

    if ball.pos.y >= lh:
        lh = ball.pos.y       
    
d = ball.pos.x - (-15)

msg = text(text = "displacement = " + str(d), pos = vec(-10, 14, 0))
msg = text(text = "total distance = " + str(td), pos = vec(-10, 12, 0))
msg = text(text = "largest height = " + str(lh), pos = vec(-10, 10, 0))