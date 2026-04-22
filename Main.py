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
machado_alabarda = Machado(1.3, 8, 6, 3, 0.3)
garra_alabarda = Garra()

camera = Camera()

# def para poder carregar as texturas
def load_texture(path):
    texture_surface = pygame.image.load(path)
    texture_data = pygame.image.tostring(texture_surface, "RGB", True)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0,
                 GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id


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

    # ativação da textura
    glEnable(GL_TEXTURE_2D)

    # cabo
    # textura madeira do cabo
    glBindTexture(GL_TEXTURE_2D, textura_madeira)
    cabo_alabarda.draw()


    glDisable(GL_TEXTURE_2D)

    # lança
    glPushMatrix()
    glTranslatef(0, cabo_alabarda.altura / 2, 0)
    lanca_alabarda.draw()
    glPopMatrix()

    # haste
    # textura metal para as partes de metal
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, textura_metal)

    glPushMatrix()
    glTranslatef(0, cabo_alabarda.altura * (23 / 60), 0)
    haste_alabarda.draw()
    glPopMatrix()


    glDisable(GL_TEXTURE_2D)

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

# carregador de textura
textura_madeira = load_texture("madeira_textura.jpg")
textura_metal = load_texture("textura_metal.jpg")

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