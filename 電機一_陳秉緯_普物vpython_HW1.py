from vpython import *

g = 9.8              # g = 9.8 m/s^2 
size = 0.25        # ball radius = 0.25 m
C_drag = 0.9       # drag Coefficient = 0.9
theta = pi/4       # angle 
t = 0              # total time
hit_ground = 0     # times of ball hitting ground

# background 
scene = canvas(align = 'left', center = vec(0,5,0), width = 350, background = vec(0.5,0.5,0))  
floor = box(length = 30, height = 0.01, width = 10, color = color.blue) 
floor.pos = vec(0.0, 0.0, 0.0)

# initialization of the ball
ball = sphere(radius = size, color = color.magenta, make_trail = True, trail_radius = size/3)  
ball.pos = vec(-15.0, size, 0.0)                  # ball's initial position 
ball.v = vec(20*cos(theta), 20*sin(theta), 0.0)   # ball's initial velocity 

# arrow of vector of velocity
velocity = arrow(color = color.black, length = 0.1, shafwidth = 0.25)
velocity.pos = ball.pos
velocity.axis = ball.v*0.5

# delcare and define the graph of speed
speed_time = graph(width = 400, align = 'right')
func1 = gdots(graph = speed_time, color = color.red, size = 2)

# initialize the largest_height and the distance
largest_height = ball.pos.y
distance = 0

dt = 0.001
while hit_ground < 3:                           # simulate until hit ground for three times
 rate(1000) 

 ball.v += vec(0, -g, 0)*dt - C_drag*ball.v*dt  # the change of the velocity of the ball  
 ball.pos += ball.v*dt                          # the change of the position of the ball 
 velocity.pos = ball.pos                        # renew arrow position
 velocity.axis = ball.v*0.5                     # keep the angle between axis of arrow and that of ball on pi/4 


 t += 0.001 
 func1.plot(pos = (t, ball.v.mag))              # illustrate the graph of speed
 
 distance += ball.v.mag*dt                      # get the distance

 if ball.pos.y > largest_height:                # get the largest height
    largest_height = ball.pos.y
        
 if ball.pos.y <= size and ball.v.y < 0:        # check if ball hits the ground
    ball.v.y = - ball.v.y                       # if so, reverse y component of velocity
    hit_ground += 1                             # the loop couter of while
    

# show the data we got
message1 = text(text = 'displacement = ' + str(ball.pos.x + 15), pos = vec(-10, 7.5, 0), color = color.cyan)   
message2 = text(text = 'total distance = ' + str(distance), pos = vec(-10, 9, 0), color = color.cyan)    
message3 = text(text = 'largest height = ' + str(largest_height), pos = vec(-10, 10.5, 0), color = color.cyan)

