numbers = [10, 20, 30, 40, 50]

# Find largest number
largest = max(numbers)

print("Largest:", largest)


# Find smallest number
smallest = min(numbers)

print("Smallest:", smallest)


# Find second largest
unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second Largest:", unique_numbers[-2])


# Reverse list
print("Reverse:", numbers[::-1])


# Sum of elements
print("Sum:", sum(numbers))


# Find even numbers
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers:", even_numbers)