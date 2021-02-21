text = input("Enter the word: ")
vowels = 0
text.lower()
for i in text:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
         vowels = vowels + 1
print("The number of vowels is: ", vowels)