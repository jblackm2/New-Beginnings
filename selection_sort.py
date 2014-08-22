# Copyright (c) 2014 Justin Blackmon
# Selection sort program
# Takes an unsorted list of numbers and sorts them lowest to highest

# Open file of numbers
f = open("selection.py")
lines = f.readlines()
f.close()

# Removes the whitespace
lines = [x.strip() for x in lines]
lines = [int(x) for x in lines]
# Caluclaing the number of elements in the list
n = len(lines)
print(lines)

def selection(lines):
    for i in range(0, n-1):
        # Make each i the low
        low = i
        for j in range( i +1, n):
            # if j is less than the current low, it replaces it
            if lines[j] < lines[low]:
                low = j
        # Swap the positions
        lines[i], lines[low] = lines[low], lines[i]
    return lines

print(selection(lines))
