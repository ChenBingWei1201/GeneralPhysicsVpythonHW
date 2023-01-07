from vpython import *

scene = canvas(width = 600, height = 600, background = vec(0.5, 0.5, 0))

g = 9.8 # g = 9.8 m/s^2
size = 0.25 # ball radius = 0.25 m
height = 15.0 # ball center initial height = 15 m
scene = canvas(width = 800, height = 800, center = vec(0, height/2, 0), background = vec(0.5, 0.5, 0)) # open a window
floor = box(length = 30, height = 0.01, width = 10, color = color.blue) # the floor
ball = sphere(radius = size, color = color.red, make_trail = True, trail_radius = 0.05) # the ball
ball.pos = vec( 0, height, 0) # ball center initial position
ball.v = vec(0, 0 , 0) # ball initial velocity
msg =text(text = 'Free Fall', pos = vec(-10, 10, 0))

a1 = arrow(color = color.green, shaftwidth = 0.1)
a1.pos = ball.pos
a1.axis = vec(0, -1, 0)


dt = 0.001 # time step
while ball.pos.y >= size: # until the ball hit the ground
    rate(1000) # run 1000 times per real second
    ball.pos = ball.pos + ball.v*dt
    ball.v.y = ball.v.y - g*dt
    a1.pos = ball.pos
msg.visible = False
msg = text(text = str(ball.v.y), pos = vec(-10, 10, 0))
print(ball.v.y)