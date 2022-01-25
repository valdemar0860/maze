import pygame as pg
pg.init()

class OurSprites(pg.sprite.Sprite): 
    def __init__(self, x, y, image, speed): 
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(OurSprites):
    def move(self):
        key = pg.key.get_pressed()
        
        if key[pg.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key[pg.K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if key[pg.K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if key[pg.K_DOWN] and self.rect.x < 620:
            self.rect.y += self.speed
            
class Enemy(OurSprites):
    def move(self):
        
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
            
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = "left"
            


window = pg.display.set_mode((700, 500))
back = pg.transform.scale(pg.image.load("background.jpg"), (700, 500))

clock = pg.time.Clock()
pg.mixer.music.load("jungles.ogg")
pg.mixer.music.play()

cat = Player(200, 200, "hero.png", 4)
dog = Enemy(614, 400, "cyborg.png", 2)

dog.direction = "left"

game = True
FPS = 60

while game:
    window.blit(back, (0, 0))
    cat.reset()
    dog.reset()
    cat.move()
    dog.move()
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
            
    pg.display.update()
    clock.tick(60)
 
