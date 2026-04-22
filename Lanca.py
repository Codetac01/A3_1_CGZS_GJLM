from OpenGL.GL import *
from math import cos, sin, pi

class Lanca:
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
        glColor3f(1, 1, 1)  # necessário pra textura aparecer

        # laterais da ponta
        glBegin(GL_TRIANGLES)

        for i in range(self.lados):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % self.lados]
            p3 = self.topo

            u1 = i / self.lados
            u2 = (i + 1) / self.lados

            glTexCoord2f(u1, 0)
            glVertex3fv(p1)

            glTexCoord2f(u2, 0)
            glVertex3fv(p2)

            glTexCoord2f((u1 + u2) / 2, 1)
            glVertex3fv(p3)

        glEnd()

        # base da lança
        glBegin(GL_POLYGON)
        for i in range(self.lados):
            x, y, z = self.vertices[i]

            u = (cos(2 * pi * i / self.lados) + 1) / 2
            v = (sin(2 * pi * i / self.lados) + 1) / 2

            glTexCoord2f(u, v)
            glVertex3f(x, y, z)

        glEnd()