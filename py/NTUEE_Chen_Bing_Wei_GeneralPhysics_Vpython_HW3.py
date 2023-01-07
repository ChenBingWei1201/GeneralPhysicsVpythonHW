from vpython import*

# background settings
scene = canvas(height = 400, width = 600, background = vec(0, 0, 0))

# constant settings
G = 6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} # 10 times larger for better view
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0


# gravitional force (1:受力物 2:施力物)
def G_force(mass1, position1, mass2, position2):
  return G*mass1*mass2/mag2(position2-position1)*norm(position2-position1)

# earth
earth = sphere(radius = radius['earth'], texture = {'file':textures.earth})
earth.m = mass['earth']
earth.pos = vec(0, 0, 0)
earth.v = vec(0, 0, 0)               

# the moon
moon = sphere(radius = radius['moon'], color = color.white)
moon.m = mass['moon']
moon.pos = vec(moon_orbit['r']*cos(-theta), moon_orbit['r']*sin(-theta), 0)
moon.v = vec(0, 0, -moon_orbit['v'])

# 地-月系統動量守恆, 地-月系統質心固定
u = 7.36/604.36*moon.v
d = 7.36/604.36*moon.pos
earth.v -= u
moon.v -= u
earth.pos -= d
moon.pos -= d

# sun
sun = sphere(radius = radius['sun'],color = color.orange, emissive = True)
sun.m = mass['sun']
sun.pos = vec(0, 0, 0)
sun.v = vec(0, 0, 0)
scene.lights = []          # 背景無光
local_light(pos = sun.pos) # 以太陽為光源


# 在太陽軌道上的位置和初速
earth.pos += vec(earth_orbit['r'], 0, 0)
moon.pos += vec(earth_orbit['r'], 0, 0)
earth.v +=vec(0, 0, -earth_orbit['v'])
moon.v +=vec(0, 0, -earth_orbit['v'])

# 垂直月球繞地軌道面的箭頭
moon_norm = arrow(color = color.cyan, shaftwidth = 0.1*radius['earth'])
moon_norm.pos = earth.pos
# 垂直黃道面的箭頭
eclip_norm = arrow(color = color.magenta, shaftwidth = 0.1*radius['earth'])
eclip_norm.pos = earth.pos

dt = 60*60*3
t = 0
c = -0.25
previous_phi = 0

while True:
  rate(1000)

  # 帶入之前def的公式
  earth.a = G_force(earth.m, earth.pos, moon.m, moon.pos)/earth.m + G_force(earth.m, earth.pos, sun.m, sun.pos)/earth.m
  moon.a = G_force(moon.m, moon.pos, earth.m, earth.pos)/moon.m + G_force(moon.m, moon.pos, sun.m, sun.pos)/moon.m
  sun.a = G_force(sun.m, sun.pos, moon.m, moon.pos)/sun.m + G_force(sun.m, sun.pos, earth.m, earth.pos)/sun.m

  earth.v += earth.a*dt 
  earth.pos += earth.v*dt
  moon.v += moon.a*dt 
  moon.pos += moon.v*dt
  sun.v += sun.a*dt 
  sun.pos += sun.v*dt

  scene.center = earth.pos
  
  moon_norm.pos = earth.pos
  eclip_norm.pos = earth.pos
  moon_norm.axis = 3*radius['earth']*norm(cross(moon.pos-earth.pos,moon.v-earth.v))
  eclip_norm.axis = 3*radius['earth']*norm(cross(earth.pos-sun.pos,earth.v-sun.v))


  projection = norm(cross(moon.pos-earth.pos,moon.v-earth.v))-proj(norm(cross(moon.pos-earth.pos,moon.v - earth.v)),vec(0,1,0))
  phi = 190/pi*diff_angle(vec(1,0,0), projection)
  
  if(phi - 90)*(previous_phi - 90) < 0 and c < 3:
    c += 0.5
    time =t/(365.24*86400*c) # time表示經過幾年
    print('The moon precession is ', time, 'years')
  previous_phi = phi
  t += dt
