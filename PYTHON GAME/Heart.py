import turtle
import math
import random


def setup_environment():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Ultimate Love")
    screen.tracer(0)
    return screen


class VortexParticle:
    def __init__(self):
        self.reset()
        self.history = [(self.x, self.y)] * 5

    COLOR = (1.0, 0.1, 0.15)  # bright red

    def reset(self):
        self.x = random.uniform(-400, 400)
        self.y = random.uniform(-300, 300)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.color = self.COLOR
        self.target_angle = random.uniform(0, 2 * math.pi)

    def update(self, t, mouse_x, mouse_y):
        self.history.append((self.x, self.y))
        self.history.pop(0)

        scale = 15 + 3 * math.sin(t * 0.03)
        heart_x = 16 * math.sin(self.target_angle) ** 3 * scale
        heart_y = (13 * math.cos(self.target_angle) - 5 * math.cos(2 * self.target_angle) -
                   2 * math.cos(3 * self.target_angle) - math.cos(4 * self.target_angle)) * scale

        dx, dy = heart_x - self.x, heart_y - self.y

        # pull toward its target point on the heart outline
        self.vx += dx * 0.002
        self.vy += dy * 0.002

        # sideways push -> gives the swirling "vortex" look
        self.vx += -dy * 0.001
        self.vy += dx * 0.001

        # friction so particles settle instead of oscillating forever
        self.vx *= 0.95
        self.vy *= 0.95

        # cap top speed
        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        max_speed = 8
        if speed > max_speed:
            self.vx = self.vx / speed * max_speed
            self.vy = self.vy / speed * max_speed

        self.x += self.vx
        self.y += self.vy

        # slow drift of target point -> gentle pulsing/shimmer
        self.target_angle += 0.002

    def get_color(self, t):
        return self.color


def main():
    screen = setup_environment()

    mouse_pos = [0, 0]

    def track_mouse(x, y):
        mouse_pos[0], mouse_pos[1] = x, y

    screen.onclick(track_mouse)

    particles = [VortexParticle() for _ in range(150)]

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.speed(0)

    t = 0

    def animate():
        nonlocal t
        pen.clear()
        for p in particles:
            p.update(t, mouse_pos[0], mouse_pos[1])
            color = p.get_color(t)
            pen.goto(p.x, p.y)
            pen.dot(6, color)
        t += 1
        screen.update()
        screen.ontimer(animate, 20)

    animate()
    screen.mainloop()


if __name__ == "__main__":
    main()