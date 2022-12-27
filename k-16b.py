from vpython import*
G=6.673E-11
dis = 1.495E11 #0.01 AU
sun_mass = 1.989E30
sun_radius, jupiter_radius = 6.96E8, 6.99E7
sun_mass, jupiter_mass = 1.989E30, 1.898E27
mass = {'alpha': 0.690,'beta': 0.203, 'planet': 0.333} #the mass of the stars proportional to sun
radius = {'alpha': 0.649, 'beta': 0.226, 'planet': 0.7538}
dis = 1.95E11
#d_at_perihelion = {'earth': 1.495E11, 'mars':2.279E11, 'halley': 8.7665E10}
def G_force(m1, m2, pos_vec):
    return -G * m1 * m2 / mag2(pos_vec) * norm(pos_vec)
def G_potential(m1, m2, pos_vec):
    return -G * m1 * m2 / mag(pos_vec)
class planets(sphere):
    def kinetic_energy(self):
        return 0.5 * self.m * mag2(self.v)
    def potential_energy(self):
        return - G * mass['sun'] * self.m / mag(self.pos)
scene = canvas(width=800, height=800, background=vector(0,0,0))
scene.lights = []

suna = sphere(pos=vector(0,0,0), m = mass['alpha'] * sun_mass, radius = radius['alpha'] * sun_radius * 10, color = color.orange, emissive=True, make_trail = True)
sunb = sphere(pos=vector(dis * 0.224,0,0), m = mass['beta'] * sun_mass, radius = radius['beta'] * sun_radius * 10, color = color.red, emissive=True, make_trail = True)
planets = []
com = (suna.m * suna.pos + sunb.m * sunb.pos) / (suna.m + sunb.m)
for i in range (1):
    planet = sphere(pos=vector(dis * (0.5 + 0.1 * i), 0, 0) - com, m = mass['planet'] * jupiter_mass, radius = radius['planet'] * jupiter_radius * 100, color = color.blue, emission = True, make_trail = True)
    planets.append(planet)
local_light(pos=vector(0,0,0))
suna.pos -= com
sunb.pos -= com
V0 = sqrt(G / mag(suna.pos - sunb.pos) / (suna.m + sunb.m))
suna.v = vector(0, V0*sunb.m, 0)
sunb.v = vector(0, -V0*suna.m, 0)
for i in range (1):
    planets[i].v = vector(0, -1* sqrt(-1 * (G_potential(planets[i].m, suna.m, planets[i].pos - suna.pos) + G_potential(planets[i].m, sunb.m, planets[i].pos - sunb.pos)) / planets[i].m), 0)
#stars = [suna, sunb, planet]
dt=60 * 60
while True:
    rate(1000)
    for i in range (1):
        planets[i].a = (G_force(suna.m, planets[i].m, planets[i].pos - suna.pos) + G_force(sunb.m, planets[i].m, planets[i].pos - sunb.pos)) / planets[i].m 
        planets[i].v += planets[i].a * dt
        planets[i].pos += planets[i].v * dt
    suna.a = G_force(suna.m, sunb.m, suna.pos - sunb.pos) / suna.m
    sunb.a = G_force(sunb.m, suna.m, sunb.pos - suna.pos) / sunb.m
    suna.v += suna.a * dt
    sunb.v += sunb.a * dt
    suna.pos += suna.v * dt
    sunb.pos += sunb.v * dt 