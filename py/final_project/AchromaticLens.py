from vpython import *
import numpy as np

scene = canvas(background=vec(0.8, 0.8, 0.8), width=1200, height=500, center=vec(10,-1.25,0))

#distance of two lens
D = 0

f = 20
phi = 1/f

#height of lens
lens_h = 1

def n_of_lamda(B, C, lamda):
    return B+C/lamda**2
B1, C1 = 1.5046, 0.0042
n1_blue, n1_green, n1_red = n_of_lamda(B1, C1, 0.4861), n_of_lamda(B1, C1, 0.58756), n_of_lamda(B1, C1, 0.6563)
v1 = (n1_green-1)/(n1_blue-n1_red)
B2, C2 = 1.67, 0.00743
n2_blue, n2_green, n2_red = n_of_lamda(B2, C2, 0.4861), n_of_lamda(B2, C2, 0.58756), n_of_lamda(B2, C2, 0.6563)
v2 = (n2_green-1)/(n2_blue-n2_red)
phi1 = v1/(f*(v1-v2))
f1 = 1/phi1
phi2 = v2/(f*(v2-v1))
f2 = 1/phi2

#first lens
r12 = - (n2_green - 1) * f2
r11 = 1/(phi1/(n1_green-1)-1/r12)
lens_surface1 = shapes.arc(radius=r12, angle1=0, angle2=asin(lens_h/r12), thickness = 0.01)
circle1 = paths.arc(pos=vec(-D/2-r12*cos(asin(lens_h/r12)), 0, 0), radius=0.0000001, angle2=2*pi, up=vec(1,0,0))
extrusion(path=circle1, shape=lens_surface1, color=color.yellow, opacity= 0.6)

lens_surface2 = shapes.arc(radius=r11, angle1=pi-asin(lens_h/r11), angle2=pi, thickness = 0.01)
circle2 = paths.arc(pos=vec(-D/2+r11*cos(asin(lens_h/r11)), 0, 0), radius=0.0000001, angle2=2*pi, up=vec(1,0,0))
extrusion(path=circle2, shape=lens_surface2, color=color.yellow, opacity= 0.6)

ABCD1_blue = [[1, 0], [(1-n1_blue)*(1/r12+1/r11), 1]]
ABCD1_green = [[1, 0], [(1-n1_green)*(1/r12+1/r11), 1]]
ABCD1_red = [[1, 0], [(1-n1_red)*(1/r12+1/r11), 1]]
ABCD1 = [ABCD1_blue, ABCD1_green, ABCD1_red]

#second lens
r21 = - (n2_green - 1) * f2
lens_surface3 = shapes.arc(radius=r21, angle1=0, angle2=asin(lens_h/r21), thickness = 0.01)
circle3 = paths.arc(pos=vec(D/2-r21*cos(asin(lens_h/r21)), 0, 0), radius=0.0000001, angle2=2*pi, up=vec(1,0,0))
extrusion(path=circle3, shape=lens_surface3, color=color.green, opacity= 0.6)

lens_surface4 = cylinder(pos = vec(D/2+r21-r21*cos(asin(lens_h/r21)), 0, 0), radius = lens_h, color = color.green, length = 0.0001, opacity = 0.6)

lens_surface5 = shapes.line(start = (D/2+r21-r21*cos(asin(lens_h/r21)), lens_h), end = (D/2, lens_h), thickness = 0.01)
circle5 = paths.arc(pos=vec(0, 0, 0), radius=0.0000001, angle2=2*pi, up=vec(1,0,0))
extrusion(path=circle5, shape=lens_surface5, color=color.green, opacity= 0.6)

ABCD2_blue = [[1, 0], [(n2_blue-1)*(1/r21), 1]]
ABCD2_green = [[1, 0], [(n2_green-1)*(1/r21), 1]]
ABCD2_red = [[1, 0], [(n2_red-1)*(1/r21), 1]]
ABCD2 = [ABCD2_blue, ABCD2_green, ABCD2_red]

#a line for referance
#curve(pos=[vec(min(-D,-2),0,0),vec(20,0,0)], color=color.red, radius = 0.008)

#light
object_height = 2*lens_h/3
x_temp = min(-D,-2)
ball_blue1 = sphere(pos = vec(x_temp,object_height,0), radius = 0.01, color = color.blue, R = [object_height,0], make_trail=True)
ball_green1 = sphere(pos = vec(x_temp,object_height,0), radius = 0.01, color = color.green, R = [object_height,0], make_trail=True)
ball_red1 = sphere(pos = vec(x_temp,object_height,0), radius = 0.01, color = color.red, R = [object_height,0], make_trail=True)
ball_blue2 = sphere(pos = vec(x_temp,-object_height,0), radius = 0.01, color = color.blue, R = [-object_height,0], make_trail=True)
ball_green2 = sphere(pos = vec(x_temp,-object_height,0), radius = 0.01, color = color.green, R = [-object_height,0], make_trail=True)
ball_red2 = sphere(pos = vec(x_temp,-object_height,0), radius = 0.01, color = color.red, R = [-object_height,0], make_trail=True)
balls = [ball_blue1, ball_green1, ball_red1, ball_blue2, ball_green2, ball_red2]

#for comparison
r1_com = 2*f*(n1_green-1)
r2_com = 2*f*(n1_green-1)
lens_surface6 = shapes.arc(radius=r2_com, angle1=0, angle2=asin(lens_h/r2_com), thickness = 0.01)
circle6 = paths.arc(pos=vec(-r2_com*cos(asin(lens_h/r2_com)), -2.5, 0), radius=0.0000001, angle2=2*pi, up=vec(1,0,0))
extrusion(path=circle6, shape=lens_surface6, color=color.yellow, opacity= 0.6)
lens_surface7 = shapes.arc(radius=r1_com, angle1=pi-asin(lens_h/r1_com), angle2=pi, thickness = 0.01)
circle7 = paths.arc(pos=vec(+r1_com*cos(asin(lens_h/r1_com)), -2.5, 0), radius=0.0000001, angle2=2*pi, up=vec(1,0,0))
extrusion(path=circle7, shape=lens_surface7, color=color.yellow, opacity= 0.6)
ball_blue1_com = sphere(pos = vec(x_temp,object_height-2.5,0), radius = 0.01, color = color.blue, R = [object_height,0], make_trail=True)
ball_green1_com = sphere(pos = vec(x_temp,object_height-2.5,0), radius = 0.01, color = color.green, R = [object_height,0], make_trail=True)
ball_red1_com = sphere(pos = vec(x_temp,object_height-2.5,0), radius = 0.01, color = color.red, R = [object_height,0], make_trail=True)
ball_blue2_com = sphere(pos = vec(x_temp,-object_height-2.5,0), radius = 0.01, color = color.blue, R = [-object_height,0], make_trail=True)
ball_green2_com = sphere(pos = vec(x_temp,-object_height-2.5,0), radius = 0.01, color = color.green, R = [-object_height,0], make_trail=True)
ball_red2_com = sphere(pos = vec(x_temp,-object_height-2.5,0), radius = 0.01, color = color.red, R = [-object_height,0], make_trail=True)
balls_com = [ball_blue1_com, ball_green1_com, ball_red1_com, ball_blue2_com, ball_green2_com, ball_red2_com]
#curve(pos=[vec(min(-D,-2),-2.5,0),vec(20,-2.5,0)], color=color.red, radius = 0.008)
ABCD_com_blue = [[1, 0], [(1-n1_blue)*(1/r2_com+1/r1_com), 1]]
ABCD_com_green = [[1, 0], [(1-n1_green)*(1/r2_com+1/r1_com), 1]]
ABCD_com_red = [[1, 0], [(1-n1_red)*(1/r2_com+1/r1_com), 1]]
ABCD_com = [ABCD_com_blue, ABCD_com_green, ABCD_com_red]

def ABCD_matrix_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]], [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def H_matrix_mul(A, R):
    return [A[0][0]*R[0]+A[0][1]*R[1], A[1][0]*R[0]+A[1][1]*R[1]]

v = 0.01
t = 0
dt = 0.001
t1 = [0, 0, 0, 0, 0, 0]
t2 = [0, 0, 0, 0, 0, 0]
t_com = [0, 0, 0, 0, 0, 0]
focal_points = [0, 0, 0]
while(ball_blue1.pos.y > ball_blue2.pos.y or ball_green1.pos.y > ball_green2.pos.y or ball_red1.pos.y > ball_red2.pos.y):
    rate(1000)
    for i in range(len(balls)):
        balls[i].pos.x += v*cos(atan(balls[i].R[1]))
        balls[i].pos.y += v*sin(atan(balls[i].R[1]))
        balls[i].R[0] = balls[i].pos.y
        if D == 0:
            if balls[i].pos.x >= 0 and t1[i] == 0 and t2[i] == 0:
                balls[i].R = H_matrix_mul(ABCD_matrix_mul(ABCD2[i%3],ABCD1[i%3]),balls[i].R)
                t1[i] = 1
                t2[i] = 1
        else:
            if balls[i].pos.x >= -D/2 and t1[i] == 0:
                balls[i].R = H_matrix_mul(ABCD1[i%3],balls[i].R)
                t1[i] = 1
            if balls[i].pos.x >= D/2 and t2[i] == 0:
                balls[i].R = H_matrix_mul(ABCD2[i%3],balls[i].R)
                t2[i] = 1
        if balls[i%3].pos.y <= balls[i%3+3].pos.y and focal_points[i%3] == 0 and 3 <= i:
            focal_points[i%3] = (balls[i%3].pos+balls[i%3+3].pos)/2
    for i in range(len(balls_com)):
        balls_com[i].pos.x += v*cos(atan(balls_com[i].R[1]))
        balls_com[i].pos.y += v*sin(atan(balls_com[i].R[1]))
        balls_com[i].R[0] = balls_com[i].pos.y + 2.5
        if balls_com[i].pos.x >= 0 and t_com[i] == 0:
                balls_com[i].R = H_matrix_mul(ABCD_com[i%3],balls_com[i].R)
                t_com[i] = 1
    t += dt
#print(focal_points)
gd1 = graph(title="d - lamda", width=1000, height=450, x=0, y=600, xtitle="lamda(nm)", ytitle="d(cm)")
gd2 = graph(title="|f-d| - lamda", width=1000, height=450, x=0, y=600, xtitle="lamda(nm)", ytitle="|f-d|(cm)")
gd3 = graph(title="d - lamda (for comparison),green:1 lens,red:2 lenses", width=1000, height=450, x=0, y=600, xtitle="lamda(cm)", ytitle="d(cm)")
gd4 = graph(title="|f-d| - lamda (for comparison),green:1 lens,red:2 lenses", width=1000, height=450, x=0, y=600, xtitle="lamda(nm)", ytitle="|f-d|(cm)")
gd5 = graph(title="d - D", width=1000, height=450, x=0, y=600, xtitle="D(cm)", ytitle="d(cm)")
gd6 = graph(title="|f-d| - f", width=1000, height=450, x=0, y=600, xtitle="f(cm)", ytitle="|f-d|(cm)")
gd7 = graph(title="|f-d| - f", width=1000, height=450, x=0, y=600, xtitle="f(cm)", ytitle="|f-d|(cm)")
gd8 = graph(title="|f-d| - lamda", width=1000, height=450, x=0, y=600, xtitle="lamda(nm)", ytitle="|f-d|(cm)")
gd1r = gcurve(graph=gd1, color=color.red)
gd2r = gcurve(graph=gd2, color=color.red)
gd3r = gcurve(graph=gd3, color=color.red)
gd3r_com = gcurve(graph=gd3, color=color.green)
gd4r = gcurve(graph=gd4, color=color.red)
gd4r_com = gcurve(graph=gd4, color=color.green)
gd5r_blue = gcurve(graph=gd5, color=color.blue)
gd5r_green = gcurve(graph=gd5, color=color.green)
gd5r_red = gcurve(graph=gd5, color=color.red)
gd5r = [gd5r_blue, gd5r_green, gd5r_red]
gd6r_blue = gcurve(graph=gd6, color=color.blue)
gd6r_green = gcurve(graph=gd6, color=color.green)
gd6r_red = gcurve(graph=gd6, color=color.red)
gd6r = [gd6r_blue, gd6r_green, gd6r_red]
gd7r_400 = gcurve(graph=gd7, color=color.blue)
gd7r_450 = gcurve(graph=gd7, color=color.yellow)
gd7r_500 = gcurve(graph=gd7, color=color.green)
gd7r_550 = gcurve(graph=gd7, color=color.cyan)
gd7r_600 = gcurve(graph=gd7, color=color.red)
gd7r = [gd7r_400, gd7r_450, gd7r_500, gd7r_550, gd7r_600]
gd8r_400 = gcurve(graph=gd8, color=color.blue)
gd8r_450 = gcurve(graph=gd8, color=color.yellow)
gd8r_500 = gcurve(graph=gd8, color=color.green)
gd8r_550 = gcurve(graph=gd8, color=color.cyan)
gd8r_600 = gcurve(graph=gd8, color=color.red)
gd8r = [gd8r_400, gd8r_450, gd8r_500, gd8r_550, gd8r_600]

for lamda in range(380, 800, 5):
    n1, n2 = n_of_lamda(B1, C1, 0.001*lamda), n_of_lamda(B2, C2, 0.001*lamda)
    result = H_matrix_mul(ABCD_matrix_mul([[1, 0], [(n2-1)*(1/r21), 1]],[[1, 0], [(1-n1)*(1/r12+1/r11), 1]]),[object_height,0])
    d = -result[0]/result[1]
    result_com = H_matrix_mul([[1, 0], [(1-n1)*(1/r2_com+1/r1_com), 1]],[object_height,0])
    d_com = -result_com[0]/result_com[1]
    gd1r.plot(pos = (1*lamda, d))
    gd2r.plot(pos = (1*lamda, abs(f-d)))
    gd3r.plot(pos = (1*lamda, d))
    gd4r.plot(pos = (1*lamda, abs(f-d)))
    gd3r_com.plot(pos = (1*lamda, d_com))
    gd4r_com.plot(pos = (1*lamda, abs(f-d_com)))

for D_ in range(50,100):
    D = 0.01*D_
    R = [[object_height, 0], [object_height, 0], [object_height, 0]]
    for i in range(3):
        result = H_matrix_mul(ABCD_matrix_mul(ABCD2[i],ABCD_matrix_mul([[1, D], [0, 1]],ABCD1[i])),R[i])
        d = -result[0]/result[1]+D/2
        gd5r[i].plot(pos = (D, d))

for f_ in range(150,250):
    f = 0.1*f_
    phi1 = v1/(f*(v1-v2))
    f1 = 1/phi1
    phi2 = v2/(f*(v2-v1))
    f2 = 1/phi2
    n1_blue, n1_green, n1_red = n_of_lamda(B1, C1, 0.4861), n_of_lamda(B1, C1, 0.58756), n_of_lamda(B1, C1, 0.6563)
    n2_blue, n2_green, n2_red = n_of_lamda(B2, C2, 0.4861), n_of_lamda(B2, C2, 0.58756), n_of_lamda(B2, C2, 0.6563)
    r12 = - (n2_green - 1) * f2
    r11 = 1/(phi1/(n1_green-1)-1/r12)
    r21 = - (n2_green - 1) * f2
    ABCD1_blue = [[1, 0], [(1-n1_blue)*(1/r12+1/r11), 1]]
    ABCD1_green = [[1, 0], [(1-n1_green)*(1/r12+1/r11), 1]]
    ABCD1_red = [[1, 0], [(1-n1_red)*(1/r12+1/r11), 1]]
    ABCD1 = [ABCD1_blue, ABCD1_green, ABCD1_red]
    ABCD2_blue = [[1, 0], [(n2_blue-1)*(1/r21), 1]]
    ABCD2_green = [[1, 0], [(n2_green-1)*(1/r21), 1]]
    ABCD2_red = [[1, 0], [(n2_red-1)*(1/r21), 1]]
    ABCD2 = [ABCD2_blue, ABCD2_green, ABCD2_red]
    R = [[object_height, 0], [object_height, 0], [object_height, 0]]
    for i in range(3):
        result = H_matrix_mul(ABCD_matrix_mul(ABCD2[i], ABCD1[i]),R[i])
        d = -result[0]/result[1]
        gd6r[i].plot(pos = (f, abs(f-d)))
        
for f_ in range(150,250):
    f = 0.1*f_
    phi1 = v1/(f*(v1-v2))
    f1 = 1/phi1
    phi2 = v2/(f*(v2-v1))
    f2 = 1/phi2
    n1_green = n_of_lamda(B1, C1, 0.587222434334)
    n2_green = n_of_lamda(B2, C2, 0.587222434334)
    n1_400, n1_450, n1_500,  n1_550, n1_600= n_of_lamda(B1, C1, 0.4), n_of_lamda(B1, C1, 0.45), n_of_lamda(B1, C1, 0.5), n_of_lamda(B1, C1, 0.55), n_of_lamda(B1, C1, 0.6)
    n2_400, n2_450, n2_500,  n2_550, n2_600= n_of_lamda(B2, C2, 0.4), n_of_lamda(B2, C2, 0.45), n_of_lamda(B2, C2, 0.5), n_of_lamda(B2, C2, 0.55), n_of_lamda(B2, C2, 0.6)
    r12 = - (n2_green - 1) * f2
    r11 = 1/(phi1/(n1_green-1)-1/r12)
    r21 = - (n2_green - 1) * f2
    ABCD1_400 = [[1, 0], [(1-n1_400)*(1/r12+1/r11), 1]]
    ABCD1_450 = [[1, 0], [(1-n1_450)*(1/r12+1/r11), 1]]
    ABCD1_500 = [[1, 0], [(1-n1_500)*(1/r12+1/r11), 1]]
    ABCD1_550 = [[1, 0], [(1-n1_550)*(1/r12+1/r11), 1]]
    ABCD1_600 = [[1, 0], [(1-n1_600)*(1/r12+1/r11), 1]]
    ABCD1 = [ABCD1_400, ABCD1_450, ABCD1_500, ABCD1_550, ABCD1_600]
    ABCD2_400 = [[1, 0], [(n2_400-1)*(1/r21), 1]]
    ABCD2_450 = [[1, 0], [(n2_450-1)*(1/r21), 1]]
    ABCD2_500 = [[1, 0], [(n2_500-1)*(1/r21), 1]]
    ABCD2_550 = [[1, 0], [(n2_550-1)*(1/r21), 1]]
    ABCD2_600 = [[1, 0], [(n2_600-1)*(1/r21), 1]]
    ABCD2 = [ABCD2_400, ABCD2_450, ABCD2_500, ABCD2_550, ABCD2_600]
    R = [[object_height, 0], [object_height, 0], [object_height, 0], [object_height, 0], [object_height, 0]]
    for i in range(5):
        result = H_matrix_mul(ABCD_matrix_mul(ABCD2[i], ABCD1[i]),R[i])
        d = -result[0]/result[1]
        gd7r[i].plot(pos = (f, abs(f-d)))
        
for lamda_ in range(380,780):
    lamda = 0.001*lamda_
    f = 20
    phi1 = v1/(f*(v1-v2))
    f1 = 1/phi1
    phi2 = v2/(f*(v2-v1))
    f2 = 1/phi2
    n1_green = n_of_lamda(B1, C1, lamda)
    n2_green = n_of_lamda(B2, C2, lamda)
    n1_400, n1_450, n1_500,  n1_550, n1_600= n_of_lamda(B1, C1, 0.4), n_of_lamda(B1, C1, 0.45), n_of_lamda(B1, C1, 0.5), n_of_lamda(B1, C1, 0.55), n_of_lamda(B1, C1, 0.6)
    n2_400, n2_450, n2_500,  n2_550, n2_600= n_of_lamda(B2, C2, 0.4), n_of_lamda(B2, C2, 0.45), n_of_lamda(B2, C2, 0.5), n_of_lamda(B2, C2, 0.55), n_of_lamda(B2, C2, 0.6)
    r12 = - (n2_green - 1) * f2
    r11 = 1/(phi1/(n1_green-1)-1/r12)
    r21 = - (n2_green - 1) * f2
    ABCD1_400 = [[1, 0], [(1-n1_400)*(1/r12+1/r11), 1]]
    ABCD1_450 = [[1, 0], [(1-n1_450)*(1/r12+1/r11), 1]]
    ABCD1_500 = [[1, 0], [(1-n1_500)*(1/r12+1/r11), 1]]
    ABCD1_550 = [[1, 0], [(1-n1_550)*(1/r12+1/r11), 1]]
    ABCD1_600 = [[1, 0], [(1-n1_600)*(1/r12+1/r11), 1]]
    ABCD1 = [ABCD1_400, ABCD1_450, ABCD1_500, ABCD1_550, ABCD1_600]
    ABCD2_400 = [[1, 0], [(n2_400-1)*(1/r21), 1]]
    ABCD2_450 = [[1, 0], [(n2_450-1)*(1/r21), 1]]
    ABCD2_500 = [[1, 0], [(n2_500-1)*(1/r21), 1]]
    ABCD2_550 = [[1, 0], [(n2_550-1)*(1/r21), 1]]
    ABCD2_600 = [[1, 0], [(n2_600-1)*(1/r21), 1]]
    ABCD2 = [ABCD2_400, ABCD2_450, ABCD2_500, ABCD2_550, ABCD2_600]
    R = [[object_height, 0], [object_height, 0], [object_height, 0], [object_height, 0], [object_height, 0]]
    for i in range(5):
        result = H_matrix_mul(ABCD_matrix_mul(ABCD2[i], ABCD1[i]),R[i])
        d = -result[0]/result[1]
        gd8r[i].plot(pos = (lamda_, abs(f-d)))






