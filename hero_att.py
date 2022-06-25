from colorama import Fore


def hero_attributes():
    health = 13
    energy = 20
    # if health in range((health * (2//3)), health):
    print(Fore.YELLOW + str(health) + ' - ' + Fore.GREEN + (health * '#'))
    print(Fore.YELLOW + str(energy) + ' - ' + Fore.LIGHTBLUE_EX + (energy * '#'))
    strenght = 1

hero_attributes()