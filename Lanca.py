from OpenGL.GL import *
from math import cos, sin, pi

class Lanca:
    def __init__(self, altura, raio, lados=8):

        self.vertices = []

        # base (círculo)
        for i in range(lados):
            ang = 2 * pi * i / lados
            x = cos(ang) * raio
            z = sin(ang) * raio
            self.vertices.append((x, 0, z))

        # ponta
        self.topo = (0, altura, 0)

        self.lados = lados

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