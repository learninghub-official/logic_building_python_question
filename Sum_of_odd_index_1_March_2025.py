# Get the sum of index

l = [1,7,3,2,5,4]
#   [5,4,3,2,1,0]

# 5+3+1 = 9
sum = 0
for i in range(len(l)):
    if i%2 != 0:
        print(i)
        sum = sum + i
print("sum = ",sum)


    
