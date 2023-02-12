from vpython import *

g, size, height = 9.8, 0.25, 15.0

class any_ball(sphere):  # any_ball inherited properties from sphere
 m = 1.0 
 v = vector(0,0,0) 
 def kinetic_energy(self): # declaring a method, which is a function belonged to a specific class. The way it works is the same as a function
  return 0.5 * self.m * mag(self.v)**2 # Ek = (1/2)*m*(v^2)

scene = canvas(width=800, height=800, center = vec(0,height/2,0), background=vec(0.5,0.5,0))
floor = box(length=30, height=0.01, width=10, color=color.blue)
ball = any_ball(radius = size, color=color.red) 

print(ball.m, ball.v, ball.kinetic_energy()) 

ball.pos, ball.v, ball.m = vector(0, height, 0), vector(0, 0, 0), 3.0

dt = 0.001
while ball.pos.y >= size:
 rate(1000)
 ball.pos += ball.v*dt
 ball.v.y += - g*dt
 
print(ball.m, ball.v, ball.kinetic_energy())