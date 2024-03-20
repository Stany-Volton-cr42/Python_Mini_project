import pygame
import time
import sys
from pygame.locals import *
import random

SIZE = 40

class Apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("G:\\Python_project\\Python_Littel_project\\DSA_project\\resources\\apple.jpg").convert()
        self.x = 120
        self.y = 120

    def apple_draw(self):
        self.parent_screen.blit(self.apple,(self.x,self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,14) * SIZE
        self.y = random.randint(1,14) * SIZE
        
class Snake:
    def __init__(self,parent_screen,length):
        self.parent_screen = parent_screen    
        self.image = pygame.image.load("G:\\Python_project\\Python_Littel_project\\DSA_project\\resources\\block.jpg").convert()
        self.direction = "down"

        self.length = length
        self.x = [40] *length
        self.y = [40] *length


    def draw(self):
        self.parent_screen.fill((146, 201, 131))

        for i in range(self.length):
            self.parent_screen.blit(self.image,(self.x[i],self.y[i]))
        pygame.display.flip()


    def Increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"


    def walk(self):
        for i in range(self.length -1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]


        if self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "down":
            self.y[0] += SIZE
        elif self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "right":
            self.x[0] += SIZE

        self.draw()


class game:
    def __init__(self):    
        pygame.init()
        width, height = 760, 600
        self.screen = pygame.display.set_mode((width, height))
        self.Snake = Snake(self.screen,2)
        self.apple = Apple(self.screen)
        self.Snake.draw()
        self.apple.apple_draw()

    def eat_apple(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.Snake.length}",True,(200,200,200))
        self.screen.blit(score,(550,10))

    def play(self):
        self.Snake.walk()
        self.apple.apple_draw()
        self.display_score()
        pygame.display.flip()

        if self.eat_apple(self.Snake.x[0], self.Snake.y[0], self.apple.x, self.apple.y):
            self.Snake.Increase_length()
            self.apple.move()

    def run(self):    
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.Snake.move_left()

                    if event.key == K_RIGHT:
                        self.Snake.move_right()

                    if event.key == K_UP:
                        self.Snake.move_up()

                    if event.key == K_DOWN:
                        self.Snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.3)



if __name__ == "__main__":
    game = game()
    game.run()


    fps = 90
    fpsClock = pygame.time.Clock()
    pygame.quit()
    sys.exit()

fpsClock.tick(fps)