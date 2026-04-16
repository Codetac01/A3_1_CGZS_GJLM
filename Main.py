import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Cabo import cabo

pygame.init()

# configurações
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Cubo 3D')

cubo = cabo()

def initialise():

    # projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -5)

    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # rotação simples
    glRotatef(1, 1, 1, 1)

    cubo.draw()


done = False
initialise()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()