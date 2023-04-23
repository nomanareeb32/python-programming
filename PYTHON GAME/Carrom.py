import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, linspace

plt.figure(figsize=(8, 8))
plt.plot(0, 0, marker='o', color='black')
plt.plot(1, 0, marker='o', color='black')
plt.plot(1, 1, marker='o', color='black')
plt.plot(0, 1, marker='o', color='black')
plt.plot(
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0]
)
# points of second line
plt.plot(0.08, 0.08, marker='o', color='red')
plt.plot(0.92, 0.08, marker='o', color='red')
plt.plot(0.92, 0.92, marker='o', color='red')
plt.plot(0.08, 0.92, marker='o', color='red')
plt.plot(
    [0.08, 0.92, 0.92, 0.08, 0.08],
    [0.08, 0.08, 0.92, 0.92, 0.08]
)
# create four goals on each corner
plt.plot(0.13, 0.13, marker='o', markersize=30, color='black')
plt.plot(0.87, 0.13, marker='o', markersize=30, color='black')
plt.plot(0.87, 0.87, marker='o', markersize=30, color='black')
plt.plot(0.13, 0.87, marker='o', markersize=30, color='black')
# create point in the middle
plt.plot(0.5, 0.5, marker='o', markersize=10, color='red')
# create round circle
angles = np.linspace(0, 2 * pi, 100)
r = 0.1
xs = r * cos(angles)
ys = r * sin(angles)
plt.plot(xs + 0.5, ys + 0.5, color='grey')
## draw line on left bottom from middle to nearly goal
plt.plot(
    [0.38, 0.18],
    [0.38, 0.18],
    color='grey'
)
# create round circle
small_angles_1 = np.linspace(6 / 8 * 2 * pi, 12 / 8 * 2 * pi, 100)
r1 = 0.05
xs = r1 * cos(small_angles_1)
ys = r1 * sin(small_angles_1)
plt.plot(xs + 0.35, ys + 0.35, color='grey')
# points on the left bottom circle
x1 = r1 * cos(pi) + 0.35
y1 = r1 * sin(pi) + 0.35
plt.plot(x1, y1, color='grey', marker='o', markersize=5)
x2 = r1 * cos(6 / 8 * 2 * pi) + 0.35
y2 = r1 * sin(6 / 8 * 2 * pi) + 0.35
plt.plot(x2, y2, color='grey', marker='o', markersize=5)
## draw line on right bottom from middle to nearly goal
plt.plot(
    [0.62, 0.82],
    [0.38, 0.18],
    color='grey'
)
# create round circle on the right side
small_angles_2 = np.linspace(2 * pi, 14 / 8 * 2 * pi, 100)
xs = r1 * cos(small_angles_2)
ys = r1 * sin(small_angles_2)
plt.plot(xs + 0.65, ys + 0.35, color='grey')
# points on the right bottom circle
x1 = r1 * cos(2 * pi) + 0.645
y1 = r1 * sin(2 * pi) + 0.35
plt.plot(x1, y1, color='grey', marker='o', markersize=5)
x2 = r1 * cos(14 / 8 * 2 * pi) + 0.645
y2 = r1 * sin(14 / 8 * 2 * pi) + 0.35
plt.plot(x2, y2, color='grey', marker='o', markersize=5)
## draw line from right top to middle to nearly goal
plt.plot(
    [0.62, 0.82],
    [0.62, 0.82],
    color='grey'
)
# create round circle on the right top side
small_angles_3 = np.linspace(pi / 2, 2 * pi, 100)
xs = r1 * cos(small_angles_3)
ys = r1 * sin(small_angles_3)
plt.plot(xs + 0.65, ys + 0.65, color='grey')
# points on the right top circle
x1 = r1 * cos(pi / 2) + 0.645
y1 = r1 * sin(pi / 2) + 0.65
plt.plot(x1, y1, color='grey', marker='o', markersize=5)
x2 = r1 * cos(2 * pi) + 0.645
y2 = r1 * sin(2 * pi) + 0.65
plt.plot(x2, y2, color='grey', marker='o', markersize=5)
## draw line from left top to middle to nearly goal
plt.plot(
    [0.38, 0.18],
    [0.62, 0.82],
    color='grey'
)
# create round circle on the left top side
small_angles_4 = np.linspace(pi, 10 / 8 * 2 * pi, 100)
xs = r1 * cos(small_angles_4)
ys = r1 * sin(small_angles_4)
plt.plot(xs + 0.35, ys + 0.65, color='grey')
# points on the left top circle
x1 = r1 * cos(pi) + 0.35
y1 = r1 * sin(pi) + 0.65
plt.plot(x1, y1, color='grey', marker='o', markersize=5)
x2 = r1 * cos(10 / 8 * 2 * pi) + 0.35
y2 = r1 * sin(10 / 8 * 2 * pi) + 0.65
plt.plot(x2, y2, color='grey', marker='o', markersize=5)
##First horizental design
plt.plot([0.26, 0.75], [0.21, 0.21], color='black')
plt.plot([0.25, 0.75], [0.24, 0.24], color='black', alpha=0.1)
plt.plot(0.25, 0.225, color='brown', marker='o', markersize=12)
plt.plot(0.75, 0.225, color='brown', marker='o', markersize=12)
##right vertical design
plt.plot([0.77, 0.77], [0.26, 0.76], color='green', alpha=0.1)
plt.plot([0.80, 0.80], [0.25, 0.76], color='black')
plt.plot(0.785, 0.25, color='brown', marker='o', markersize=12)
plt.plot(0.785, 0.76, color='brown', marker='o', markersize=12)
##left horizental design
plt.plot([0.76, 0.26], [0.76, 0.76], color='black', alpha=0.1)
plt.plot([0.76, 0.26], [0.79, 0.79], color='black')
plt.plot(0.75, 0.78, color='brown', marker='o', markersize=12)
plt.plot(0.25, 0.78, color='brown', marker='o', markersize=12)
##down vertical design
plt.plot([0.24, 0.24], [0.74, 0.27], color='black', alpha=0.1)
plt.plot([0.21, 0.21], [0.74, 0.27], color='black')
plt.plot(0.225, 0.74, color='brown', marker='o', markersize=12)
plt.plot(0.225, 0.26, color='brown', marker='o', markersize=12)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis("off")
plt.show()
