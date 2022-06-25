def port():
    import RPG_enemy as enemy
    print(f'On your way you come upon {enemy}')
    print('Fight or run (r/f)')
    choice = input()
    if choice.capitalize() == 'R':
        run = 'run'
        return run
    else:
        fight = 'fight'
        return fight

port()