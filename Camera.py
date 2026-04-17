import pygame
from OpenGL.GLU import *
from math import *

class Camera:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 3)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, -1)

        self.yaw = -90
        self.pitch = 0

        self.last_mouse = pygame.math.Vector2(pygame.mouse.get_pos())

    def rotate(self, yaw, pitch):
        self.yaw += yaw * 0.1
        self.pitch += pitch * 0.1

        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward.y = sin(radians(self.pitch))
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))

        self.forward = self.forward.normalize()

        self.right = self.forward.cross(pygame.Vector3(0, 1, 0)).normalize()
        self.up = self.right.cross(self.forward).normalize()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = pygame.math.Vector2(mouse_pos) - self.last_mouse
        self.last_mouse = mouse_pos

        self.rotate(mouse_change.x, -mouse_change.y)

        keys = pygame.key.get_pressed()
        speed = 0.1

        if keys[pygame.K_DOWN]:
            self.eye -= self.forward * speed
        if keys[pygame.K_UP]:
            self.eye += self.forward * speed
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