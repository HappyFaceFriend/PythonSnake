import pygame
import Input

game_settings = {
    "display_width": 400,
    "display_height": 400,
    "title": "Sname Game",
    "icon_path": "images/icon.png"
}

pygame.init()
#Init window settings
gameDisplay=pygame.display.set_mode((game_settings["display_height"], game_settings["display_height"]))
pygame.display.set_caption(game_settings["title"])
pygame.display.set_icon(pygame.image.load(game_settings["icon_path"]))
#Init delta_time
delta_time=0
last_tick=pygame.time.get_ticks()

tempimg = pygame.image.load("images/icon.png")

running = True
while running:
    #Handle events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    #Update inputs
    Input.keyboard.update()
    Input.mouse.update()

    #Calculate delta_time
    delta_time=(pygame.time.get_ticks()-last_tick)/1000
    last_tick=pygame.time.get_ticks()
    
    #Render test image
    pygame.draw.rect(gameDisplay,(0,0,0), [0,0,game_settings["display_height"], game_settings["display_height"]])
    gameDisplay.blit(tempimg,Input.get_mouse_pos())

    pygame.display.update()

    Input.keyboard.late_update()

pygame.quit()