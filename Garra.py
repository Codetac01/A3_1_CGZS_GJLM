from OpenGL.GL import *

class Garra:
    def __init__(self, espessura=1.2):
        zf = espessura / 2
        zb = -espessura / 2

        # triângulo principal (frente)
        self.f0 = (1.20,  0.35, zf)
        self.f1 = (1.20, -0.35, zf)
        self.f2 = (4.60, -0.10, zf)

        # triângulo principal (trás)
        self.b0 = (1.20,  0.35, zb)
        self.b1 = (1.20, -0.35, zb)
        self.b2 = (4.60, -0.10, zb)

        # 🔻 NOVO TRIÂNGULO (ponta caindo para baixo)
        self.f3 = (4.40, -0.25, zf)
        self.f4 = (4.80, -0.45, zf)

        self.b3 = (4.40, -0.25, zb)
        self.b4 = (4.80, -0.45, zb)

    def draw(self):
        glColor3f(0.75, 0.75, 0.75)

        # ======================
        # TRIÂNGULO PRINCIPAL
        # ======================
        glBegin(GL_TRIANGLES)
        glVertex3fv(self.f0)
        glVertex3fv(self.f1)
        glVertex3fv(self.f2)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex3fv(self.b0)
        glVertex3fv(self.b1)
        glVertex3fv(self.b2)
        glEnd()

        # ======================
        # TRIÂNGULO DA PONTA (novo)
        # ======================
        glBegin(GL_TRIANGLES)
        glVertex3fv(self.f2)
        glVertex3fv(self.f3)
        glVertex3fv(self.f4)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex3fv(self.b2)
        glVertex3fv(self.b3)
        glVertex3fv(self.b4)
        glEnd()

        # ======================
        # LATERAIS
        # ======================
        glBegin(GL_QUADS)

        # corpo principal
        glVertex3fv(self.f0); glVertex3fv(self.f1); glVertex3fv(self.b1); glVertex3fv(self.b0)
        glVertex3fv(self.f0); glVertex3fv(self.f2); glVertex3fv(self.b2); glVertex3fv(self.b0)
        glVertex3fv(self.f1); glVertex3fv(self.f2); glVertex3fv(self.b2); glVertex3fv(self.b1)

        # ponta nova
        glVertex3fv(self.f2); glVertex3fv(self.f3); glVertex3fv(self.b3); glVertex3fv(self.b2)
        glVertex3fv(self.f2); glVertex3fv(self.f4); glVertex3fv(self.b4); glVertex3fv(self.b2)
        glVertex3fv(self.f3); glVertex3fv(self.f4); glVertex3fv(self.b4); glVertex3fv(self.b3)

        glEnd()

        # ======================
        # CONTORNO
        # ======================
        glColor3f(0.95, 0.95, 0.95)
        glBegin(GL_LINES)

        # principal frente
        glVertex3fv(self.f0); glVertex3fv(self.f1)
        glVertex3fv(self.f1); glVertex3fv(self.f2)
        glVertex3fv(self.f2); glVertex3fv(self.f0)

        # principal trás
        glVertex3fv(self.b0); glVertex3fv(self.b1)
        glVertex3fv(self.b1); glVertex3fv(self.b2)
        glVertex3fv(self.b2); glVertex3fv(self.b0)

        glEnd()