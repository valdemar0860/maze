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

window = pg.display.set_mode((700, 500))
back = pg.transform.scale(pg.image.load("99px_ru_wallpaper_34496_fon_cherni_i_belij_black_or_white.jpg"), (700, 500))

clock = pg.time.Clock()
pg.mixer.music.load("No Place For Straw Cowboys.ogg")
pg.mixer.music.play()

cat = OurSprites(200, 200, "IMG_20210325_204910_851.jpg", 10)


game = True
FPS = 60

while game:
    window.blit(back, (0, 0))
    cat.reset()
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
            
    pg.display.update()
    clock.tick(60)
