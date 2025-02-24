# # Print the word with the maximum number of characters along with the count

# l = 'My name is Mayank I work at TCS' 
# k = l.split(" ")  # Splitting the string into words

# words_list = []  # Stores words
# length = []  # Stores word lengths

# # Loop through each word in the list
# for i in k:
#     words_list.append(i)  # Append word to words_list
#     length.append(len(i))  # Append word length to length list

# # Find the maximum length
# maximum = max(length)

# # Print words that match the max length
# for i in words_list:
#     if len(i) == maximum:
#         print(f"{i} ({maximum} characters)")


# The above code is using un necessary loop 

# here is the more precised way to solve this problem

l = 'My name is Mayank I work at TCS' 
k = l.split(" ") 

max_word = max(k, key=len)

print(max_word)
