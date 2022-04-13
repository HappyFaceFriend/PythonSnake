
board_size = (40,40)
cell_size = (15,15)
display_width = 20 * 2 + board_size[0] * cell_size[0]
display_height = 20 * 2 + 100 + board_size[1] * cell_size[1]

title = "Snake Game"
icon_path = "images/icon.png"
font_style = "fonts/arial.ttf"


import TitleScene 

initial_scene = TitleScene.TitleScene()