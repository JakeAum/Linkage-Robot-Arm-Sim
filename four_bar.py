# This is my attempt at creating a 4 bar linkage simulator

import pygame
import math

class FourBarLinkage:
    def __init__(self, link1, link2, link3, link4):
        self.link1 = link1 # Ground
        self.link2 = link2 # Input
        self.link3 = link3 # Coupler
        self.link4 = link4 # Output

        self.validate_geometry()
       
    def validate_geometry(self):

        
class Link:
    def __init__(self, length, angle, x1, y1):
        self.length = length
        self.angle = angle  # in radians
        self.x1 = x1
        self.y1 = y1
        self.x2, self.y2 = self.calculate_end_point()

    def calculate_end_point(self):
        x2 = self.x1 + self.length * math.cos(self.angle)
        y2 = self.y1 + self.length * math.sin(self.angle)
        return x2, y2

    def update(self, angle):
        self.angle = angle
        self.x2, self.y2 = self.calculate_end_point()
        
    def Draw(self, screen):
        pygame.draw.line(screen, "black", (self.x1, self.y1), (self.x2, self.y2), 10)


def pygameMain(link_list):
    ### Pygame Init ### 
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Four Bar Linkage")
    clock = pygame.time.Clock()
    running = True

    ### Pygame Loop ###
    while running:
        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       
        ### Draw ###
                
        screen.fill("white")
        drawObjects(link_list,screen)
        pygame.display.flip()
        clock.tick(60)

def initLinks():

    test_link = Link(50, 50, 100, 10)
    link_list = [test_link]

    link1 = Link(0, 0, 10, 10)
    link2 = Link(0, 0, 10, 10)
    link3 = Link(0, 0, 10, 10)
    link4 = Link(0, 0, 10, 10)

    #link_list = [test_link , link1 , link2, link3 , link4]
 
    return link_list

def drawObjects(link_list, screen):
    for linkName in link_list:
        linkName.Draw(screen)

def main():
    link_list = initLinks()  
    
    # Test
    for linkName in link_list:
        linkName.Test()


    pygameMain(link_list)

if __name__ == "__main__":
    main()