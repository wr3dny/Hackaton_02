# RPG
# step by step so called 'concept'
from RPG_name_generator import name_generator




def hero_sex(name):
    if name[-1] == 'a':
        he_she = 'lady'
    else:
        he_she = 'sir'
    return he_she


def hero_attributes():

    pass


def inventory():
    items_list = []
    pass


def crossroads():
    picked_direction = input('Please choose Your path: \n'
                             'Mountains (M) \n'
                             'Village (V) \n'
                             'Castle (C) \n'
                             'Forrest (F) \n')
    if picked_direction.capitalize() == 'M':
        print(f'You travel up the slope of the mountains')
    pass


def mountains():
    pass


# def village():
#     pass
#
#
# def castle():
#     pass
#
#
# def forrest():
#     pass


def main():
    hero_name = name_generator()
    he_she = hero_sex(hero_name)
    print(f'{he_she.capitalize()} {hero_name} Your journey beggins' )
    crossroads()
    pass


if __name__ == '__main__':
    main()
