def crossroads():
    while True:
        picked_direction = input('Mountains (M) \n'
                                 'Village (V) \n'
                                 'Castle (C) \n'
                                 'Forrest (F) \n'
                                 '>>>> '
                                 )
        picked_direction = picked_direction.capitalize()
        if picked_direction == 'M' or 'V' or 'C' or 'F' :
            picked_direction = True
            break
        else:
            print('This direction is not yet avaible')

    if picked_direction.capitalize() == 'M':
        print(f'You travel up the slope of the mountains.')
    elif picked_direction.capitalize() == 'V':
        print(f'You go straight to peaceful (?) village. ')
    elif picked_direction.capitalize() == 'C':
        print(f'You castle. Maybe theres a princess to rescue. ')
    elif picked_direction.capitalize() == 'F':
        print(f'You enter deep gloomy forrest. ')



crossroads()



