def crossroads():
    picked_direction = input('Mountains (M) \n'
                             'Village (V) \n'
                             'Castle (C) \n'
                             'Forrest (F) \n'
                             '>>>> '
                             )
    while picked_direction.capitalize() != 'M' or 'V' or 'C' or 'F':
        picked_direction = input('Mountains (M) \n'
                                 'Village (V) \n'
                                 'Castle (C) \n'
                                 'Forrest (F) \n'
                                 '>>>> '
                                 )
    else:
        if picked_direction.capitalize() == 'M' or 'V' or 'C' or 'F':


        if picked_direction.capitalize() == 'M':
            print(f'You travel up the slope of the mountains.')
        elif picked_direction.capitalize() == 'V':
            print(f'You go straight to peaceful (?) village. ')
        elif picked_direction.capitalize() == 'C':
            print(f'You castle. Maybe theres a princess to rescue. ')
        elif picked_direction.capitalize() == 'F':
            print(f'You enter deep gloomy forrest. ')



crossroads()



