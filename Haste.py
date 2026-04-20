from OpenGL.GL import *
from math import cos, sin, pi

class Haste:
    def __init__(self, raioint, raioext, altura, lados):

        self.raioint = raioint
        self.raioext = raioext
        self.altura = altura
        self.lados = lados

        self.vertices = []

        for i in range(self.lados):
            ang = 2 * pi * i / self.lados
            x = cos(ang) * self.raioint
            z = sin(ang) * self.raioint
            self.vertices.append((x, -self.altura / 2, z))

        for i in range(self.lados):
            ang = 2 * pi * i / self.lados
            x = cos(ang) * self.raioint
            z = sin(ang) * self.raioint
            self.vertices.append((x, +self.altura / 2, z))

        for i in range(self.lados):
            ang = 2 * pi * i / self.lados
            x = cos(ang) * self.raioext
            z = sin(ang) * self.raioext
            self.vertices.append((x, -self.altura / 2, z))

        for i in range(self.lados):
            ang = 2 * pi * i / self.lados
            x = cos(ang) * self.raioext
            z = sin(ang) * self.raioext
            self.vertices.append((x, +self.altura / 2, z))

    def draw(self):

        glBegin(GL_LINES)

        # base interna
        for i in range(self.lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[(i + 1) % self.lados])

        # topo interno
        for i in range(self.lados):
            glVertex3fv(self.vertices[i + self.lados])
            glVertex3fv(self.vertices[((i + 1) % self.lados) + self.lados])

        # laterais internas
        for i in range(self.lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[i + self.lados])

        # base externa
        for i in range(self.lados):
            glVertex3fv(self.vertices[i + 2 * self.lados])
            glVertex3fv(self.vertices[(i + 1) % self.lados + 2 * self.lados])

        # topo externo
        for i in range(self.lados):
            glVertex3fv(self.vertices[i + 3 * self.lados])
            glVertex3fv(self.vertices[((i + 1) % self.lados) + 3 * self.lados])

        # laterais externas
        for i in range(self.lados):
            glVertex3fv(self.vertices[i + 2 * self.lados])
            glVertex3fv(self.vertices[i + 3 * self.lados])

        # ligação base interno x externo
        for i in range(self.lados):
            glVertex3fv(self.vertices[i])
            glVertex3fv(self.vertices[i + 2 * self.lados])

        # ligação topo interno x externo
        for i in range(self.lados):
            glVertex3fv(self.vertices[i + self.lados])
            glVertex3fv(self.vertices[i + 3 * self.lados])

        glEnd()