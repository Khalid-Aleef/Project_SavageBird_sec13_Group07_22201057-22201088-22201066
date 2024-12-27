import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y, b):
    glPointSize(b)  # Pixel size
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # Pixel position
    glEnd()

def score_show(str, x, y):
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for i in str:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(i))

global score ,sp_cir
game_pause = False
sp_cir = []
score = 0
lis = []
zones = []
fire = []
button = []
pillar=[]

def draw_midpoint(x1, y1, x2, y2):
    global lis
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    E = 2 * dy
    NE = 2 * (dy - dx)
    x = x1
    y = y1
    line_points = []

    while x <= x2:
        line_points.append([x, y])
        if d > 0:
            d += NE
            y += 1
            x += 1
        else:
            d += E
            x += 1
    return line_points


def zone_detection(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        if dx < 0 and dy < 0:
            return 4

        if dx < 0 and dy >= 0:
            return 3
        if dx >= 0 and dy < 0:
            return 7
    else:
        if dx >= 0 and dy < 0:
            return 6
        if dx < 0 and dy >= 0:
            return 2

        if dx < 0 and dy < 0:
            return 5

        if dx >= 0 and dy >= 0:
            return 1


def add_buttonline(x1, y1, x2, y2):
    global button
    z = zone_detection(x1, y1, x2, y2)
    button.append([z, x1, y1, x2, y2])


# back_button
add_buttonline(-480, 480, -460, 480)
add_buttonline(-480, 480, -470, 490)
add_buttonline(-480, 480, -470, 470)

# play and pause
add_buttonline(-10, 490, -10, 470)
add_buttonline(10, 490, 10, 470)

# quit
add_buttonline(490, 490, 460, 460)
add_buttonline(460, 490, 490, 460)


def add_midline(x1, y1, x2, y2):
    global zones
    z = zone_detection(x1, y1, x2, y2)
    zones.append([z, x1, y1, x2, y2])


def add_pillar(x1, y1, x2, y2):
    global pillar
    z=zone_detection(x1, y1, x2, y2)
    pillar.append([z, x1, y1, x2, y2])


# bird
add_midline(-433, 198, -433, 174)
add_midline(-433, 198, -395, 194)
add_midline(-433, 174, -395, 194)
add_midline(-395, 194, -356, 219)
add_midline(-356, 219, -351, 247)
add_midline(-351, 247, -315, 253)
add_midline(-315, 253, -325, 227)
add_midline(-325, 227, -313, 210)
add_midline(-313, 210, -349, 182)
add_midline(-349, 182, -386, 172)
add_midline(-386, 172, -395, 194)
add_midline(-373, 201, -386, 188)
add_midline(-386, 188, -356, 188)
add_midline(-356, 188, -344, 201)
add_midline(-334, 241, -334, 241)


#pillar
rany = random.randint(-300,300)

add_pillar(300,500,300,rany)
add_pillar(400,500,400,rany)
add_pillar(300,rany,400,rany)

add_pillar(300,-500,300,rany-400)
add_pillar(400,-500,400,rany-400)
add_pillar(300,rany-400,400,rany-400)









def fire_circle(r, cx, cy):
    global fire
    fire.append([r, cx, cy])



def sp_circle(r, cx, cy):
    global sp_cir
    if len(sp_cir) < 1:
        sp_cir.append([r, cx, cy])


def midpoint_circle(r):
    cir = []
    d = 1 - r
    x = 0
    y = r
    while x <= y:
        cir.append((x, y))
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

    c_lis = []
    for i in cir:  # Zone 1
        c_lis.append((i[0], i[1]))
    for i in cir:  # Zone 6
        c_lis.append((i[0], - i[1]))
    for i in cir:  # Zone 5
        c_lis.append((- i[0], - i[1]))
    for i in cir:  # Zone 2
        c_lis.append((- i[0], i[1]))
    for i in cir:  # Zone 0
        c_lis.append((i[1], i[0]))
    for i in cir:  # Zone 3
        c_lis.append((- i[1], i[0]))
    for i in cir:  # Zone 4
        c_lis.append((- i[1], - i[0]))
    for i in cir:  # Zone 7
        c_lis.append((i[1], - i[0]))

    return c_lis

def keyboardListener(key, x, y):
    global zones, game_pause
    if game_pause:
        return
    else:
        if key==b'w':
            for z in zones:
                z[2] += 90
                z[4] += 90


        elif key == b" ":
            fire_circle(5, zones[8][1], zones[8][2])

        glutPostRedisplay()


def mouseListener(buttons, state, x, y):
    global  fire, sp_cir, score, zones, game_pause,pillar
    if buttons == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            if x > 0 and x < 30:
                    if y > 0 and y < 30:
                        sp_cir = []
                        score = 0
                        lis = []
                        zones = []
                        fire = []
                        button = []
                        pillar = []
                        # bird
                        add_midline(-433, 198, -433, 174)
                        add_midline(-433, 198, -395, 194)
                        add_midline(-433, 174, -395, 194)
                        add_midline(-395, 194, -356, 219)
                        add_midline(-356, 219, -351, 247)
                        add_midline(-351, 247, -315, 253)
                        add_midline(-315, 253, -325, 227)
                        add_midline(-325, 227, -313, 210)
                        add_midline(-313, 210, -349, 182)
                        add_midline(-349, 182, -386, 172)
                        add_midline(-386, 172, -395, 194)
                        add_midline(-373, 201, -386, 188)
                        add_midline(-386, 188, -356, 188)
                        add_midline(-356, 188, -344, 201)
                        add_midline(-334, 241, -334, 241)

                        # pillar
                        rany = random.randint(-300, 300)

                        add_pillar(300, 500, 300, rany)
                        add_pillar(400, 500, 400, rany)
                        add_pillar(300, rany, 400, rany)

                        add_pillar(300, -500, 300, rany - 400)
                        add_pillar(400, -500, 400, rany - 400)
                        add_pillar(300, rany - 400, 400, rany - 400)
                        glutPostRedisplay()



            if x > 230 and x < 270:
                if y > 0 and y < 20:
                    if game_pause == False:
                        game_pause = True


                    else:
                        game_pause = False

            if x > 470 and x < 500:
                if y > 0 and y < 20:
                    glutLeaveMainLoop()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500.0, 500.0, -500.0, 500.0, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_line(x1, y1, x2, y2, z,b=1):
    global lis
    if z == 0:
        lis = draw_midpoint(x1, y1, x2, y2)
        for i in lis:
            xd = i[0]
            yd = i[1]
            draw_points(xd, yd,b)

    if z == 1:
        lis = draw_midpoint(y1, x1, y2, x2)
        for i in lis:
            xd = i[1]
            yd = i[0]
            draw_points(xd, yd,b)

    if z == 2:
        lis = draw_midpoint(y1, -x1, y2, -x2)
        for i in lis:
            xd = -i[1]
            yd = i[0]
            draw_points(xd, yd,b)

    if z == 3:
        lis = draw_midpoint(-x1, y1, -x2, y2)
        for i in lis:
            xd = -i[0]
            yd = i[1]
            draw_points(xd, yd,b)

    if z == 4:
        lis = draw_midpoint(-x1, -y1, -x2, -y2)
        for i in lis:
            xd = -i[0]
            yd = -i[1]
            draw_points(xd, yd,b)

    if z == 5:
        lis = draw_midpoint(-y1, -x1, -y2, -x2)
        for i in lis:
            xd = -i[1]
            yd = -i[0]
            draw_points(xd, yd,b)

    if z == 6:
        lis = draw_midpoint(-y1, x1, -y2, x2)
        for i in lis:
            xd = i[1]
            yd = -i[0]
            draw_points(xd, yd,b)

    if z == 7:
        lis = draw_midpoint(x1, -y1, x2, -y2)
        for i in lis:
            xd = i[0]
            yd = -i[1]
            draw_points(xd, yd,b)


def animate():
    if game_pause == True:
        return

    glutPostRedisplay()
    global  lis, fire, score, sp_cr_count,zones,pillar


    for i in sp_cir:

        if i[0] >= 100:
            i[0] -= 10
        elif i[0] <= 70:
            i[0] += 10
        else:
            if i[0] < 50:
                i[0] += 10
            else:
                i[0] -= 10
        i[1] -= 1
        if i[2] < -500:
            sp_cir.pop(0)

    #bird
    for z in zones:
        z[2] -= 2
        z[4] -= 2

        if z[2]<=-500:
            print("Game Over.")
            glutLeaveMainLoop()

    #for pillar animation
    for p in pillar:
        p[1]-=1
        p[3]-=1

        if p[3]<-500:
            pillar.remove(p)
            if len(pillar)<12:
                score+=1
                print("score:",score)


        if p[3]<-100:
            if len(pillar)<12:

             rany = random.randint(-300, 300)
             if score != 0 and score % 4 == 0:
                 sp_circle(100, 450, rany-200)

             add_pillar(400, 500, 400, rany)
             add_pillar(500, 500, 500, rany)
             add_pillar(400, rany, 500, rany)

             add_pillar(400, -500, 400, rany - 400)
             add_pillar(500, -500, 500, rany - 400)
             add_pillar(400, rany - 400, 500, rany - 400)

    #for fire animation
    for j in fire:
        j[1] += 2
        if j[2] > 500:
            fire.remove(j)


    glutPostRedisplay()


def showScreen():
    global score, sp_cir
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # blue back button
    glColor3f(0.0, 0.0, 1.0)  # Blue
    for i in button[:3]:  # First three lines for the Back button
        draw_line(i[1], i[2], i[3], i[4], i[0])

    glColor3f(1.0, 1.0, 0.0)  # Red
    for i in button[3:5]:
        draw_line(i[1], i[2], i[3], i[4], i[0])

    # red quit button
    glColor3f(1.0, 0.0, 0.0)  # Red
    for i in button[5:]:  # Last two lines for the Quit button
        draw_line(i[1], i[2], i[3], i[4], i[0])

    # Bird Draw
    glColor3f(1.0, 1.0, 0.0)
    for i in zones:
        draw_line(i[1], i[2], i[3], i[4], i[0])

    glColor3f(1,1,1)
    for i in pillar:
        draw_line(i[1], i[2], i[3], i[4], i[0],5) #5 is thikness


    #collide with pillar
    for p in pillar:
        for z, x1, y1, x2, y2 in zones:
            if -433<= p[1] <= -313 and y1 <= p[2] <= y2 or p[2] >= y1 >= p[4] and -433<= p[1] <= -313 or p[2] <= y1 <= p[4] and -433<= p[1] <= -313:
                 print("Your Bird is dead")
                 glutLeaveMainLoop()
                 break

# sp_cir drawing.
    collisonflag_sp = False
    for r, cx, cy in sp_cir:
        circle_drawpoints_sp = midpoint_circle(r)
        for x, y in circle_drawpoints_sp:
            glColor3f(1, 0, 0)
            draw_points(cx + x, cy + y,3)

        #bird collide with sp_circle
        for z, x1, y1, x2, y2 in zones:
            for i in circle_drawpoints_sp:
                    if x1 < i[0] + cx < x2:
                        glutLeaveMainLoop()
                        print("Savage Bird is no more")
                        print("Game Over")
                        collisonflag_sp = True
                        break
            if collisonflag_sp:
                break
        if collisonflag_sp:
            break


    # fire circle drawing
    for r, cx, cy in fire:
        circle_drawpoint = midpoint_circle(r)
        for x, y in circle_drawpoint:
            glColor3f(0.0, 0.4, 0.6)
            draw_points(cx + x, cy + y,1)

        # fire collide with sp_circle
        for r2, cx2, cy2 in sp_cir:
            distance = ((cx - cx2) ** 2 + (cy - cy2) ** 2) ** 0.5
            if distance <= (r + r2):
                score += 5
                print("score:", score)
                sp_cir.remove([r2, cx2, cy2])
                fire.remove([r, cx, cy])

        for p in pillar:
            for i in circle_drawpoint:
                m=i[0] + cx
                n=i[1]+cy
                if m>= p[1]:
                    if  p[2] >= n >= p[4] or p[2]<n and p[4]<n:
                      fire.remove([r,cx,cy])
                      break
            break
    glColor3f(1, 1, 1)  # White text
    score_show(f"Score: {score}", -480, -470)
    glutSwapBuffers()
def init():
    glClearColor(0,0,0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -500, 500)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutIdleFunc(animate)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Group07_Savage Bird_22201057,22201088,22201066")
init()
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutDisplayFunc(showScreen)

glutMainLoop()