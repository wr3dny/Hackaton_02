from colorama import Fore, Back


hero_attributes = {
    'health' : 13,
    'energy' : 20,
    'attack' : 1
 }

print(Fore.YELLOW + str(hero_attributes.get('health')) + ' - ' + Fore.GREEN + (hero_attributes.get('health') * '#'))
print(Fore.YELLOW + str(hero_attributes.get('energy')) + ' - ' + Fore.LIGHTCYAN_EX + (hero_attributes.get('energy') * '#'))

    # for health in range((health * (2//3)), health):
    # print(Fore.YELLOW + str(health) + ' - ' + Fore.GREEN + (health * '#'))
    # print(Fore.YELLOW + str(energy) + ' - ' + Fore.LIGHTBLUE_EX + (energy * '#'))
    # strenght = 1

