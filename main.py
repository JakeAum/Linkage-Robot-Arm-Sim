# Jacob Auman
# 2D Linkage Robot Arm simulator
#############################################
import pygame
import math
import pygame

class Joint:
    def __init__(self, x, y, color, is_fixed=False):
        self.x = x
        self.y = y
        self.color = color
        self.is_fixed = is_fixed
        self.is_dragging = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Link: 
    # This Class takes in two Joint Class Instances, and a specified length that the two points must always maintain
    def __init__(self, jointA, jointB, length):
        self.jointA = jointA
        self.jointB = jointB
        self.length = length

    def draw(self, screen):
        pygame.draw.line(screen, "black", (self.jointA.x, self.jointA.y), (self.jointB.x, self.jointB.y), 5)

    def updateJointPosition(self):
        # This function will check if the points are within the specified length, and if not, it will then check to see which point are fixed or floating then calculate the new position of the floating point.

        # Calculate the distance between the two points
        distance = math.sqrt((self.jointB.x - self.jointA.x)**2 + (self.jointB.y - self.jointA.y)**2)
        if self.length != distance:
            if self.jointA.is_fixed == False and self.jointB.is_fixed == True:
                # Calculate the new position of jointA
                self.jointA.x = self.jointB.x - (self.jointB.x - self.jointA.x) / distance * self.length
                self.jointA.y = self.jointB.y - (self.jointB.y - self.jointA.y) / distance * self.length
            elif self.jointA.is_fixed == True and self.jointB.is_fixed == False:
                # Calculate the new position of jointB
                self.jointB.x = self.jointA.x - (self.jointA.x - self.jointB.x) / distance * self.length
                self.jointB.y = self.jointA.y - (self.jointA.y - self.jointB.y) / distance * self.length
            elif self.jointA.is_fixed == False and self.jointB.is_fixed == False:
                # Calculate the new position of both joints
                angle = math.atan2(self.jointB.y - self.jointA.y, self.jointB.x - self.jointA.x)
                new_x = self.jointA.x + math.cos(angle) * self.length
                new_y = self.jointA.y + math.sin(angle) * self.length
                self.jointB.update_position(new_x, new_y)
                self.jointA.update_position(new_x - math.cos(angle) * self.length, new_y - math.sin(angle) * self.length)
            else:
                raise Exception("Both joints cannot be fixed")



def main():
    ### pygame init ###
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    
    #Center-Ish Origin Point
    a = 750
    b = 650

    joint1 = Joint(a, b, "red", is_fixed=True)
    joint2 = Joint(a, b-1, "blue", is_fixed=False)
    joint3 = Joint(a-1, b-1, "green", is_fixed=False)
   
    joint_list = [joint1, joint2, joint3]

    link12 = Link(joint1, joint2, 400)
    link12.updateJointPosition()
    link13 = Link(joint1, joint3, 200)
    link13.updateJointPosition()
    link23 = Link(joint2, joint3, 300)
    link23.updateJointPosition()

    link_list = [link12, link13, link23]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                
                    for joint in joint_list:
                        if (joint.x - 10 <= event.pos[0] <= joint.x + 10 and joint.y - 10 <= event.pos[1] <= joint.y + 10) and not joint.is_fixed:
                            joint.is_dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    for joint in joint_list:
                        joint.is_dragging = False

                    for link in link_list:
                        link.updateJointPosition()

            elif event.type == pygame.MOUSEMOTION:
                if joint1.is_dragging or joint2.is_dragging or joint3.is_dragging:
                    for joint in joint_list:
                        if joint.is_dragging:
                            joint.update_position(event.pos[0], event.pos[1])

                    for link in link_list:
                        link.updateJointPosition()

        screen.fill("white")
        ((1280, 720))

        pygame.draw.rect(screen, "black", (650, 600, 200 , 200), 5)
        
        for joint in joint_list:
            joint.draw(screen)
        for link in link_list:
            link.draw(screen)
    
        pygame.display.flip()
        clock.tick(60)   
    pygame.quit()


if __name__ == "__main__":
    main()
