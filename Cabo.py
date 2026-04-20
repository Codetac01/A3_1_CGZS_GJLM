from OpenGL.GL import *
from math import cos, sin, pi

class Cabo:
    def __init__(self, raio, altura, lados):
        self.vertices = []

        self.raio = raio
        self.altura = altura
        self.lados = lados

        # base
        for i in range(self.lados):
            ang = 2 * pi * i / self.lados
            x = cos(ang) * self.raio
            z = sin(ang) * self.raio
            self.vertices.append((x, -self.altura / 2, z))

        # topo
        for i in range(self.lados):
            ang = 2 * pi * i / self.lados
            x = cos(ang) * self.raio
            z = sin(ang) * self.raio
            self.vertices.append((x, self.altura / 2, z))

    def draw(self):
        glColor3f(0.7, 0.7, 0.7)
        glBegin(GL_LINES)

        # base
        for i in range(self.lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[(i + 1) % self.lados])

        # topo
        for i in range(self.lados):
            glVertex3fv(self.vertices[i + self.lados])
            glVertex3fv(self.vertices[((i + 1) % self.lados) + self.lados])

        # laterais
        for i in range(self.lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[i + self.lados])

        glEnd()