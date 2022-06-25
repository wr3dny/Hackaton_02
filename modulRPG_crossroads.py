def crossroads():
    while True:
        picked_direction = input('Mountains (M) \n'
                                 'Village (V) \n'
                                 'Castle (C) \n'
                                 'Forrest (F) \n'
                                 'Port (P)\n'
                                 '>>>> '
                                 )
        if picked_direction.capitalize() == 'M':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'C':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'V':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'F':
            picked_direction = True
            break
        elif picked_direction.capitalize() == 'P':
            picked_direction = True
            break
        else:
            print('Direction currently not available')
        direction = picked_direction
        return direction



crossroads()
