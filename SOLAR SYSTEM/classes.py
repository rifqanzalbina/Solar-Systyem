import itertools
import math
import turtle

class CelestialBody(turtle.Turtle):

    min_display_size = 20
    display_log_scale = 1.1

    def __init__(self,solar_system,mass,postition=(0,0),velocity=(0,0)):
        super().__init__()
        self.mass = mass
        self.setx(postition[0])
        self.sety(postition[1])
        self.velocity = velocity
        self.display_size = max(math.log(self.mass, self.display_log_scale),self.min_display_size)

        self.penup()
        self.hideturtle()

        solar_system.add_body(self)

    def draw(self):
        self.clear()
        self.dot(self.display_size)

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])

class Sun(CelestialBody):

    def __init__(self,solar_system,mass,position=(0,0),velocity=(0,0)):
        super().__init__(solar_system, mass, position, velocity)
        self.color("yellow")


class Planet(CelestialBody):

    colors = itertools.cycle(["grey","brown","blue","red","orange","yellow","green","sky"])

    def __init__(self, solar_system, mass, position=(0,0), velocity=(0,0)):
        super().__init__(solar_system, mass, position, velocity)
        self.color(next(Planet.colors))


class SolarSystem():

    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width,height)
        self.solar_system.bgcolor("black")

        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)

    def update_all_bodies(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

    @staticmethod
    def gravitational_orbit(first: CelestialBody, second: CelestialBody):

        g_force = first.mass * second.mass / first.distance(second) ** 2
        angle = first.towards(second)
        reverse = 1

        for body in first, second:
            acceleration = g_force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (body.velocity[0] + (reverse*acc_x), body.velocity[1] + (reverse*acc_y))
            reverse = -1

    def check_collision(self, first, second):
        if isinstance(first, Planet) and isinstance(second, Planet):
            return
        if first.distance(second) < first.display_size/2 + second.display_size/2:
            for body in first,second:
                if isinstance(body, Planet):
                    self.remove_body(body)
                    turtle.bye()

    def orbitals(self):
        bodies_copy = self.bodies.copy()
        for index, first in enumerate(bodies_copy):
            for second in bodies_copy[index+1:]:
                self.gravitational_orbit(first, second)
                self.check_collision(first, second)


def main():
    ...

if __name__ == '__main__':
    main()