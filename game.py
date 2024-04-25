import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at a crossroads.")
    time.sleep(1)
    print("Which path will you take?")

def crossroads():
    print("\nYou are at a crossroads.")
    print("1. Go left into the dark forest.")
    print("2. Go right towards the mountains.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        forest()
    elif choice == '2':
        mountains()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        crossroads()

def forest():
    print("\nYou enter the dark forest.")
    time.sleep(1)
    print("As you move deeper into the forest, you hear strange noises.")
    time.sleep(1)
    print("What will you do?")
    print("1. Investigate the noises.")
    print("2. Continue walking quietly.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("\nYou investigate the noises and encounter a friendly woodland creature.")
        time.sleep(1)
        print("The creature guides you safely through the forest.")
        time.sleep(1)
        print("Congratulations, you've survived the forest!")
        time.sleep(1)
        play_again()
    elif choice == '2':
        print("\nYou continue walking quietly through the forest.")
        time.sleep(1)
        print("Suddenly, you stumble upon a sleeping bear!")
        time.sleep(1)
        print("The bear wakes up and chases you away.")
        time.sleep(1)
        print("Game over!")
        time.sleep(1)
        play_again()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        forest()

def mountains():
    print("\nYou start climbing the mountains.")
    time.sleep(1)
    print("It's a tough climb, but the view from the top is breathtaking.")
    time.sleep(1)
    print("As you reach the summit, you notice a cave.")
    time.sleep(1)
    print("Will you enter the cave?")
    print("1. Enter the cave.")
    print("2. Stay on the mountain summit.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("\nYou enter the cave and find a treasure chest!")
        time.sleep(1)
        print("Congratulations, you've found the treasure!")
        time.sleep(1)
        play_again()
    elif choice == '2':
        print("\nYou decide to stay on the mountain summit and enjoy the view.")
        time.sleep(1)
        print("As you relax, you notice a storm approaching.")
        time.sleep(1)
        print("You quickly descend the mountain to safety.")
        time.sleep(1)
        print("Congratulations, you've survived the storm!")
        time.sleep(1)
        play_again()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        mountains()

def play_again():
    print("\nDo you want to play again?")
    choice = input("Enter 'yes' to play again, or 'no' to quit: ")
    if choice.lower() == 'yes':
        start_game()
    elif choice.lower() == 'no':
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_again()

def start_game():
    introduction()
    crossroads()

start_game()
