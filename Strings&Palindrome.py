# Reverse a string

text = "python"

reverse_text = text[::-1]

print("Original:", text)
print("Reverse:", reverse_text)


# Check palindrome

word = "madam"

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


# Count vowels

text = "hello world"

vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Vowels:", count)


# Count characters

text = "python"

for char in text:
    print(char)