import pygame, random
import tkinter as tk
from tkinter import messagebox

side_length = 700
row = 20

class Cube(object):
    # row = 10
    def __init__(self, start, xdir=1, ydir=0, color = 'red'):
        self.pos = start
        self.xdir = xdir
        self.ydir = ydir
        self.color = color

    def move(self, xdir, ydir):
        self.xdir = xdir
        self.ydir = ydir
        self.pos = (self.pos[0] + self.xdir, self.pos[1] + self.ydir)

    def draw(self, surface, eyes = False):
        dis = side_length // row
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
        if eyes:
            center = dis//2
            radius = 3
            circle_middle = (i*dis+center-radius, j*dis+8)
            circle_middle2 = (i*dis+dis-radius*2, j*dis+8)
            pygame.draw.circle(surface, 'white', circle_middle, radius)
            pygame.draw.circle(surface, 'white', circle_middle2, radius)

class Snake(object):
    body = []
    turns = {}
    
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.ydir = 0
        self.xdir = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            can_back_trun = True

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_RIGHT]:
                    if len(self.body) < 3 or (len(self.body) > 2 and self.xdir != -1):
                        self.xdir = 1
                        self.ydir = 0
                        self.turns[self.head.pos[:]] = [self.xdir, self.ydir]
                elif keys[pygame.K_LEFT]:
                    if len(self.body) < 3 or (len(self.body) > 2 and self.xdir != 1):
                        self.xdir = -1
                        self.ydir = 0
                        self.turns[self.head.pos[:]] = [self.xdir, self.ydir]
                elif keys[pygame.K_UP]:
                    if len(self.body) < 3 or (len(self.body) > 2 and self.ydir != 1):
                        self.xdir = 0
                        self.ydir = -1
                        self.turns[self.head.pos[:]] = [self.xdir, self.ydir]
                elif keys[pygame.K_DOWN]:
                    if len(self.body) < 3 or (len(self.body) > 2 and self.ydir != -1):
                        self.xdir = 0
                        self.ydir = 1
                        self.turns[self.head.pos[:]] = [self.xdir, self.ydir]
            
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
                
            else:
                if c.xdir == -1 and c.pos[0] <= 0: c.pos = (row - 1, c.pos[1])
                elif c.xdir == 1 and c.pos[0] >= row - 1: c.pos = (0, c.pos[1])
                elif c.ydir == 1 and c.pos[1] >= row - 1: c.pos = (c.pos[0], 0)
                elif c.ydir == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], row - 1)
                else: c.move(c.xdir, c.ydir)
    
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.xdir, tail.ydir

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].xdir = dx
        self.body[-1].ydir = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else: 
                c.draw(surface)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.ydir = 0
        self.xdir = 1

def drawGrid(surface):
    size_btwn = side_length // row

    x = 0
    y = 0
    for l in range(row):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, 'white', (x, 0), (x, side_length))
        pygame.draw.line(surface, 'white', (0, y), (side_length, y))

def randomSnack(item):
    positions = item.body

    while True:
        x = random.randrange(row)
        y = random.randrange(row)

        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break

    return (x,y)

def messageBox(subject, content):
    root = tk.Tk()
    root.attributes("-topmost",True)
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

snake = Snake('red', (10,10))
snack = Cube(randomSnack(snake), color='yellow')

def refreshGame(surface):
    surface.fill('black')
    drawGrid(surface)
    snake.draw(surface)
    snack.draw(surface)
    pygame.display.update()

def main():
    global snack
    game = pygame.display.set_mode((side_length,side_length))
    
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(randomSnack(snake), color='yellow')
        
        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z:z.pos, snake.body[x+1:])):
                print()
                messageBox("Game Over".upper(), f"Your score: {len(snake.body)}")
                snake.reset((10,10))
                break

        refreshGame(game)


main()