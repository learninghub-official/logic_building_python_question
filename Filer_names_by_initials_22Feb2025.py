arry = ['A','B','M','N','G']
arry1 = ['Mayank','Nupur','Gavish','krish']

for j in arry1:
    for k in range(len(j)):
        for i in arry:
            if j[k] == i:
                print(j)

