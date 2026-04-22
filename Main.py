import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Cabo import Cabo
from Lanca import Lanca
from Haste import Haste
from Machado import Machado
from Garra import Garra
from Camera import Camera

pygame.init()

screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Alabarda 3D')

cabo_alabarda = Cabo(1, 60, 8)
lanca_alabarda = Lanca(1, 3, 8)
haste_alabarda = Haste(1, 1.3, 3, 8)
machado_alabarda = Machado(1.3, 8, 6, 3)
garra_alabarda = Garra()

camera = Camera()

def initialise():
    glClearColor(*background_color)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    glLineWidth(2.5)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    camera.update()

    # cabo
    cabo_alabarda.draw()

    # lança
    glPushMatrix()
    glTranslatef(0, cabo_alabarda.altura / 2, 0)
    lanca_alabarda.draw()
    glPopMatrix()

    # haste
    glPushMatrix()
    glTranslatef(0, cabo_alabarda.altura * (23 / 60), 0)
    haste_alabarda.draw()
    glPopMatrix()

    # machado
    glPushMatrix()
    glTranslatef(0, cabo_alabarda.altura * (23 / 60), 0)
    machado_alabarda.draw()
    glPopMatrix()

    # garra / ponta triangular
    glPushMatrix()
    glTranslatef(0, cabo_alabarda.altura * (23 / 60), 0)
    glScalef(-1, 1, 1)
    glRotatef(-1, 0, 1, 0)
    glRotatef(-2, 0, 0, 1)
    garra_alabarda.draw()
    glPopMatrix()

done = False
initialise()

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()