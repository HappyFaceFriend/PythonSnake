
import Settings

def save_gamescene(gamescene):
    pass

def save_score(score):
    file = open(Settings.save_score_path, 'w')
    file.write(str(score))
    file.close()

def load_gamescene():
    return None

def load_score():
    try:
        file = open(Settings.save_score_path, 'r')
        score = int(file.read())
        file.close()
        return score
    except:
        return 0