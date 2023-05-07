import time
from classes import SolarSystem, Sun, Planet

solar_system = SolarSystem(width = 1.0, height = 1.0)

sun_x = Sun( solar_system= solar_system, mass= 10000, position=(-200, 0), velocity=(0,3.5))
sun_y = Sun( solar_system= solar_system, mass= 10000, position=(200, 0), velocity=(0,-3.5))

planet_x = Planet(solar_system,mass=22, position=(50,0) ,velocity=(0, 11))
planet_y = Planet(solar_system,mass=3, position=(-350,0),velocity=(0, -10))

while 1:
    solar_system.orbitals()
    solar_system.update_all_bodies()
    time.sleep(0.000000001)