# Copyright (c) 2014 redacted
# Should print two columns, using 0,1's
# First column 0 mean message is ham, 1 is spam
# Second column 0 means the message has no !, 1 means it cotains !
# Should be able to set parameters, number of rows, percent ham,
# percent ham/spam with a !

import random

# Main function to generate columns
def ham_spam():
    
    # Lists for columns
    first = []
    second = []
    
    # Variables 
    l = 10
    frac_ham =.66
    frac_ham_ex =.2
    frac_spam_ex =.9

    # Convert variables to whole numbers for random generator
    frac_ham = frac_ham * 100
    frac_ham_ex = frac_ham_ex * 100
    frac_spam_ex = frac_spam_ex * 100

    # Generate column of ham or spam
    for i in range(l):
        column1 = random.randrange(1,101,1)
        if column1 <= frac_ham:
            first.append("0")
        else:
            first.append("1")
        
        
    # Generate column of exclamation point or no    
    for i in first:
        column2 = random.randrange(1,101,1)
        if i == "0":
            if column2 <= frac_ham_ex:
                second.append("1")
            else:
                second.append("0")
        elif i == "1":
            if column2 <= frac_spam_ex:
                second.append("1")
            else:
                second.append("0")
                
    # Print the two columns
    for i in range(l):
        print(first[i], second[i])

    # Return to function
    return l, first, second

if __name__ == "__main__":
    ham_spam()


   



    

    

    
    
    
            
        

    
        

