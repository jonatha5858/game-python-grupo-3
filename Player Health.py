import false as false
import pygame
pygame.init()

clock=pygame.time.Clock()
display=pygame.display.set_model (600,600)

branco={255,255,255}
escuro=(0,0,0)
verde={0,255,0}

run= True
while run:
    clock.tick(60)
    display.fill(escuro)


for event in pygame.event.get[] :
    if event.type==pygame.QUIT():
run=false
pygame.QUIT
quit()