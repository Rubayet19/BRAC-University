from OpenGL.GL import *
from OpenGL.GLUT import *
import math

def midpoint_circle(r, center_x, center_y):
    original_points = [] #zone 1 points

    x = 0
    y = r

    original_points.append((x , y))

    d = 1-r

    while x < y-1:
        if d >= 0:
            # (SE)
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1

        else:
            # (E)
            d = d + 2 * x + 3
            x = x + 1
        original_points.append((x, y))

    circle_points = get_other_points(original_points, center_x, center_y)
    return circle_points

# for other zones
def get_other_points (original_points, center_x, center_y):
    other_points = []
    zone0_array = []
    zone1_array = []
    zone2_array = []
    zone3_array = []
    zone4_array = []
    zone5_array = []
    zone6_array = []
    zone7_array = []

    for s in range(len(original_points)):
        x, y = original_points[s][0], original_points[s][1]
        zone0_array.append((y+ center_x, x+ center_y))
        zone1_array.append((x+ center_x, y+ center_y))
        zone2_array.append((-x+ center_x, y+ center_y))
        zone3_array.append((-y+ center_x, x+ center_y))
        zone4_array.append((-y+ center_x, -x+ center_y))
        zone5_array.append((-x+ center_x, -y+ center_y))
        zone6_array.append((x+ center_x, -y+ center_y))
        zone7_array.append((y+ center_x, -x+ center_y))

    other_points.append(zone0_array)
    other_points.append(zone1_array)
    other_points.append(zone2_array)
    other_points.append(zone3_array)
    other_points.append(zone4_array)
    other_points.append(zone5_array)
    other_points.append(zone6_array)
    other_points.append(zone7_array)

    return other_points

def get_other_centers(radius):
    center = math.ceil(radius * math.cos(math.pi/4))
    center1 = (center,center)
    center2 = (-center, center)
    center3 = (center, -center)
    center4 = (-center, -center)
    return center1, center2, center3, center4

def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()


def iterate():
    glViewport(0, 0, 600, 600) #how much space occupied in window
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-600, 600, -600, 600, 0.0, 1.0) #x,y and z axis
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)


    # Largest Circle
    radius1 = 500
    centerX = 0
    centerY = 0
    pixels = midpoint_circle(radius1, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Top Circle
    radius2 = (radius1/2)
    centerX = 0
    centerY = (radius1/2)
    pixels = midpoint_circle(radius2, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Bottom Circle
    radius3 = (radius1/2)
    centerX = 0
    centerY = -(radius1/2)
    pixels = midpoint_circle(radius3, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Left Circle
    radius4 = (radius1/2)
    centerX = -(radius1/2)
    centerY = 0
    pixels = midpoint_circle(radius4, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Right Circle
    radius5 = (radius1/2)
    centerX = (radius1/2)
    centerY = 0
    pixels = midpoint_circle(radius5, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    # Other 4 Circles
    center1, center2 , center3, center4 = get_other_centers(radius1/2)

    radius6 = (radius1 / 2)
    (centerX, centerY) = center1
    pixels = midpoint_circle(radius6, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    radius7 = (radius1 / 2)
    (centerX, centerY) = center2
    pixels = midpoint_circle(radius7, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    radius8 = (radius1 / 2)
    (centerX, centerY) = center3
    pixels = midpoint_circle(radius8, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)

    radius9 = (radius1 / 2)
    (centerX, centerY) = center4
    pixels = midpoint_circle(radius9, centerX, centerY)
    for i in range(len(pixels)):
        for p in pixels[i]:
            draw_points(*p)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 3") #window name
glutDisplayFunc(showScreen)

glutMainLoop()