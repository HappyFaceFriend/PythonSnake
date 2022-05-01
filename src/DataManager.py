
import Settings

ranking = []
try:
    file = open(Settings.save_rankings_path, 'r')
    ranking = eval(file.read())
    file.close()
except:
    file = open(Settings.save_rankings_path, 'w')
    file.write(str([]))
    file.close()
    pass

def add_ranking(name, score):
    if score == 0:
        return
    global ranking
    ranking.append((name, score))
    ranking.sort(key = lambda x: x[1], reverse = True)
    
    file = open(Settings.save_rankings_path, 'w')
    file.write(str(ranking))
    file.close()

def get_best_ranking():
    global ranking
    if len(ranking) == 0:
        return None
    return ranking[0]

def save_gamescene(gamescene):
    state = gamescene.get_state_dict()
    file = open(Settings.save_state_path, 'w')
    file.write(str(state))
    file.close()

def load_gamescene():
    try:
        file = open(Settings.save_state_path, 'r')
        state = eval(file.read())
        file.close()
        return state
    except:
        return None
    
