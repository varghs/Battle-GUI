import random

'''
NOTE: This is a full implementation of Character/CharacterRoster. 
You may replace parts of this with your own implementation - but 
note the NEW comments for some key changes from the original Battle lab. 
'''

class Character (object):
    ''' 
    The maximum dexterity of any character is 100.  
    This value may be used in the attack() method to determine the likelihood of the Character hitting the enemy.
    This is a class variable (shared among all Character objects), so it can be accessed with Character.MAX_DEXTERITY  
    '''
    MAX_DEXTERITY = 100
    
    def __init__ (self, name, hit_points, strength, dexterity, small_image, large_image):
        ''' 
        This method intializes a new Character object, setting up the properties
        name, hit_points, strength, and dexerity based upon the passed parameters. 
        NEW: Two parameters and properties are added here: small_image and large_image, which
        can be used by a GUI to visualize the character
        '''
        self.name = name
        self.hit_points = hit_points
        self.strength = strength
        self.dexterity = dexterity
        self.small_image = small_image
        self.large_image = large_image
        
    def attack (self, enemy):
        ''' 
        In this method, self attempts to attack the enemy (another Character object) .  

        First, the method uses self's and enemy's dexterity property to randomly determine if the attack lands.
        Exactly how this is implemented is up to you, but it should generally adhere to these rules:
        1) If the dexterity of self is higher than that of enemy, the probability increases.
        2) If the dexterity of self is lower than that of enemy, the probability decreases.

        If the attack lands, determine the amount of damage to be dealt to enemy. 
        It should be a random number between 0 and self's strength property.
        The enemy's hit points should then be reduced by that amount.
        
        Finally, the method should RETURN the result of the attack to the user.

        NEW: Instead of printing the result of the attack, the result is returned as a string.
        '''
        dex_advantage = ((self.dexterity - enemy.dexterity) / 2)
        hit_prob =   Character.MAX_DEXTERITY / 2 + dex_advantage
        hit_attempt = random.randrange(0,Character.MAX_DEXTERITY)
        if (hit_prob>= hit_attempt):
            damage = random.randrange (0, self.strength)
            enemy.hit_points -= damage
            result = (self.name + " hits " + enemy.name +" causing " + str(damage) + " damage.")
        else:
            result = (self.name + " misses " + enemy.name + ".")
        return result
        
    def get_death_message(self):
        ''' Returns (NOT print) a death message. It should include self's name '''
        return self.name + ": Ahhhhh.. too much damage!  I have died."
                
    def __str__ (self):
        ''' Return (NOT print) a string that includes the name, hit points, strength, and dexterity of this object (self). '''
        return self.name + "; HP: " + str(self.hit_points) + "; Strength: " + str(self.strength) + "; Dexterity: " + str(self.dexterity)        
        
class CharacterRoster (object):
    def __init__ (self, file_name):
        '''
        This method intializes a new CharacterRoster object, setting up a property character_list 
        and filling it with new Character objects.
        The Character objects are defined in the file file_name; each line describes the properties of a single character.
        The file is in comma separated format.  Each line of the file includes:
            <Name>,<Hit Points>,<Strength>,<Dexterity>
        '''
        self.character_list = []

        
        text_file = open(file_name,"r")
        
        for line in text_file:
            line = line.strip()
            my_fields = line.split(",")
            character = Character (my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), my_fields[4], my_fields[5])
            self.character_list.append(character)
    
    def print_roster(self):
        '''
        Prints a numbered list of all Characters in the roster.
        Use str() on each Character object to utilize the __str__ method.
        NOTE: This method isn't used by GUIs.
        '''
        for i in range (len(self.character_list)):
            print (str(i) +": " + str(self.character_list[i]))        
    
    def get_and_remove_character (self, i):
        ''' 
        Gets and returns the "ith" Character from the list, then removes the 
        character from the list.  (Removal so prevents the user and computer from 
        using the same character).
        '''
        ch = self.character_list[i]
        self.character_list.remove(self.character_list[i])
        return ch
    
    def get_random_character (self):
        ''' Gets and returns a random character from the list (for the computer). '''
        return random.choice(self.character_list)
    
    def get_number_of_characters (self):
        ''' Returns the number of Characters in the roster. '''
        return len(self.character_list)

