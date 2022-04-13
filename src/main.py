import pygame
import Input
import Settings
import Globals

def update():
    Globals.current_scene.update()

def render(gameDisplay):
    Globals.current_scene.render(gameDisplay)
    pygame.display.update()

pygame.init()
#Init window settings
Globals.gameDisplay = pygame.display.set_mode((Settings.display_width, Settings.display_height))
pygame.display.set_caption(Settings.title)
pygame.display.set_icon(pygame.image.load(Settings.icon_path))
#Init delta_time
SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,1)
clock =pygame.time.Clock()

Globals.current_scene = Settings.initial_scene
running = True
while running:
    #Handle events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    #Update inputs
    Input.keyboard.update()
    Input.mouse.update()

  
    #Update
    update()
    render(Globals.gameDisplay)

    Input.keyboard.late_update()
    clock.tick(10)

pygame.quit()