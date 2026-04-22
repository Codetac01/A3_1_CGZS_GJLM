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

        glColor3f(1, 1, 1)  # não apaga essa bosta freitas, se n, n aparece as textura

        glBegin(GL_QUADS)

        # adição da textura na parte de dentro
        for i in range(self.lados):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % self.lados]
            p3 = self.vertices[(i + 1) % self.lados + self.lados]
            p4 = self.vertices[i + self.lados]

            u1 = i / self.lados
            u2 = (i + 1) / self.lados

            glTexCoord2f(u1, 0)
            glVertex3fv(p1)

            glTexCoord2f(u2, 0)
            glVertex3fv(p2)

            glTexCoord2f(u2, 1)
            glVertex3fv(p3)

            glTexCoord2f(u1, 1)
            glVertex3fv(p4)

        # adição da textura na parte de fora
        for i in range(self.lados):
            p1 = self.vertices[i + 2 * self.lados]
            p2 = self.vertices[(i + 1) % self.lados + 2 * self.lados]
            p3 = self.vertices[(i + 1) % self.lados + 3 * self.lados]
            p4 = self.vertices[i + 3 * self.lados]

            u1 = i / self.lados
            u2 = (i + 1) / self.lados

            glTexCoord2f(u1, 0)
            glVertex3fv(p1)

            glTexCoord2f(u2, 0)
            glVertex3fv(p2)

            glTexCoord2f(u2, 1)
            glVertex3fv(p3)

            glTexCoord2f(u1, 1)
            glVertex3fv(p4)

        glEnd()

        # adicionei uma tampa pq se n ia ficar oco isso (tampa de baixo)
        glBegin(GL_POLYGON)
        for i in range(self.lados):
            x, y, z = self.vertices[i + 2 * self.lados]

            u = (cos(2 * pi * i / self.lados) + 1) / 2
            v = (sin(2 * pi * i / self.lados) + 1) / 2

            glTexCoord2f(u, v)
            glVertex3f(x, y, z)
        glEnd()

        # tampa de cima
        glBegin(GL_POLYGON)
        for i in range(self.lados):
            x, y, z = self.vertices[i + 3 * self.lados]

            u = (cos(2 * pi * i / self.lados) + 1) / 2
            v = (sin(2 * pi * i / self.lados) + 1) / 2

            glTexCoord2f(u, v)
            glVertex3f(x, y, z)
        glEnd()