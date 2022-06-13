border_size = 20
topbar_height = 100

#SingleMode
board_size = (40,40)
cell_size = (15,15)
display_width = border_size * 2 + board_size[0] * cell_size[0]
display_height = border_size * 2 + topbar_height + board_size[1] * cell_size[1]
#DualMode
Dboard_size=(40,80)
Dcell_size=(8,8)
Ddisplay_width=border_size*2+Dboard_size[0]*cell_size[0]
Ddisplay_height=border_size*2+Dboard_size[1]*cell_size[1]


title = "Snake Game"


import os
from pathlib import Path

base = str(Path(__file__).absolute().parent.parent)
icon_path = os.path.join(base, "images/icon.png")
font_style = os.path.join(base, "fonts/arial.ttf")
save_dir = os.path.join(base, "data")
save_state_path = os.path.join(base, "data/gamescene.dat")
save_rankings_path = os.path.join(base, "data/score.dat")

bg_path = os.path.join(base, "images/titlescene/bg.png")

f_path = os.path.join(base, "images/buttonframe.png")
f_hover_path = os.path.join(base, "images/buttonframe_hover.png")
f_down_path = os.path.join(base, "images/buttonframe_down.png")

f2_path = os.path.join(base, "images/buttonframe2.png")
f2_hover_path = os.path.join(base, "images/buttonframe2_hover.png")
f2_down_path = os.path.join(base, "images/buttonframe2_down.png")

