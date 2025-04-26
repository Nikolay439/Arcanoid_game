import pygame
pygame.init()


move_right = False
move_left = False

back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()

speed_x = 3
speed_y = 4


#переменные, отвечающие за координаты платформы
racket_x = 200
racket_y = 330


#флаг окончания игры
game_over = False
#класс из предыдущего проекта
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color


    def color(self, new_color):
        self.fill_color = new_color


    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)


    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


    def colliderect(self, rect):
        return self.rect.colliderect(rect)


#класс для объектов-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))



class Label(Area):
    def set_text(self,text,fsize = 12 ,text_color= (0,0,0)):# какой текст (шрифт,какой цвет)
        self.image = pygame.font.SysFont('vedrana' ,fsize).render(text,True,text_color)

    # место где будет написоно слово
    def draw(self , shift_x = 0 , shift_y = 0):
        self.fill()
        mw.blit(self.image , (self.rect.x  + shift_x,  self.rect.y + shift_y))



#создание мяча и платформы
ball = Picture('ball_1615463127.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)








start_x= 5
start_y = 5
caunt = 9

monsters = []

for j in range(3):
    y= start_y +(55 * j)
    x= start_x +(27.5 * j)
    for i in range(caunt):
        d= Picture('enemy_1615463121.png', x, y , 50 ,50)
        monsters.append(d)
        x=x+55
        d.draw()

    caunt = caunt -1

while not game_over:


    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event. type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.colliderect(platform.rect):
        speed_y *= -1

    if ball.rect.y <  0:
        speed_y *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1






    if move_left:
        platform.rect.x -=5

    if move_right:
        platform.rect.x +=5




    mw.fill(back)

    if ball.rect.y > (racket_y +20):
        time_text = Label(150,150,50,50,back)
        time_text.set_text('YOU LOSE' , 60 ,(225, 0, 0))
        time_text.draw(10,10)
        game_over = True

    if len (monsters) == 0:
        time_text = Label(150,150,50,50,back)
        time_text.set_text('YOU WIN' , 60 ,(0, 200, 0))
        time_text.draw(10,10)
        game_over = True


    for d in  monsters:
        d.draw()

        if d.rect.colliderect(ball.rect):
            monsters.remove(d)
            d.fill()
            speed_y *=-1


    ball.draw()
    platform.draw()
    pygame.display.update()
    clock.tick(40)



