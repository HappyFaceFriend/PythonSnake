import Settings

gameDisplay = None
current_scene = None
next_scene = None

running = True

ranking = []
recent_score = 0

def change_scene(scene):
    global next_scene
    next_scene = scene

def quit_game():
    global running
    running = False