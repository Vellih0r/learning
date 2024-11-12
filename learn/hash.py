voted = {}

def check_voter(name):
    if voted.get(name):
        print("Already vote!")
    else:
        voted[name] = True
        print("Let them vote")