# Copyright (c) 2014 redacted
# Should read the data from gen-email.py
# Produce a table estimating the probabilities of ham or spam
# of future messages based on the exclamation point
# Pr(S|E) = Pr(E|S) Pr(S) / PR(E)
# Pr(S|E) = EnS/S * (S/l) / (E/l)
# Pr(H|E) = EnH/H * (H/1) / (E/1)
# Pr(H|N) = NnH/H * (H/l) / (N/l)
# Pr(S|N) = NnS/S * (S/1) / (N/1)

# import function from other module
from gen_email import ham_spam

# import lists from other module
l, first, second = ham_spam()


# Count occurences

s = first.count("1")
h = first.count("0")
e = second.count("1")
n = second.count("0")
h_e = 0
s_e = 0
h_n = 0
s_n = 0

# Determine the relation between the two columns
for i in range(l):
    if first[i] == "0" and second[i] == "1":
        h_e += 1
    elif first[i] == "1" and second[i] == "1":
        s_e += 1
    elif first[i] == "0" and second[i] == "0":
        h_n += 1
    elif first[i] == "1" and second[i] == "0":
        s_n += 1

# Calculate the probabilities
pr_s_e = ((s_e/s) * (s/l)) / (e/l)
pr_h_e = ((h_e/h) * (h/l)) / (e/l)
pr_s_n = ((s_n/s) * (s/l)) / (n/l)
pr_h_n = ((h_n/h) * (h/l)) / (n/l)   

# Print table 
print("    ", "N","   ", "E")
print("H", " ", "%.2f" %pr_h_n , " ","%.2f" %pr_h_e)
print("S", " ", "%.2f" %pr_s_n, " ","%.2f" %pr_s_e)
