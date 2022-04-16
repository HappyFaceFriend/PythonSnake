

border_size = 20
topbar_height = 100
board_size = (40,40)
cell_size = (20,20)
display_width = border_size * 2 + board_size[0] * cell_size[0]
display_height = border_size * 2 + topbar_height + board_size[1] * cell_size[1]

title = "Snake Game"
icon_path = "images/icon.png"
font_style = "fonts/arial.ttf"

import TitleScene 
initial_scene = TitleScene.TitleScene()