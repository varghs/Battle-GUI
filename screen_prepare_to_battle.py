import tkinter
import characters

class Screen_PrepareToBattle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
    
    def create_widgets(self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        labels = ["You", "Computer", f"{self.player1.hit_points} HP", f"{self.player2.hit_points} HP", f"{self.player1.dexterity} Dexterity", f"{self.player2.dexterity} Dexterity", f"{self.player1.strength} Strength", f"{self.player2.strength} Strength"]
        players = [self.player1, self.player2]
        i = 0
        count = 0
        while count < 5:
            for j in range(2):
                if count == 1:
                    imageLarge = tkinter.PhotoImage(file="images/" + players[j].large_image)
                    w = tkinter.Label (self, image = imageLarge)
                    w.photo = imageLarge
                    w.grid(row=count, column=j)
                    i -= 1
                else:
                    tkinter.Label(self, text=labels[i]).grid(row=count,column=j)
                i += 1
            count += 1
        
        tkinter.Button(self, text="Commence Battle!", command=self.commence_battle_clicked).grid(row=5,column=1,sticky=tkinter.E)

                

    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()