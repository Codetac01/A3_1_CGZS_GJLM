from OpenGL.GL import *

class Garra:
    def __init__(self, espessura=1.20):
        self.espessura = espessura
        zf = espessura / 2 #z da frente
        zb = -espessura / 2 #z de trás
#PONTOS X E Y
        base = [
            (1.02, 0.10),
            (1.60, 0.10),
            (2.20, 0.08),
            (2.80, 0.00),
            (3.20, -0.10),
            (3.45, -0.22),
            (3.35, -0.42),
            (3.25, -0.58),
        ]

        interno = [
            (1.20, 0.02),
            (1.70, 0.01),
            (2.30, -0.02),
            (2.80, -0.08),
            (3.10, -0.14),
            (3.05, -0.28),
            (2.95, -0.36),
        ]

        self.frente = []
        self.tras = []
        self.interno_frente = []
        self.interno_tras = []
      #  TRANSFORMA BASE EM 3D
        for x, y in base:
            self.frente.append((x, y, zf))
            self.tras.append((x, y, zb))

        for x, y in interno:
            self.interno_frente.append((x, y, zf))
            self.interno_tras.append((x, y, zb))

    def draw_linha_aberta(self, pontos): #método para desenhar uma sequência de linhas ligando pontos em ordem.
        for i in range(len(pontos) - 1): #Esse for percorre os índices da lista, menos o último.
            glVertex3fv(pontos[i])
            glVertex3fv(pontos[i + 1])

    def draw(self):
        glColor3f(1.0, 0.25, 0.25)
        glBegin(GL_LINES)

        # contorno externo da frente
        self.draw_linha_aberta(self.frente)

        # contorno externo de trás
        self.draw_linha_aberta(self.tras)

        # linhas ligando frente e trás
        # começa do ponto 1 e vai até o penúltimo
        for i in range(1, len(self.frente) - 1):
            glVertex3fv(self.frente[i])
            glVertex3fv(self.tras[i])

        # detalhe interno da frente
        self.draw_linha_aberta(self.interno_frente)

        # detalhe interno de trás
        self.draw_linha_aberta(self.interno_tras)

        # ligações do detalhe interno com a frente
        glVertex3fv(self.frente[1])
        glVertex3fv(self.interno_frente[0])

        glVertex3fv(self.frente[-2])
        glVertex3fv(self.interno_frente[-1])

        # ligações do detalhe interno com trás
        glVertex3fv(self.tras[1])
        glVertex3fv(self.interno_tras[0])

        glVertex3fv(self.tras[-2])
        glVertex3fv(self.interno_tras[-1])

        glEnd()