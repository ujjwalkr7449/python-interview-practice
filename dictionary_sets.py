# Dictionary

student = {
    "name": "Ujjwal",
    "age": 22,
    "course": "Python"
}

print("Name:", student["name"])
print("Course:", student["course"])


# Add new value

student["city"] = "Bihar"

print(student)


# Frequency counting

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print("Frequency:", frequency)


# Set removes duplicates

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)


# Set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)