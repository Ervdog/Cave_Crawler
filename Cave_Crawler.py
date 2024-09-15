class Character:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Character Name: {self.name}")

# Introduction to the game
def game_introduction(character):
    print(f"\nWelcome, {character.name}, to the Forbidden Mountain Cave.")
    print("You approach the cave and are quickly met with the first problem.")
    print("You must choose between each path carefully and face the consequences.")

# First decision for the player
def first_choice():
    print("\nThere are two tunnels in front of you.")
    print("1. Enter the first tunnel (It looks dark and narrow).")
    print("2. Enter the second tunnel (it looks brighter but with a strange smell).")

    choice = input("\nWhat will you do? (Enter 1 or 2): ")
    
    if choice == "1":
        print("\nYou cautiously step into the dark and narrow tunnel...")
        print("The tunnel becomes tighter and darker, but you sense something ahead.")
        second_choice_tunnel_1()

    elif choice == "2":
        print("\nYou head towards the brighter tunnel with a strange smell...")
        print("As you move forward, the air becomes denser, and there are sounds in the distance.")
        second_choice_tunnel_2()

    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        first_choice()

# Continuation for the first tunnel choice
def second_choice_tunnel_1():
    print("\nAs you keep pressing forward, you stumble across a statue in a spacious room.")
    print("1. Move towards the statue.")
    print("2. Return back to the first two tunnels.")

    choice = input("\nWhat will you do? (Enter 1 or 2): ")

    if choice == "1":
        print("\nThe statue says the next warrior becomes death. YOU HAVE BECOME DEATH!")
        game_over()

    elif choice == "2":
        print("\nYou decide to go back, you feel that was the right choice...")
        first_choice()

    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        second_choice_tunnel_1()

# Continuation for the second tunnel choice
def second_choice_tunnel_2():
    print("\nAs you approach the smell it fades away, but a light appears...")
    print("1. Touch the light.")
    print("2. Run back...")

    choice = input("\nWhat will you do? (Enter 1 or 2): ")

    if choice == "1":
        print("\nYou touch the light and it transports you to another world and another cave, again...")
        first_choice()

    elif choice == "2":
        print("\nYou turn back and run but you trip and fall head first only to die...")
        game_over()

    else:
        print("\nInvalid choice. Please enter 1 or 2. ")
        second_choice_tunnel_2()


# Game Over Function
def game_over():
     print("\nGame Over! You have met your fate early...")
     restart_game()

# Restart Game Function
def restart_game():
    choice = input("\nWould you like to restart the game? (yes or no): ")

    if choice == "yes":
        print("\nRestarting the game...")
        main()

    elif choice == "no":
        print("\nThanks for playing! Goodbye!")
        exit()
    
    else:
        print("\nInvalid choice. Please enter 'yes' or 'no'.")
        restart_game()
         
# Main game function
def main(): 
 # Get the character's name from the user
 user_name = input("Enter the name for your character: ")

 # Create an instance of Character with the user's name
 player_character = Character(user_name)

 # Display the character's information
 player_character.display_info()

 # Introduce the character to the game world
 game_introduction(player_character)

 # Present the first choice
 first_choice()

# Start the game
if __name__ == "__main__":
    main()
