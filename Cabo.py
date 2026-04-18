from OpenGL.GL import *
import pygame
from math import cos, sin, pi

class cabo:
    def __init__(self, largura, altura, profundidade):

        x = largura / 1
        y = altura / 2
        z = profundidade / 2

        self.vertices = []

        raio = 1
        self.altura = altura
        lados = 8

        glColor3f(0.7, 0.7, 0.7)
        # base
        for i in range(lados):
            ang = 2 * pi * i / lados
            x = cos(ang) * raio
            z = sin(ang) * raio
            self.vertices.append((x, -altura, z))

        # topo
        for i in range(lados):
            ang = 2 * pi * i / lados
            x = cos(ang) * raio
            z = sin(ang) * raio
            self.vertices.append((x, altura, z))

        self.triangles = [
            0, 2, 3, 0, 3, 1,
            6, 7, 5, 6, 5, 4,
            1, 3, 5, 1, 5, 7,
            2, 4, 5, 2, 5, 3,
            0, 6, 2, 2, 6, 0,
            7, 1, 6, 6, 1, 7,
        ]

        self.draw_type = GL_LINE_LOOP

    def draw(self):
        lados = 8

        glBegin(GL_LINES)

        # base
        for i in range(lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[(i + 1) % lados])

        # topo
        for i in range(lados):
            glVertex3fv(self.vertices[i + lados])
            glVertex3fv(self.vertices[((i + 1) % lados) + lados])

        # laterais
        for i in range(lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[i + lados])

        glEnd()