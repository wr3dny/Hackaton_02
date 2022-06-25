from colorama import Fore

def hero_att():
    hero_attributes = {
        'health' : 20,
        'energy' : 20,
        'attack' : 1
     }
    return hero_attributes

# print(Fore.YELLOW + str(hero_attributes.get('health')) + ' - ' + Fore.GREEN + (hero_attributes.get('health') * '#'))
# print(Fore.YELLOW + str(hero_attributes.get('energy')) + ' - ' + Fore.LIGHTCYAN_EX + (hero_attributes.get('energy') * '#'))



