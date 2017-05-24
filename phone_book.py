running = True
# this code is so cool

while running:

    try:
        query = int(input('Enter 1 to search phonebook, enter 2 to quit: '))
    except ValueError:
        print('Input must be a number. Please try again.')
        continue

    if query == 1:
        print('Thank you.')
        running = False
    elif query == 2:
        quit()
    else:
        print('I did not understand that.')
