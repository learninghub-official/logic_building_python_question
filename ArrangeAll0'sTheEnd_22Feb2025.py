# Arrange all the zero's at the end of a new list from the given list

list = [0,7,5,7,4,2,9,0,8,0,8,0]

list1 = []   # This is the list of all Zero's
list2 = []   # This is the list of all non-zero's

for i in list:
    if i == 0:
        list1.append(i)
    else:
        list2.append(i)

# Now we have two list of zero's and non zero's elements

print(list1)
print(list2)


# But we have to make a single list of all elements with all zero's in the end of the list

list3 = []

for j in list2:   # We take list of nonzero's first as they are coming first
    list3.append(j)
for k in list1:
    list3.append(k)

print("final list: ", list3)


# Now we have to push this code in out github repo
