from OpenGL.GL import *
from math import sqrt


class Machado:
    def __init__(self, raio, altura, pontos, largura, espessura):

        self.raio = raio
        self.altura = altura
        self.pontos = pontos
        self.largura = largura
        self.espessura = espessura

        z_frente = self.espessura / 2
        z_tras = -self.espessura / 2

        self.base_topo_f = (self.raio, self.altura / 2, z_frente)
        self.base_baixo_f = (self.raio, -self.altura / 2, z_frente)
        self.base_topo_t = (self.raio, self.altura / 2, z_tras)
        self.base_baixo_t = (self.raio, -self.altura / 2, z_tras)

        self.curva_cima_f = []
        self.curva_baixo_f = []
        self.curva_cima_t = []
        self.curva_baixo_t = []

        for i in range(self.pontos):
            t = i / (self.pontos - 1)

            x = self.raio + t * self.largura
            y = self.altura / 2 * sqrt(1 - t ** 2)

            self.curva_cima_f.append((x, y, z_frente))
            self.curva_baixo_f.append((x, -y, z_frente))

            self.curva_cima_t.append((x, y, z_tras))
            self.curva_baixo_t.append((x, -y, z_tras))

    def draw(self):

        glColor3f(0.5, 0.5, 0.5)

        # face +z
        glBegin(GL_POLYGON)
        glVertex3fv(self.base_topo_f)

        for v in self.curva_cima_f:
            glVertex3fv(v)

        for v in reversed(self.curva_baixo_f):
            glVertex3fv(v)

        glVertex3fv(self.base_baixo_f)

        # face -z
        glVertex3fv(self.base_topo_t)

        for v in self.curva_cima_t:
            glVertex3fv(v)

        for v in reversed(self.curva_baixo_t):
            glVertex3fv(v)

        glVertex3fv(self.base_baixo_t)
        glEnd()

        glBegin(GL_QUADS)
        for i in range(len(self.curva_cima_f) - 1):
            # lateral de cima
            glVertex3fv(self.curva_cima_f[i])
            glVertex3fv(self.curva_cima_f[i + 1])
            glVertex3fv(self.curva_cima_t[i + 1])
            glVertex3fv(self.curva_cima_t[i])

            # lateral de baixo
            glVertex3fv(self.curva_baixo_f[i])
            glVertex3fv(self.curva_baixo_f[i + 1])
            glVertex3fv(self.curva_baixo_t[i + 1])
            glVertex3fv(self.curva_baixo_t[i])
        glEnd()

         # lateral da ponta
        glBegin(GL_QUADS)
        glVertex3fv(self.curva_cima_f[-1])
        glVertex3fv(self.curva_baixo_f[-1])
        glVertex3fv(self.curva_baixo_t[-1])
        glVertex3fv(self.curva_cima_t[-1])

        # lateral do encaixe
        glVertex3fv(self.base_topo_f)
        glVertex3fv(self.base_baixo_f)
        glVertex3fv(self.base_baixo_t)
        glVertex3fv(self.base_topo_t)
        glEnd()