from characters import CharacterRoster, Character

def main():
    # Loads the character roster from the file
    character_choices = CharacterRoster ("battle_characters.txt")

    # Get the user's choice
    print ("Prepare to battle!\n\nWhich character would you like?")
    character_choices.print_roster()
    iMax = character_choices.get_number_of_characters()
    choice = int(input())
    while choice < 0 or choice >=iMax:
        choice = int(input ("Please choose between 0 and " + str (iMax) + "."))
    
    # Get the character for the user and the computer.
    player = character_choices.get_and_remove_character(choice)
    computer = character_choices.get_random_character()
    
    # Preparation for the battle
    print ("You have picked: " + str(player))
    print ("The computer picked: " + str(computer))
    print ("Let's battle!\n")
    
    # Battle Loop
    rnd = 1
    while player.hit_points > 0 and computer.hit_points > 0:
        print ("Round: " + str (rnd))
        print (player.name + ": " + str(player.hit_points) + " hit points remaining.")
        print (computer.name + ": " + str(computer.hit_points) + " hit points remaining.")
        input ("\nPress enter to attack!")

        # Player attacks first, then Computer attacks back (if alive)
        print(player.attack (computer))

        if computer.hit_points > 0:
            print(computer.attack (player))

        print()
        # Next round! (unless someone died)
        rnd += 1

    # Print post-battle death message:
    if computer.hit_points <= 0:
        print(computer.get_death_message())
    elif player.hit_points <= 0:
        print(player.get_death_message())

main()
    