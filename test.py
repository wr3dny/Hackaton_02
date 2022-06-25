def what_to_do():
    print('|| Welcome||')
    print('What You want to do ?')
    options = int(input('1 - new game, 2 - continue, 3 - quit'))
    return options

def menu():
    try:
        what_to_do()
    except ValueError as e:
        print('Its not what I meant')


