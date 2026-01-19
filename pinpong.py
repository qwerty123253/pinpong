from pygame import *
from random import *
import sys

win = display.set_mode((800, 500))

clock = time.Clock()

init()
image_generator = font.Font(None, 50)

class Player():
    def __init__(self, x, y, speed):
        self.hitbox = Rect(x, y, 20, 150)
        self.speed = speed
        self.score = 0
        self.score_img = image_generator.render(str(self.score), False, (255, 255, 255), (0, 0, 0)) # четвёртое это бэкграунд

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
            ball1.random_x = randint(1, 2)
            ball1.random_y = randint(1, 2)


    def AI(self):
                # Добавляем небольшую случайную ошибку
        target_y = ball1.hitbox.centery + randint(-120, 120)
        
        # Двигаемся к цели
        if self.hitbox.centery < target_y:
            self.hitbox.y += self.speed
        elif self.hitbox.centery > target_y:
            self.hitbox.y -= self.speed

        # Ограничиваем движение в пределах экрана
        if self.hitbox.top < 0:
            self.hitbox.top = 0
        if self.hitbox.bottom > 500:
            self.hitbox.bottom = 500

        # Отбиваем мяч
        if self.hitbox.colliderect(ball1.hitbox):
            ball1.speed_x = -ball1.speed
            ball1.random_x = randint(1, 2)
            ball1.random_y = randint(1, 2)
            #self.hitbox.y = ball1.hitbox.y
            #if self.hitbox.colliderect(ball1.hitbox):
                #ball1.speed_x = -ball1.speed

        

        




class Ball():
        def __init__(self, x, y, speed):
            self.hitbox = Rect(x, y, 30, 30)
            self.speed = speed
            self.speed_x = speed
            self.speed_y = speed
            self.random_x = 1
            self.random_y = 1


        def move(self):
            self.hitbox.x += self.speed_x * self.random_x
            self.hitbox.y += self.speed_y * self.random_y
            if self.hitbox.top < 0:
                self.speed_y = self.speed
            if self.hitbox.bottom > 500:
                self.speed_y = -self.speed
            if self.hitbox.left < 0:
                self.speed_x = self.speed
                AI.score += 1
                AI.score_img = image_generator.render(str(AI.score), False, (255, 255, 255), (0, 0, 0))
                self.hitbox.center = (400, 250)
                self.random_x = 1
                self.random_y = 1
                #time.wait(300)
                #player1.hitbox.height -= 10
                player1.speed += 0.2
            if self.hitbox.right > 800:
               self.speed_x = -self.speed
               player1.score += 1
               player1.score_img = image_generator.render(str(player1.score), False, (255, 255, 255), (0, 0, 0))
               #AI.hitbox.height += 10
               self.hitbox.center = (400, 250)
               self.random_x = 1
               self.random_y = 1
               #time.wait(300)
               



        



        

        


player1 = Player(50, 240, 2)
ball1 = Ball(10, 10, 1)
AI = Player(700, 240, 2)

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

    win.blit(player1.score_img, (20, 20))
    win.blit(AI.score_img, (750, 20))

    if player1.score == 10:
            quit()
            sys.exit()

    if AI.score == 10:
            quit()
            sys.exit()

    display.update()
    clock.tick(500)

    


