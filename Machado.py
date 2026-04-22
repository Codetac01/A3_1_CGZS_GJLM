from OpenGL.GL import *
from math import sqrt


class Machado:
    def __init__(self, raio, altura, pontos, largura):
        meio = altura / 2
        self.raio = raio
        self.espessura = 0.3

        z_front = self.espessura / 2
        z_back = -self.espessura / 2

        # base (encaixe)
        self.base_top_f = (self.raio, meio, z_front)
        self.base_bot_f = (self.raio, -meio, z_front)

        self.base_top_b = (self.raio, meio, z_back)
        self.base_bot_b = (self.raio, -meio, z_back)

        # curvas
        self.curva_cima_f = []
        self.curva_baixo_f = []
        self.curva_cima_b = []
        self.curva_baixo_b = []

        for i in range(pontos):
            t = i / (pontos - 1)

            x = self.raio + t * largura
            y = meio * sqrt(1 - t**2)

            self.curva_cima_f.append((x, y, z_front))
            self.curva_baixo_f.append((x, -y, z_front))

            self.curva_cima_b.append((x, y, z_back))
            self.curva_baixo_b.append((x, -y, z_back))

    def draw(self):
        glColor3f(0.5, 0.5, 0.5)

        # face da frente
        glBegin(GL_POLYGON)
        glVertex3fv(self.base_top_f)

        for v in self.curva_cima_f:
            glVertex3fv(v)

        for v in reversed(self.curva_baixo_f):
            glVertex3fv(v)

        glVertex3fv(self.base_bot_f)
        glEnd()

        # face de trás
        glBegin(GL_POLYGON)
        glVertex3fv(self.base_top_b)

        for v in self.curva_cima_b:
            glVertex3fv(v)

        for v in reversed(self.curva_baixo_b):
            glVertex3fv(v)

        glVertex3fv(self.base_bot_b)
        glEnd()

        # lateral de cima
        glBegin(GL_QUADS)
        for i in range(len(self.curva_cima_f) - 1):
            glVertex3fv(self.curva_cima_f[i])
            glVertex3fv(self.curva_cima_f[i + 1])
            glVertex3fv(self.curva_cima_b[i + 1])
            glVertex3fv(self.curva_cima_b[i])
        glEnd()

        # lateral de baixo
        glBegin(GL_QUADS)
        for i in range(len(self.curva_baixo_f) - 1):
            glVertex3fv(self.curva_baixo_f[i])
            glVertex3fv(self.curva_baixo_f[i + 1])
            glVertex3fv(self.curva_baixo_b[i + 1])
            glVertex3fv(self.curva_baixo_b[i])
        glEnd()

        # lateral da ponta
        glBegin(GL_QUADS)
        glVertex3fv(self.curva_cima_f[-1])
        glVertex3fv(self.curva_baixo_f[-1])
        glVertex3fv(self.curva_baixo_b[-1])
        glVertex3fv(self.curva_cima_b[-1])
        glEnd()

        # lateral do encaixe
        glBegin(GL_QUADS)
        glVertex3fv(self.base_top_f)
        glVertex3fv(self.base_bot_f)
        glVertex3fv(self.base_bot_b)
        glVertex3fv(self.base_top_b)
        glEnd()