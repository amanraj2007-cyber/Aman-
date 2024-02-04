import turtle
import math
import time

class CelestialBody:
    def __init__(self, name, radius, distance_from_sun, orbital_period, color):
        self.name = name
        self.radius = radius  # in pixels
        self.distance_from_sun = distance_from_sun  # in pixels
        self.orbital_period = orbital_period if orbital_period != 0 else 1  # Avoid division by zero
        self.color = color
        self.angle = 0

        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(self.color)
        self.turtle.shapesize(stretch_wid=self.radius / 20, outline=None)
        self.turtle.penup()
        self.update_position()

    def update_position(self):
        if self.orbital_period == 0:
            return  # Skip update if orbital period is zero to avoid division by zero
        x = self.distance_from_sun * math.cos(math.radians(self.angle))
        y = self.distance_from_sun * math.sin(math.radians(self.angle))
        self.turtle.goto(x, y)
        self.angle += 360 / self.orbital_period

def animate_solar_system(bodies, steps, delay):
    for _ in range(steps):
        for body in bodies:
            body.update_position()
        turtle.update()
        time.sleep(delay)
        turtle.clear()

# Create celestial bodies
sun = CelestialBody("Sun", 50, 0, 0, "yellow")
earth = CelestialBody("Earth", 20, 150, 50, "blue")  # Increased radius
mars = CelestialBody("Mars", 15, 200, 100, "red")  # Increased radius

# Create a screen for the animation
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Animation")
screen.tracer(0)  # Turn off automatic screen updates

# Add celestial bodies to the solar system
solar_system = [sun, earth, mars]

# Animate the solar system
animate_solar_system(solar_system, steps=500, delay=0.05)

turtle.done()
