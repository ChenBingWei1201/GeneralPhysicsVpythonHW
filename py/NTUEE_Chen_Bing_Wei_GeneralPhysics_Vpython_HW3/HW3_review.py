from vpython import*

G=6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10} #10 times larger for better view
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0


def G_force(m1, m2, pos_vec1, pos_vec2):
    return -G*m1*m2/mag2(pos_vec2-pos_vec1) * norm(pos_vec2-pos_vec1)
class as_obj(sphere):
    def kinetic_energy(self):
        return 0.5*self.m*mag(self.v)**2
    def potential_energy(self):
        return -G*mass['sun']*self.m/mag(self.pos)
    
scene = canvas(width=800, height=800, background=vector(0, 0, 0))
scene.lights = []

# scene.forward = vector(0, -1, 0)
sun = sphere(pos = vec(earth_orbit['r'], 0, 0), radius = radius['sun'], color = color.orange, emissive=True)
local_light(pos = sun.pos)
sun.m = mass['sun']

earth = as_obj(pos = vec(0, 0, 0), radius = radius['earth'], m = mass['earth'], texture = {"file":textures.earth})
earth.v = vec(0, 0, -earth_orbit['v'])
earth.m = mass['earth']

moon = as_obj(pos = vec(moon_orbit['r'] * cos(theta), moon_orbit['r'] * sin(theta), 0), radius = radius['moon'], m = mass['moon'], color = color.white)
moon.v = vec(0, 0, -moon_orbit['v'])
moon.m = mass['moon']


# print(earth.potential_energy(), earth.kinetic_energy())

dt = 3600
while True:
    rate(1000)
    earth.a = G_force(earth.m, moon.m, earth.pos, moon.pos)/earth.m + G_force(earth.m, sun.m, earth.pos, sun.pos)/earth.m
    moon.a = G_force(moon.m, earth.m, moon.pos, earth.pos)/moon.m + G_force(sun.m, moon.m, sun.pos, moon.pos)/moon.m
    sun = G_force(sun.m, earth.m, sun.pos, earth.pos)/sun.m + G_force(sun.m, earth.m, sun.pos, earth.pos)/sun.m
    earth.v += earth.a * dt
    moon.v += moon.a * dt
    sun.v += sun.a * dt
    earth.pos += earth.v * dt
    moon.pos += moon.v * dt
    sun.pos += sun.v * dt
    scene.center = earth.pos
    