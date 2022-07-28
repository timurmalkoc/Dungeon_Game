import random
import pygame
import tkinter as tk
from tkinter import messagebox

width = 500
rows = 10
gap = width // rows

# ================================== draw grid 10X10 ===================================
def draw_grid(surface):
    x = 0
    y = 0
    for i in range(rows):
        x+=gap
        y+=gap
        pygame.draw.line(surface, (255,255,255) , (x,0),(x,width))
        pygame.draw.line(surface, (255,255,255) , (0,y),(width,y))

# ============================== draw all stuff ========================================
def draw_all(surface):
    surface.fill((0,0,0))
    draw_grid(surface)
    player.draw_path(surface)
    player.draw_player(surface)
    basket.draw_basket(surface)
    egg_1.draw_egg(surface)
    egg_2.draw_egg(surface)
    egg_3.draw_egg(surface)
    door.draw_door(surface)
    pygame.display.update()

# ================================== Token and Character ===============================
class Token:
    def __init__(self ,pos):
        self.x = pos[0]
        self.y = pos[1]


    def draw(self, surface, color, x, y):
        pygame.draw.rect(surface, color, (x*gap+1,y*gap+1,gap-2,gap-2))

    def draw2(self, surface, color):
        pygame.draw.rect(surface, color, (self.x*gap+1,self.y*gap+1,gap-2,gap-2))

# ====================================== Player =========================================
class Player(Token):
    path = []
    basket = False
    egg_1 = False
    egg_2 = False
    egg_3 = False
    win = False
    def __init__(self, pos, color, health):
        super().__init__(pos)
        self.color = color
        self.health = health
        self.path.append([pos[0],pos[1]])
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

            key = pygame.key.get_pressed()

            if key[pygame.K_LEFT]:
                if self.x>0:
                    self.x-=1
                    self.path.append([self.x, self.y])
            elif key[pygame.K_RIGHT]:
                if self.x<9:
                    self.x+=1
                    self.path.append([self.x, self.y])
            elif key[pygame.K_UP]:
                if self.y>0:
                    self.y-=1
                    self.path.append([self.x, self.y])
            elif key[pygame.K_DOWN]:
                if self.y<9:
                    self.y+=1
                    self.path.append([self.x, self.y])


    # Checking requirements --------------------------------------------
        # cheking basket
            if self.x==basket.x and self.y==basket.y:
                basket.show = False
                self.basket = True
        # checking eggs
            if self.basket and self.x == egg_1.x and self.y==egg_1.y:
                egg_1.show = False
                self.egg_1 = True

            if self.basket and self.x == egg_2.x and self.y==egg_2.y:
                egg_2.show = False
                self.egg_2 = True

            if self.basket and self.x == egg_3.x and self.y==egg_3.y:
                egg_3.show = False
                self.egg_3 = True
        # checking monsters -----------------------------------------------------------------------------------
            if self.x == monster_1.x and self.y == monster_1.y:
                message_box("Lost !!!", "Monster got you!! \n Game over")
                self.win = True
            if self.x == monster_2.x and self.y == monster_2.y:
                message_box("Lost !!!", "Monster got you!! \n Game over")
                self.win = True
            if self.x == monster_3.x and self.y == monster_3.y:
                message_box("Lost !!!", "Monster got you!! \nGame over")
                self.win = True
            if self.x == monster_4.x and self.y == monster_4.y:
                message_box("Lost !!!", "Monster got you!! \n Game over")
                self.win = True
            if self.x == monster_5.x and self.y == monster_5.y:
                message_box("Lost !!!", "Monster got you!! \n Game over")
                self.win = True
            if self.x == monster_6.x and self.y == monster_6.y:
                message_box("Lost !!!", "Monster got you!! \nGame over")
                self.win = True

        # checking all requirements ---------------------------------------------------------------------------
            if self.basket and self.egg_1 and self.egg_2 and self.egg_3 and self.x==door.x and self.y==door.y:
                message_box("Win !!!", "You won the game !!!!")
                self.win = True


    # ================= Print Character ====================
    def draw_player(self, surface):
        Token.draw(self, surface, self.color, self.path[-1][0], self.path[-1][1])


    # =============== Print Character Path =================
    def draw_path(self, surface):
        for i in range(len(self.path)):
            Token.draw(self, surface, (0,255,0), self.path[i][0], self.path[i][1])

class Monster(Token):
    pass

# ==================================== Egg =============================================
class Egg(Token):
    def __init__(self, pos, show=True):
        super().__init__(pos)
        self.show = show

    def draw_egg(self, surface):
        if self.show:
            Token.draw2(self, surface, (255,255,255))
            pygame.draw.ellipse(surface,(239,200,180),(self.x*gap+5,self.y*gap+1, gap-10,gap-2))
# ==================================== Basket ==============================================
class Basket(Token):
    def __init__(self, pos, show=True):
        super().__init__(pos)
        self.show = show
    def draw_basket(self, surface):
        if self.show:
            Token.draw2(self, surface, (255,255,255))
            pygame.draw.rect(surface, (210,105,30), (self.x*gap+10,self.y*gap+20,gap-20,gap-30))
            pygame.draw.rect(surface, (210,105,30), (self.x*gap+22,self.y*gap+10,gap-42,gap-40))

# ==================================== Door ================================================
class Door(Token):
    def draw_door(self, surface):
        Token.draw2(self, surface, (255,255,255))
        pygame.draw.rect(surface, (0,0,0), (self.x*gap+10,self.y*gap+10,gap-20,gap-12))


# ========= generatining characters locations ===============
def generate_rondom_positions(number_of_character):
    c = []
    while len(c)<number_of_character:
        r1 = random.randrange(0,9,1)
        r2 = random.randrange(0,9,1)
        if not [r1,r2] in c:
            c.append([r1,r2])

    print("Cahracter locations :",c)
    return c

def characters_postion():
    # generate random positions for given number of charecters into a dictionary
    c = generate_rondom_positions(12)
    
    d = {   "player":c[0],
            "monster_1":c[1],
            "monster_2":c[2],
            "monster_3":c[3],
            "basket":c[4],
            "egg_1":c[5],
            "egg_2":c[6],
            "egg_3":c[7],
            "door":c[8],
            "monster_4":c[9],
            "monster_5":c[10],
            "monster_6":c[11],
    }
    return d

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)


def main():
    win = pygame.display.set_mode((width,width))
    flag = 1
    global player, position, basket, door, egg_1,egg_2,egg_3,monster_1, monster_2, monster_3, monster_4,monster_5,monster_6
    clock = pygame.time.Clock()

    position  = characters_postion()
    player = Player(position["player"],(255,0,0),100)
    basket = Basket(position["basket"])
    door = Door(position["door"])
    egg_1 = Egg(position["egg_1"])
    egg_2 = Egg(position["egg_2"])
    egg_3 = Egg(position["egg_3"])
    monster_1 = Monster(position["monster_1"])
    monster_2 = Monster(position["monster_2"])
    monster_3 = Monster(position["monster_3"])
    monster_4 = Monster(position["monster_4"])
    monster_5 = Monster(position["monster_5"])
    monster_6 = Monster(position["monster_6"])
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        draw_all(win)
        # get user input
        player.move()
        if player.win == True:
            break
main()