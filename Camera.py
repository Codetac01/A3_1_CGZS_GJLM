import pygame
from OpenGL.GLU import *
from math import *

class Camera:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 3)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.forward = pygame.math.Vector3(0, 0, -1)

        self.yaw = -90
        self.pitch = 0

        # trava o mouse (IMPORTANTE)
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

    def rotate(self, dx, dy):
        sensitivity = 0.1

        self.yaw += dx * sensitivity
        self.pitch += dy * sensitivity


        self.pitch = max(-89, min(89, self.pitch))


        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward.y = sin(radians(self.pitch))
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))

        self.forward = self.forward.normalize()


        self.right = self.forward.cross(pygame.math.Vector3(0, 1, 0)).normalize()
        self.up = self.right.cross(self.forward).normalize()

    def update(self):

        dx, dy = pygame.mouse.get_rel()

        self.rotate(dx, -dy)

        keys = pygame.key.get_pressed()
        speed = 0.1

        if keys[pygame.K_UP]:
            self.eye += self.forward * speed
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward * speed
        if keys[pygame.K_RIGHT]:
            self.eye += self.right * speed
        if keys[pygame.K_LEFT]:
            self.eye -= self.right * speed

        look = self.eye + self.forward

        gluLookAt(
            self.eye.x, self.eye.y, self.eye.z,
            look.x, look.y, look.z,
            self.up.x, self.up.y, self.up.z
        )