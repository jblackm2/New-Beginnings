# Copyright (c) 2014 Justin Blackmon
# Mergesort program
# Read a file of integers one and at a time
# Merge sort them
# Open file of numbers

f = open("selection.py")
a = f.readlines()
f.close()

# Removes the whitespace
a = [x.strip() for x in a]
a = [int(x) for x in a]
# Caluclaing the number of elements in the list

print(a)

def merge(a1, a2):
    r = []
    while len(a1) > 0 and len(a2) > 0:
        if a1[0] <= a2[0]:
            r.append(a1[0])
            del a1[0]
        else:
            r.append(a2[0])
            del a2[0]
    
    return r + a1 + a2

def merge_sort(a):
    n = len(a)
       
    if n < 2:
        return a
    a1 = a[0: n// 2]
    a2 = a[n//2 : n]
    print(a1)
    print(a2)
    a1 = merge_sort(a1)
    a2 = merge_sort(a2)
    r = merge(a1, a2)
    return r


        

