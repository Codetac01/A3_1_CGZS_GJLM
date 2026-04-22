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
        glColor3f(1, 1, 1)  # necessário pra textura freitas

        # face +z
        glBegin(GL_POLYGON)

        glTexCoord2f(0,1); glVertex3fv(self.base_topo_f)

        for i, v in enumerate(self.curva_cima_f):
            glTexCoord2f(i / len(self.curva_cima_f), 1)
            glVertex3fv(v)

        for i, v in enumerate(reversed(self.curva_baixo_f)):
            glTexCoord2f(i / len(self.curva_baixo_f), 0)
            glVertex3fv(v)

        glTexCoord2f(0,0); glVertex3fv(self.base_baixo_f)

        glEnd()

        # face -z
        glBegin(GL_POLYGON)

        glTexCoord2f(0,1); glVertex3fv(self.base_topo_t)

        for i, v in enumerate(self.curva_cima_t):
            glTexCoord2f(i / len(self.curva_cima_t), 1)
            glVertex3fv(v)

        for i, v in enumerate(reversed(self.curva_baixo_t)):
            glTexCoord2f(i / len(self.curva_baixo_t), 0)
            glVertex3fv(v)

        glTexCoord2f(0,0); glVertex3fv(self.base_baixo_t)

        glEnd()

        # lateral de cima e baixo
        glBegin(GL_QUADS)
        for i in range(len(self.curva_cima_f) - 1):

            # cima
            glTexCoord2f(0,0); glVertex3fv(self.curva_cima_f[i])
            glTexCoord2f(1,0); glVertex3fv(self.curva_cima_f[i + 1])
            glTexCoord2f(1,1); glVertex3fv(self.curva_cima_t[i + 1])
            glTexCoord2f(0,1); glVertex3fv(self.curva_cima_t[i])

            # baixo
            glTexCoord2f(0,0); glVertex3fv(self.curva_baixo_f[i])
            glTexCoord2f(1,0); glVertex3fv(self.curva_baixo_f[i + 1])
            glTexCoord2f(1,1); glVertex3fv(self.curva_baixo_t[i + 1])
            glTexCoord2f(0,1); glVertex3fv(self.curva_baixo_t[i])

        glEnd()

        # lateral da ponta + encaixe
        glBegin(GL_QUADS)

        # ponta
        glTexCoord2f(0,0); glVertex3fv(self.curva_cima_f[-1])
        glTexCoord2f(1,0); glVertex3fv(self.curva_baixo_f[-1])
        glTexCoord2f(1,1); glVertex3fv(self.curva_baixo_t[-1])
        glTexCoord2f(0,1); glVertex3fv(self.curva_cima_t[-1])

        # encaixe
        glTexCoord2f(0,0); glVertex3fv(self.base_topo_f)
        glTexCoord2f(1,0); glVertex3fv(self.base_baixo_f)
        glTexCoord2f(1,1); glVertex3fv(self.base_baixo_t)
        glTexCoord2f(0,1); glVertex3fv(self.base_topo_t)

        glEnd()