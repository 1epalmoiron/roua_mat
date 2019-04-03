import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False

pawn = pygame.image.load('pawn.png')
queen = pygame.image.load('queen.png')
bishop = pygame.image.load('bishop.png')
knight = pygame.image.load('knight.png')
rook = pygame.image.load('rook.png')
king = pygame.image.load('king.png')

wpawn = pygame.image.load('wpawn.png')
wqueen = pygame.image.load('wqueen.png')
wbishop = pygame.image.load('wbishop.png')
wknight = pygame.image.load('wknight.png')
wrook = pygame.image.load('wrook.png')
wking = pygame.image.load('wking.png')


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True



        screen.fill((255, 255, 255))
        x = 0
        y = 0
        color = (0,0,0)
        i = 0
        for y in range(0,640,80):
                for x in range(0,640,80):

                        if i % 2==0:
                                color = (0,255,255)

                        else:
                                color = (0,0,0)

                        pygame.draw.rect(screen, color, pygame.Rect(x, y, 80, 80))
                        i+=1
                i+=1


        a = 10
        b = 100
        screen.blit(pawn,(a,b))

        a += 40 +30 + 10
        screen.blit(pawn,(a,b))

        a += 40 +30 + 10
        screen.blit(pawn,(a,b))

        a += 40 +30 + 10
        screen.blit(pawn,(a,b))

        a += 40 +30 + 10
        screen.blit(pawn,(a,b))

        a += 40 +30 + 10
        screen.blit(pawn,(a,b))

        a += 40 +30 + 10
        screen.blit(pawn,(a,b))

        a += 40 +30 + 10
        screen.blit(pawn,(a,b))

        
        x = 10
        y = 495
        screen.blit(wpawn,(x,y))

        x += 40 +30 + 10
        screen.blit(wpawn,(x,y))

        x += 40 +30 + 10
        screen.blit(wpawn,(x,y))

        x += 40 +30 + 10
        screen.blit(wpawn,(x,y))

        x += 40 +30 + 10
        screen.blit(wpawn,(x,y))

        x += 40 +30 + 10
        screen.blit(wpawn,(x,y))

        x += 40 +30 + 10
        screen.blit(wpawn,(x,y))

        x += 40 +30 + 10
        screen.blit(wpawn,(x,y))

       	screen.blit(rook,(10,15)) #rook Black
       	screen.blit(wrook,(10,570)) #rook White

       	screen.blit(knight,(90,15)) #knight Black
       	screen.blit(wknight,(90,570)) #knight White
 
       	screen.blit(bishop,(170,15)) #bishop Black
       	screen.blit(wbishop,(170,570)) #bishop White

       	screen.blit(king,(250,15)) #king Black
       	screen.blit(wking,(250,570)) #king White

       	screen.blit(queen,(330,15)) #queen Black
       	screen.blit(wqueen,(330,570)) #queen White

       	screen.blit(bishop,(410,15)) #bishop Black
       	screen.blit(wbishop,(410,570)) #bishop White

      	screen.blit(knight,(490,15)) #knight Black
       	screen.blit(wknight,(490,570)) #knight White

       	screen.blit(rook,(570,15)) #rook Black
       	screen.blit(wrook,(570,570)) #rook White
 
        pygame.display.flip()

