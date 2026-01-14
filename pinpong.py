from pygame import *
win = display.set_mode((800, 500))

clock = time.Clock()
class Player():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 20, 150)
        self.speed = speed

    def move(self):
        key_list = key.get_pressed()
        if key_list[K_w]:
            self.hitbox.y -= self.speed
        if key_list[K_s]:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 500:     
            self.hitbox.bottom = 500
        if self.hitbox.top < 0:     
            self.hitbox.top = 0
        if self.hitbox.colliderect(ball1.hitbox):
            ball1.speed_x = ball1.speed

    def AI(self):
        self.hitbox.y = ball1.hitbox.y
        if self.hitbox.colliderect(ball1.hitbox):
            ball1.speed_x = -ball1.speed




class Ball():
        def __init__(self, x, y, speed):
            self.hitbox = Rect(x, y, 25, 25)
            self.speed = speed
            self.speed_x = speed
            self.speed_y = speed


        def move(self):
            self.hitbox.x += self.speed_x
            self.hitbox.y += self.speed_y
            if self.hitbox.top < 0:
                self.speed_y = self.speed
            if self.hitbox.bottom > 500:
                self.speed_y = -self.speed
            #if self.hitbox.left < 0:
                #self.speed_x = self.speed
            #if self.hitbox.right > 800:
               #self.speed_x = -self.speed

        


player1 = Player(50, 240, 1)
ball1 = Ball(10, 10, 2)
AI = Player(700, 240, 1)

while True:
    win.fill((0, 0, 0))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    player1.move()
    draw.rect(win, (255, 0, 0), player1.hitbox)
    draw.rect(win, (0, 0, 255), AI.hitbox)
    AI.AI()
    ball1.move()
    draw.rect(win, (0, 255, 0), ball1.hitbox)
    display.update()
    clock.tick(500)

    


