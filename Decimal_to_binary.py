# 10 in binary = 1010
# Then we toggle this binary 1010 = 0101
# Then convert this toggeled binary to decimal 0101 = 5

# Here 10 is the input and 5 is the output


# Taking Input

n = int(input())

# Converting decimal to binary

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""

    while n > 0:
        reminder = n%2
        binary = str(reminder) + binary
        n = n//2

    return binary
# print(decimal_to_binary(n))
b = decimal_to_binary(n)
# print(b)
# Converting binary to decimal

# binary = "1010"

# for i in b:
#     # print(i)
#     if i == " ":
#         return None
#     else:



