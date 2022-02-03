import tkinter

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.attack_bttn = tkinter.Button(self, text="Attack", command=self.attack_clicked)
        self.attack_bttn.grid(row=0,column=0)
        self.attack_output1 = tkinter.Label(self)
        self.attack_output1.grid(row=0,column=1)
        self.attack_output2 = tkinter.Label(self)
        self.attack_output2.grid(row=1,column=1)
        self.victory_label = tkinter.Label(self)
        self.victory_label.grid(row=2,column=1)
        text_labels = ["You", "Computer", f"{self.player1.hit_points}/{self.player1_max_hp} HP", f"{self.player2.hit_points}/{self.player2_max_hp} HP"]
        players = [self.player1, self.player2]
        self.hit_points_labels = []
        for i in range(1, 4):
            for j in range(2):
                if i == 2:
                    imageLarge = tkinter.PhotoImage(file="images/" + players[j].large_image)
                    w = tkinter.Label (self, image = imageLarge)
                    w.photo = imageLarge
                    w.grid(row=i+2, column=j)
                elif i == 3:
                    self.hit_points_labels.append(tkinter.Label(self, text=text_labels[i+j-1]))
                    self.hit_points_labels[j].grid(row=i+2,column=j)
                else:
                    tkinter.Label(self, text=text_labels[i+j-1]).grid(row=i+2,column=j)
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''
        self.attack_output1["text"] = self.player1.attack(self.player2)
        self.hit_points_labels[1]["text"] = f"{self.player2.hit_points}/{self.player2_max_hp} HP"
        if self.player2.hit_points > 0:
            self.attack_output2["text"] = self.player2.attack(self.player1)
            self.hit_points_labels[0]["text"] = f"{self.player1.hit_points}/{self.player1_max_hp} HP"
        else:
            self.attack_output2.destroy()
            self.victory_update(self.player1)
        if self.player1.hit_points < 0:
            self.victory_update(self.player2)
                                           
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()

    def victory_update(self, player):
        self.victory_label["text"] = f"{player.name} is victorious!"
        self.attack_bttn.destroy()
        tkinter.Button(self, text="Exit!",command=self.exit_clicked).grid(row=7,column=1,sticky=tkinter.E)