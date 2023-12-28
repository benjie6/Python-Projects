# Python Ver:   3.12.0
#
# Author:       Benjamin Vega
#
# Purpose:      Phonebook Demo. Demonstrating OOP, TKinter GUI module,
#               using TKinter parent  anf Child relationships.
#
#Tested OS:     This code was written and tested to work with Window 10.

from tkinter import *
import tkinter as tk




# Be sure to import our other modules
# so we can have access to them
import phonebook_gui
import phonebook_func


# Frame is the TKinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __int__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.mixsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The TKinter Phonebook Demo")
        self.master.configure(bg="#FOFOFO")
        # This protocol method is a tkinter built-in method to cath if
        # the user clickd the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master


        # load in the GUI widgets from a separate module,
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
