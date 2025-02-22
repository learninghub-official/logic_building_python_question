arry = ['A','B','M','N']
arry1 = ['Mayank','Nupur','Gavish']

for j in arry1:
    for k in range(len(j)):
        for i in arry:
            if j[k] == i:
                print(j)

