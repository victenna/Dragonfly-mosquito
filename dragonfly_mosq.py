import pygame,random
from math import *
pygame.init()
screen = pygame.display.set_mode((1200, 900))
bg = pygame.image.load('bGround.png')
clock = pygame.time.Clock()
class Bug(pygame.sprite.Sprite):
    def __init__(self,image,scale):
        super().__init__()
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(scale,scale))
        self.start_image=self.image
        self.rect=self.image.get_rect()
        self.settings()
    def settings(self):
        x=random.randint(100,700)
        y=random.randint(100,700)
        dx=random.randint(-5,5)
        dy=random.randint(-5,5)
        self.x,self.y=x,y
        self.rect.center=(self.x,self.y)
        self.dx,self.dy=dx,dy
    def hide(self):
        self.image.fill((0,0,0,0))
    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        if self.x>1150 or self.x<50: self.dx=-self.dx
        if self.y>850 or self.y<50: self.dy=-self.dy
        self.rect.center=(self.x,self.y)
        degree=atan2(-self.dy,self.dx)*180/3.14159
        self.image=pygame.transform.rotate(self.start_image,degree)
Q,Q1=60,3
bug,killer=pygame.sprite.Group(),pygame.sprite.Group()
for i in range (Q):
    bug.add(Bug('mosquito1.png',20))
for i in range (Q1):
    killer.add(Bug('dragonfly1.png',50))
font=pygame.font.Font(None,56)
start_time=pygame.time.get_ticks()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), exit()
    screen.fill('light green')
    bug.update(),bug.draw(screen)    
    killer.update(),killer.draw(screen)
    collision=pygame.sprite.groupcollide(killer,bug,False,True)
    clock.tick(100)
    Time=(pygame.time.get_ticks()-start_time)//1000
    text=font.render(str(Time),True,(255,255,255))
    screen.blit(text,(800,50))
    pygame.display.update()