
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
icon_path = "images/icon.png"
font_style = "fonts/arial.ttf"
save_dir = "data"
save_state_path = "data/gamescene.dat"
save_rankings_path = "data/score.dat"
