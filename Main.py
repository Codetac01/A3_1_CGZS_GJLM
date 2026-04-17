import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Cabo import cabo
from Camera import Camera

pygame.init()

# configurações
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Cubo 3D')


cabo_alabarda = cabo(1, 30, 50)

camera = Camera()

def initialise():

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()


    camera.update()


    # glRotatef(1, 1, 1, 1)

    cabo_alabarda.draw()


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