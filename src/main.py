import pygame
import Input
import Settings
import Globals
import DataManager

def update(delta_time):
    Globals.current_scene.update(delta_time)

def render(gameDisplay):
    Globals.current_scene.render(gameDisplay)
    pygame.display.update()

pygame.init()
#Init window settings
Globals.gameDisplay = pygame.display.set_mode((Settings.display_width, Settings.display_height))
pygame.display.set_caption(Settings.title)
pygame.display.set_icon(pygame.image.load(Settings.icon_path))
#Init delta_time
delta_time=0
last_time=pygame.time.get_ticks()


import TitleScene
Globals.current_scene = TitleScene.TitleScene()

while Globals.running:
    #Handle events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Globals.running = False
        else:
            Input.events.append(event)
    #Update inputs
    Input.keyboard.update()
    Input.mouse.update()
    #Update
    delta_time=(pygame.time.get_ticks()-last_time) / 1000
    last_time=pygame.time.get_ticks() 
   
    update(delta_time)
    render(Globals.gameDisplay)

    Input.keyboard.late_update()
    Input.events = []
    if Globals.next_scene != None:
        Globals.current_scene = Globals.next_scene
        Globals.next_scene = None
pygame.quit()