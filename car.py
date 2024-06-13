command = ""
started = False
while True:
    command = input('> ').lower()

    if command == 'start':
        if started:
            print('Car has already started!')
        else:
            started = True
            print('Car has started...')

    elif command == 'stop':
        if not started:
            print('Car is already stoppped!')
        else:
            started = False
            print('Car has stopped')

    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit

""")
    elif command == 'quit':
        break

    else:
        print("Sorry, I don't understand")
