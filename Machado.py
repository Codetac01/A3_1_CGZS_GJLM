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
        self.base_top = (self.raio, meio, 0)
        self.base_bot = (self.raio, -meio, 0)

        # curvas
        self.curva_cima_f = []
        self.curva_baixo_f = []
        self.curva_cima_b = []
        self.curva_baixo_b = []

        for i in range(pontos):
            t = i / (pontos - 1)

            x = self.raio + t * largura
            y = meio * sqrt(1 - t ** 2)

            self.curva_cima_f.append((x, y, z_front))
            self.curva_baixo_f.append((x, -y, z_front))

            self.curva_cima_b.append((x, y, z_back))
            self.curva_baixo_b.append((x, -y, z_back))

    def draw(self):

        glColor3f(0.5, 0.5, 0.5)

        glBegin(GL_POLYGON)

        # lâmina de cima
        for v in self.curva_cima:
            glVertex3fv(v)

        # lâmina de baixo
        for v in reversed(self.curva_baixo):
            glVertex3fv(v)

        # conexão
        glVertex3fv(self.base_top)
        glVertex3fv(self.base_bot)

        glEnd()

        glBegin(GL_QUADS)

        for i in range(len(self.curva_cima_f) - 1):
            glVertex3fv(self.curva_cima_f[i])
            glVertex3fv(self.curva_cima_f[i + 1])
            glVertex3fv(self.curva_cima_b[i + 1])
            glVertex3fv(self.curva_cima_b[i])

        for i in range(len(self.curva_baixo_f) - 1):
            glVertex3fv(self.curva_baixo_f[i])
            glVertex3fv(self.curva_baixo_f[i + 1])
            glVertex3fv(self.curva_baixo_b[i + 1])
            glVertex3fv(self.curva_baixo_b[i])

        glEnd()