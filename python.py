# user_input = input("Enter a string: ")
# print("Number of characters:", len(user_input))

# user_input = input("Enter a string: ").replace(" ","")
# print("Number of characters:", len(user_input))


words=[]
for i in range(5):
     word = input(f"Enter word {i+1}: ")
     words.append(word)
     print("\nWord Lengths:")
for word in words:
     print(f"'{word}' is {len(word)} characters")
