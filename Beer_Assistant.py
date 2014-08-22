# Copyright (c) 2014 Justin Blackmon
# A GUI that will be used in homebrewing
# Will have a timer that counts down from 60 minutes, tells you when to add
# ingredients
# Allow user to enter ingredient types and amounts
# Save recipes for use later
# Calculate ABV%, IBUS, color

from tkinter import *
import time
from threading import Timer

class Application():
    def __init__(self, root):
        
        self.root = root

        self.container = Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.ingredients = Ingredients(self.container, self)
        self.ingredients.grid(row=0, column=0, sticky="nsew")
        
        self.recipe = Recipe(self.container, self)
        self.recipe.grid(row=0, column=0, sticky="nsew")

        self.showIngredients()
            
    def showIngredients(self):
        self.ingredients.tkraise()

    def showRecipe(self):
        self.recipe.tkraise()


class Ingredients(Frame):
    def __init__(self, root, application):
        super(Ingredients, self).__init__(root)

        self.root = root
        self.application = application
        
        self["borderwidth"] = 10
        self.grid()

        # Title for frame
        Label(self,
              text = "Enter your ingredients:",
              font = 10
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,
              text = "Recipe name:",
              font = 8
              ).grid(row = 0, column = 2, sticky = E)
        self.recipe_name_ent = Entry(self, width = 17)
        self.recipe_name_ent.grid(row = 0, column = 3, sticky = W)

        # Bittering hops type
        Label(self,
              text = "Bittering hops: "
              ).grid(row = 1, column = 0, sticky = W)
        self.bitter_hops_ent1 = Entry(self, width = 12)
        self.bitter_hops_ent1.grid(row = 2, column = 0,sticky = W)
        

        # Bittering hops amount
        Label(self,
              text = "Amount(oz): "
              ).grid(row = 1, column = 1, sticky = W)
        self.bitter_hops_ent2 = Entry(self, width = 7)
        self.bitter_hops_ent2.grid(row = 2, column = 1, sticky = W)
        

        # Flavor hops type
        Label(self,
              text = "Flavor hops: "
              ).grid(row = 3, column = 0, sticky = W)
        self.flavor_hops_ent1 = Entry(self, width = 12)
        self.flavor_hops_ent1.grid(row = 4,column = 0, sticky = W)
        
        # Flavor hops amount
        Label(self,
              text = "Amount(oz): "
              ).grid(row = 3, column = 1, sticky = W)
        self.flavor_hops_ent2 = Entry(self, width = 7)
        self.flavor_hops_ent2.grid(row = 4, column = 1, sticky = W)
        

        # Aroma hops type
        Label(self,
              text = "Aroma hops: "
              ).grid(row = 5, column = 0, sticky = W)
        self.aroma_hops_ent1 = Entry(self, width = 12)
        self.aroma_hops_ent1.grid(row = 6, column = 0, sticky = W)
        
        # Aroma hops amount
        Label(self,
              text = "Amount(oz): "
              ).grid(row = 5, column = 1, sticky = W)
        self.aroma_hops_ent2 = Entry(self, width = 7)
        self.aroma_hops_ent2.grid(row = 6, column = 1, sticky = W)
        
        # Specialty grains type
        Label(self,
              text = "Specialty grains: "
              ).grid(row = 7, column = 0, sticky = W)
        self.specialty_grains_ent1 = Entry(self, width = 12)
        self.specialty_grains_ent1.grid(row = 8, column = 0, sticky = W)
        
        # Specialty grains amount
        Label(self,
              text = "Amount(oz): "
              ).grid(row = 7, column = 1, sticky = W)
        self.specialty_grains_ent2 = Entry(self, width = 7)
        self.specialty_grains_ent2.grid(row = 8, column = 1, sticky = W)
        
        # Malt extract type
        Label(self,
              text = "Malt extract: "
              ).grid(row = 9, column = 0, sticky = W)
        self.malt_extract_ent1 = Entry(self, width = 12)
        self.malt_extract_ent1.grid(row = 10, column = 0, sticky = W)
        
        # Malt extract amount
        Label(self,
              text = "Amount (lbs): "
              ).grid(row = 9, column = 1, sticky = W)
        self.malt_extract_ent2 = Entry(self, width = 7)
        self.malt_extract_ent2.grid(row = 10, column = 1, sticky = W)
        
        # Yeast type
        Label(self,
              text = "Yeast:"
              ).grid(row = 11, column = 0, sticky = W)
        self.yeast_ent = Entry(self, width = 12)
        self.yeast_ent.grid(row = 12, column = 0, sticky = W)
        
        # Button to start the timer
        self.timer_bttn = Button(self, text = "Start Timer", font = 12,width = 17,
            command = self.timer)
        self.timer_bttn.grid(row = 1, column = 2)
        

        # Label where the alert message will appear
        
        self.alert_lbl = Label(self, text = "")
        self.alert_lbl.grid(row = 5, column = 2, columnspan = 3)
        self.alert_frame = Frame(self, borderwidth = 2, relief = "groove")
        self.alert_frame.grid(row = 5, column = 2, columnspan = 3)

        # Button to show the recipe screen
        self.recipe_bttn = Button(self, text = "Recipe", font = 12,width = 12,
            command = self.application.showRecipe)
        self.recipe_bttn.grid(row = 1, column = 3)

        

    # Timer method that will trigger the alert messages
    def timer(self):
        times = 0
        while times < 5:
            
            # Timer for entering the first ingredients
            if times == 0:
                t = Timer(1.0, self.timer_calls_1)
                t.start()
                times += 1

            # Timer for entering the second ingredients
            elif times == 1:
                t = Timer(20.0, self.timer_calls_2)
                t.start()
                times += 1
                
            # Timer for entering the third ingredients
            elif times == 2:
                t = Timer(30.0, self.timer_calls_3)
                t.start()
                times += 1

            # Timer for entering the fourth ingredients
            elif times == 3:
                t = Timer(45.0, self.timer_calls_4)
                t.start()
                times += 1

            # Timerfor entering the fifth ingredients    
            elif times == 4:
                t = Timer(55.0, self.timer_calls_5)
                t.start()
                times += 1

    # The call of the first timer
    def timer_calls_1(self):
        self.alert_lbl.configure(text ="Add your specialty grains, steep for 30 minutes.")
        
    # The cal of the second timer
    def timer_calls_2(self):
        self.alert_lbl.configure(text = "Add your bittering hops, and malt extract.")

    # The call of the third timer
    def timer_calls_3(self):
        self.alert_lbl.configure(text = "Add your flavor hops.")

    # The call of the fourth timer
    def timer_calls_4(self):
        self.alert_lbl.configure(text = "Add your aroma hops.")

    # The call of the fifth timer
    def timer_calls_5(self):
        self.alert_lbl.configure(text = "Cool your wort to below 75 degrees, and pitch your yeast.")
            
   
class Recipe(Frame):
    def __init__(self, root, application):
        super(Recipe, self).__init__(root)

        self.root = root
        self.application = application
        
        self["borderwidth"] = 10
        self.grid()

        # Label at top of the recipe window
        Label(self,
              text = "Recipe:", font = 10
              ).grid(row = 0, column = 0,columnspan = 4, sticky = W)

        # Text box where the recipe will appear
        self.recipe_txt = Text(self, width = 60, height = 15, wrap = WORD)
        self.recipe_txt.grid(row = 1, column = 0, columnspan = 2)

        # Button to produce the recipe on screen
        self.show_bttn = Button(self, text = "Show Recipe", font = 12,
            command = self.print_recipe)
        self.show_bttn.grid(row = 1, column = 3)

        # Button to save the recipe
        self.save_bttn = Button(self, text = "Save Recipe", font = 12,
            command = self.save)
        self.save_bttn.grid(row = 2, column = 3)
        
    # Called by the show recipe button
    def print_recipe(self):

        # Displays the current date
        now = time.strftime("%m/%d/%Y")

        # Displays all of the ingredients the user entered
        name = self.application.ingredients.recipe_name_ent.get()
        bitter1 = self.application.ingredients.bitter_hops_ent1.get()
        bitter2 = self.application.ingredients.bitter_hops_ent2.get()
        flavor1 = self.application.ingredients.flavor_hops_ent1.get()
        flavor2 = self.application.ingredients.flavor_hops_ent2.get()
        aroma1 = self.application.ingredients.aroma_hops_ent1.get()
        aroma2 = self.application.ingredients.aroma_hops_ent2.get()
        specialty1 = self.application.ingredients.specialty_grains_ent1.get()
        specialty2 = self.application.ingredients.specialty_grains_ent2.get()
        malt1 = self.application.ingredients.malt_extract_ent1.get()
        malt2 = self.application.ingredients.malt_extract_ent2.get()
        yeast = self.application.ingredients.yeast_ent.get()
        
        # Building up the recipe to be displayed
        recipe = "Bittering hops:"
        recipe += bitter1 + " " + bitter2 + "oz"
        recipe += "\nFlavor hops:"
        recipe += flavor1 + " " + flavor2 + "oz"
        recipe += "\nAroma hops:"
        recipe += aroma1 + " " + aroma2 + "oz"
        recipe += "\nSpecialty grains:"
        recipe += specialty1 + " " + specialty2 + "oz"
        recipe += "\nMalt extract:"
        recipe += malt1 + " " + malt2 + "lbs"
        recipe += "\nYeast:"
        recipe += yeast

        # Insert the recipe text
        self.recipe_txt.insert(0.0, name +"\n"+ now +"\n" + recipe)

    # For a future function to savethe recipe
    def save(self):
        print()
        

           
        
        
           
                





    
root = Tk()
root.title("Automated Brewer's Assistant")
root.geometry("600x300")
app = Application(root)
root.mainloop()


