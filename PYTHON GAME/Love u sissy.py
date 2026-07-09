import turtle
import math
import random


def setup_environment():
    screen = turtle.Screen()
    screen.setup(width=900, height=750)
    screen.bgcolor("#000000")
    screen.title("Love You So Much Sissy <3")
    screen.tracer(0)
    return screen


class VortexParticle:
    COLORS = [
        (1.0, 0.1, 0.15),   # bright red
        (1.0, 0.45, 0.65),  # soft pink
    ]

    def __init__(self, target_angle):
        self.target_angle = target_angle
        self.x = random.uniform(-400, 400)
        self.y = random.uniform(-300, 300)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.color = random.choice(self.COLORS)
        self.twinkle_offset = random.uniform(0, 2 * math.pi)
        # personal orbit settings for the "alive but static" phase
        self.orbit_radius = random.uniform(1.5, 4)
        self.orbit_speed = random.uniform(0.03, 0.07)
        self.orbit_phase = random.uniform(0, 2 * math.pi)

    def heart_point(self, scale):
        hx = 16 * math.sin(self.target_angle) ** 3 * scale
        hy = (13 * math.cos(self.target_angle) - 5 * math.cos(2 * self.target_angle) -
              2 * math.cos(3 * self.target_angle) - math.cos(4 * self.target_angle)) * scale
        return hx, hy

    def update_forming(self, scale):
        hx, hy = self.heart_point(scale)
        dx, dy = hx - self.x, hy - self.y
        self.vx += dx * 0.004
        self.vy += dy * 0.004
        self.vx *= 0.85
        self.vy *= 0.85
        self.x += self.vx
        self.y += self.vy

    def update_settled(self, t, scale):
        hx, hy = self.heart_point(scale)
        angle = t * self.orbit_speed + self.orbit_phase
        self.x = hx + self.orbit_radius * math.cos(angle)
        self.y = hy + self.orbit_radius * math.sin(angle)

    def get_color(self, t):
        twinkle = 0.15 * (1 + math.sin(t * 0.05 + self.twinkle_offset))
        r, g, b = self.color
        return (min(1.0, r + twinkle), min(1.0, g + twinkle), min(1.0, b + twinkle))


def write_message(pen):
    pen.clear()  # avoid stacked text if the script is re-run in the same session
    pen.penup()
    pen.goto(0, -320)
    pen.color("#ffb6c9")
    pen.write("For my sister, with all my love <3", align="center",
               font=("Georgia", 20, "italic"))


def main():
    screen = setup_environment()

    num_particles = 150
    particles = [
        VortexParticle(2 * math.pi * i / num_particles)
        for i in range(num_particles)
    ]

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.speed(0)

    label_pen = turtle.Turtle()
    label_pen.hideturtle()
    label_pen.penup()
    label_pen.speed(0)
    write_message(label_pen)

    t = 0
    settle_frames = 130
    fade_frames = 40
    final_scale = 15

    def animate():
        nonlocal t
        pen.clear()

        if t < settle_frames:
            scale = 15 + 4 * math.sin(t * 0.08)
            for p in particles:
                p.update_forming(scale)
                pen.goto(p.x, p.y)
                pen.dot(6, p.get_color(t))
        else:
            blend = min(1.0, (t - settle_frames) / fade_frames)
            for p in particles:
                hx, hy = p.heart_point(final_scale)
                p.update_settled(t, final_scale)
                sx = hx * (1 - blend) + p.x * blend
                sy = hy * (1 - blend) + p.y * blend
                pen.goto(sx, sy)
                pen.dot(6, p.get_color(t))

        t += 1
        screen.update()
        screen.ontimer(animate, 20)

    animate()
    screen.mainloop()


if __name__ == "__main__":
    main()