# Jacob Auman
# 2D Linkage Robot Arm simulator
#############################################
import pygame
import math
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


class Linkage: 
    def __init__(self, length, angle, x1, y1,color):
        self.length = length
        self._x1 = x1
        self._y1 = y1
        self._angle = angle
        self.color = color

    @property
    def x2(self):
        self.getEndPoint()
        return self._x2

    @property
    def y2(self):
        self.getEndPoint()
        return self._y2

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, value):
        self._x1 = value

    @property
    def y1(self):
        return self._y1

    @y1.setter
    def y1(self, value):
        self._y1 = value

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value

    def getEndPoint(self):
        # convert deg to rad
        angle_rad = math.radians(self.angle)

        # get the end of the linkage
        self._x2 = self.x1 + self.length * math.cos(angle_rad)
        self._y2 = self.y1 + self.length * math.sin(angle_rad)

    def draw(self):
        self.getEndPoint()
        # draw the linkage in pygame
        pygame.draw.line(screen, self.color, (self.x1, self.y1), (self.x2, self.y2), 10)


### Create Linkage Objects ###
a,b = 400,400
link1 = Linkage(200,45,a,b,"black")
link2 = Linkage(200,180,a,b,"black")

# Create Linkage Objects
t_c_x = 200
t_c_y = 200
l_ab = 100
l_ac = 100
l_bc = 100

link_t_bc = Linkage(l_bc, , t_c_x, t_c_y,"blue")

n = 45-90
link_t_ac = Linkage(l_ac, n, t_c_x, t_c_y,"black")

m = -90-45
t_b_x = link_t_bc.x2
t_b_y = link_t_bc.y2
link_t_ab = Linkage(l_ab, m, t_b_x, t_b_y,"red")

# System of Equations that solves for a triangle given 3 side lenghts
# a = 100
# b = 100
# c = 100
# A = math.acos((b**2 + c**2 - a**2)/(2*b*c))
# B = math.acos((a**2 + c**2 - b**2)/(2*a*c))
# C = math.acos((a**2 + b**2 - c**2)/(2*a*b))



def main():
    a = 400
    b = 400
    dragging = False
    offset_x = 0
    offset_y = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if pygame.Rect(a - 10, b - 10, 20, 20).collidepoint(event.pos):
                        dragging = True
                        offset_x = event.pos[0] - a
                        offset_y = event.pos[1] - b
           
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    dragging = False
           
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    a = event.pos[0] - offset_x
                    b = event.pos[1] - offset_y

        screen.fill("white")
        link1.x1 = a
        link1.y1 = b
        link1.draw()
        link2.x1 = link1.x1
        link2.y1 = link1.y1
        link2.draw()

        # draw the triangle
        link_t_bc.draw()
        link_t_ac.draw()
        link_t_ab.draw()
        
        pygame.draw.circle(screen, "red", (a, b), 10)
        pygame.display.flip()
        clock.tick(60)   
    pygame.quit()


if __name__ == "__main__":
    main()
