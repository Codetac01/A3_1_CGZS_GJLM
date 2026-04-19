from OpenGL.GL import *
from math import cos, sin, pi

class lanca:
    def __init__(self, raio, altura, lados):
        self.vertices = []

        self.raio = raio
        self.altura = altura
        self.lados = lados

        # base (círculo)
        for i in range(self.lados):
            ang = 2 * pi * i / self.lados
            x = cos(ang) * self.raio
            z = sin(ang) * self.raio
            self.vertices.append((x, 0, z))

        # ponta
        self.topo = (0, self.altura, 0)

    def draw(self):
        glColor3f(0.8, 0.8, 0.8)
        glBegin(GL_LINES)

        # base (círculo)
        for i in range(self.lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[(i + 1) % self.lados])

        # linhas até a ponta
        for i in range(self.lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.topo)

        glEnd()