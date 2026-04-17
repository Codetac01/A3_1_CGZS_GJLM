from OpenGL.GL import *
import pygame

class cabo:
    def __init__(self, largura=1, altura=1, profundidade=1):

        x = largura / 2
        y = altura / 2
        z = profundidade / 2

        self.vertices = [
            ( x, -y,  z),
            (-x, -y,  z),
            ( x,  y,  z),
            (-x,  y,  z),
            ( x,  y, -z),
            (-x,  y, -z),
            ( x, -y, -z),
            (-x, -y, -z)
        ]

        self.triangles = [
            0, 2, 3, 0, 3, 1,
            6, 7, 5, 6, 5, 4,
            1, 3, 5, 1, 5, 7,
            2, 4, 5, 2, 5, 3,
            0, 6, 2, 2, 6, 0,
            7, 1, 6, 6, 1, 7,
        ]

        self.draw_type = GL_LINE_LOOP

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()