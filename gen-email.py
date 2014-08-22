# Copyright (c) 2014 Justin Blackmon
# Should print two columns, using 0,1's
# First column 0 mean message is ham, 1 is spam
# Second column 0 means the message has no !, 1 means it cotains !
# Should be able to set parameters, number of rows, percent ham,
# percent ham/spam with a !

import random
n =10
frac_ham =.5
frac_ham_ex =1
frac_spam_ex =0
first = []
second = []

def ham_spam(n, frac_ham, frac_ham_ex, frac_spam_ex):
    frac_ham = frac_ham * 100
    frac_ham_ex = frac_ham_ex * 100
    frac_spam_ex = frac_spam_ex * 100
    for i in range(n):
        column1 = random.randrange(1,101,1)
        if column1 <= frac_ham:
            first.append("0")
        else:
            first.append("1")
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
    for i in range(n):
        print(first[i], second[i])
    
            
        

    
        

