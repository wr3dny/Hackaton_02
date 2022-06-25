def what_to_do():
    print('|| Welcome||')
    print('What You want to do ?')
    options = int(input('1 - new game, 2 - continue, 3 - quit\n'
                        ''))
    return options

def menu():
    try:
        what_to_do()
    except ValueError as e:
        print('Its not what I meant. Restart game')
        # if int(what_to_do()) != (1 or 2 or 3) :
        #     what_to_do()
        # else:
        #     return what_to_do()


def main():
    menu()




