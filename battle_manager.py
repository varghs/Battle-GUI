import tkinter

from screen_battle import Screen_Battle
from screen_prepare_to_battle import Screen_PrepareToBattle
from screen_character_selection import Screen_CharacterSelection
from characters import CharacterRoster

class BattleManager (object):
    
    def __init__ (self):
        '''
        Initializes a new battle manager by loading the list of characters from the file and
        by initializing a tkinter window.
        Although several important properties are declared, they are not given values yet.
        Notably, no screen is put into the window yet, nor any Character or CharacterRoster created yet.
        '''
        self.root = tkinter.Tk()
        self.current_screen = None
        self.character_roster = None
        self.player = None
        self.computer = None
    
    def setup_character_selection (self):
        '''
        This method is called to set up the Character Selection screen. 
        This also initializes the character_roster property.
        '''
        # Changes the window's title
        self.root.title ("Select your character!")
        # Reads battle_characters.txt to create a CharacterRoster.
        self.character_roster = CharacterRoster ("battle_characters.txt")
        # Creates and displays a Character Selection screen
        self.current_screen = Screen_CharacterSelection(master = self.root, 
                                                        roster = self.character_roster, 
                                                        callback_on_selected = self.onclose_character_selection
                                                        )
               
    def onclose_character_selection (self, selected_char_index):
        ''' This method is called when the user presses the button on the Character Selection screen. 
            selected_char_index should contain the index in the list of the character selected by the user. 
            The method manages the assignment of the player and computer properties (Character objects), 
            and then starts the Prepare for Battle screen.
            '''        
        selected_char_index = int (selected_char_index)
        
        # Gets the player's chosen Character
        self.player = self.character_roster.get_and_remove_character(selected_char_index)
        
        # Gets a different random Character for the computer.
        self.computer = self.character_roster.get_random_character()
        
        # Destroys the Character Selection window
        self.current_screen.destroy()

        # Continue on - set up the Prepare To Battle screen!
        self.setup_prepare_to_battle()

    def setup_prepare_to_battle(self):
        ''' This method is called to set up the Prepare To Battle screen. '''

        # Changes the window's title
        self.root.title ("The Combatants!")

        # Creates and displays a Prepare To Battle screen
        self.current_screen = Screen_PrepareToBattle(master = self.root, 
                                                    player1 = self.player, 
                                                    player2 = self.computer, 
                                                    callback_on_commence_battle = self.onclose_prepare_to_battle
                                                    )
    
    def onclose_prepare_to_battle (self):
        ''' 
        This method is called when the user presses the button on the Prepare to Battle screen.
        The method closes the Prepare To Battle screen and creates the Battle screen.
        '''
        # Destroys the Prepare To Battle screen
        self.current_screen.destroy()

        # Continue on - set up the Battle screen!
        self.setup_battle()


    def setup_battle(self):
        ''' This method is called to set up the Battle screen. '''
        # Changes the window's title
        self.root.title ("Battle!")

        # Creates and displays a Battle screen
        self.current_screen = Screen_Battle(master= self.root, 
                                            player1 = self.player, 
                                            player2 = self.computer, 
                                            callback_on_exit = self.onclose_battle
                                            )

    def onclose_battle (self):
        ''' 
        This method is called when the user presses the finishing button on the Battle screen, 
        after the battle is done.  This method closes the entire window, causing the program to exit.
        '''

        # Destroy the entire program's window, which includes the Battle screen.
        self.root.destroy()
        
def main():
    # Create the battle manager, which creates the tkinter window.
    battle = BattleManager()
    # The program begins with the Character Selection screen!
    battle.setup_character_selection()
    # Run the program!
    battle.root.mainloop()
 
main()
    