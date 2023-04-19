##(for Jupyter also for VIDLE)
from vpython import *
pos, angle = vector(0, 0, 0), 0
def right(b): #callback function
 global pos, angle
 pos = pos + vector(0.1, 0, 0)
def left(b):
 global pos, angle
 pos = pos + vector(-0.1, 0, 0)
def up(b):
 global pos, angle
 pos = pos + vector(0, 0.1, 0) 
def down(b):
 global pos, angle
 pos = pos + vector(0, -0.1, 0) 
scene = canvas(width=400, height=400, range = 5, background=color.white)
ball = sphere(radius = 2.0, texture=textures.earth )
button(text='left', pos=scene.title_anchor, bind = left)
button(text='up', pos=scene.title_anchor, bind = up)
button(text='down', pos=scene.title_anchor, bind = down)
button(text='right', pos=scene.title_anchor, bind = right)

while True:
 rate(1000)
 ball.rotate(angle=pi/600, axis= vector(sin(angle),cos(angle),0), origin=pos)
 ball.pos = pos