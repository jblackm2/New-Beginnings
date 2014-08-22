# Copyright (c) 2014 Justin Blackmon
# Map Drawing program
# Using Turtle use the input from a text file to draw a roadmap
# for type = "c" print "name", if "population" < 90000 draw small open circle
# if population > 90000 draw larger filled in circle at "X" "Y"
# if type = "R" draw line between the two cities listed


# import modules

from turtle import *
import csv
import sys

# import text file

city_list = csv.DictReader(open("oregonmap.csv"))

city_dict = {}        

# Main function loop

def city_print(city_list):
    for row in city_list:
        unit = row["Type"]

        # to print cities on map
        if unit == "c":
              
            x = float(row["X"])
            y = float(row["Y"])
            pop = int(row["Population"])
            name = row["Name"]
            
            # update dictionary of city coordinates 
            city_dict.update({name: [x, y]})
            penup()
            goto(x, y)
            pendown()
            
            if name[0] != "_":
                write(" " + " " + " " + " " + name, align = "left")
            if pop == 0:
                circle(0)
            elif pop > 90000:
                begin_fill()
                circle(7)
                end_fill()
            elif pop < 90000 and pop > 0:
                circle(3)
        
        # to print roads between cities
        elif unit == "r":
            
            name = row["Name"]
            x = row["X"]
            coordinates1_x = city_dict[name][0]
            coordinates1_y = city_dict[name][1]
            coordinates2_x = city_dict[x][0]
            coordinates2_y = city_dict[x][1]
            goto(coordinates1_x,coordinates1_y)
            pendown()
            goto(coordinates2_x, coordinates2_y)
            penup()
        
            
        continue
                
        return city_print

# Run function
city_print(city_list)
 



      
            

                           
