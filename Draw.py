import pygame
pygame.init()
class Button:
    def __init__(self,text,fontsize,font,width,height,xcor,ycor,colorbg,fgcolr,wachua=None):
        self.fontsize = fontsize
        self.font = pygame.font.SysFont(font,self.fontsize)
        self.width = width
        self.height = height
        self.xcor = xcor
        self.ycor = ycor
        self.bg = colorbg
        self.fg = fgcolr
        self.words = text
        self.pressedbutton = False
        self.wachua = wachua

    def draw(self):
        self.text = self.font.render(self.words,True,self.fg,self.bg)
        self.textbox = self.text.get_rect(topleft=(self.xcor,self.ycor))
        screen.blit(self.text,(self.xcor,self.ycor))

    def go1(self,width,height,color):
        global rect
        print('Got here')
        rect = pygame.Rect(width,height,width,height)
        rect.center = pygame.mouse.get_pos()
    
        if pygame.mouse.get_pressed()[0]:
            
            pygame.draw.rect(screen,color,rect)

            print('Got here too')

    def go2(self,radius,color):
        global rect
        print('Got here')
    
        if pygame.mouse.get_pressed()[0]:
            
            pygame.draw.circle(screen,color,pygame.mouse.get_pos(),radius,100)

            print('Got here too')
        

    def pressed(self):
        global sizeinput,enterCOlor
        global updating,go,go1,radius,enterCOlor1
        if self.textbox.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.pressedbutton is False:
            updating = False
            self.pressedbutton = True
            
            if self.wachua == 'SQUARE':
                go = True
                go1 = False
                sizeinput = (input('Enter the width and height separating with a comma and no spaces: '))
                enterCOlor = input('Enter color: ')
                self.go1(int(sizeinput.split(',')[0]),int(sizeinput.split(',')[1]),enterCOlor)
            if self.wachua == 'CIRCLE':
                go1 = True
                go = False
                radius = int(input('Radius: ')) 
                enterCOlor1 = input('Enter color: ')
                self.go2(radius,enterCOlor1)
            if self.wachua == 'CLEAR':
                screen.fill('black')


        if pygame.mouse.get_pressed()[0] is False and pygame.mouse.get_pressed()[1] is False and pygame.mouse.get_pressed()[2] is False:
            self.pressedbutton = False

def Square():
    pass

updating = True

screen = pygame.display.set_mode((900,900))
button1 = Button('Square',20,'Arial',40,20,0,0,'yellow','red','SQUARE')
button2 = Button('Circle',20,'Arial',40,20,70,0,'yellow','red','CIRCLE')
button3 = Button('Clear',20,'Arial',40,20,140,0,'yellow','red','CLEAR')

go = False
go1 = False

def updategame():
    if updating == True:
        screen.fill('black')

while True:
    global sizeinput,enterCOlor,enterCOlor1,radius
    global rect
    updategame()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

    button1.draw()
    button1.pressed()
    button2.draw()
    button2.pressed()
    button3.draw()
    button3.pressed()
    


    if go == True:
        button1.go1(int(sizeinput.split(',')[0]),int(sizeinput.split(',')[1]),enterCOlor)
    if go1 == True:
        button2.go2(radius,enterCOlor1)

    pygame.display.update()



# rect = pygame.Rect(self.width,self.height,self.xcor, self.ycor)
# rect.center = pygame.mouse.get_pos()