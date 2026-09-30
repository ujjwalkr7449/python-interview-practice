try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:

    print("Please enter numbers only.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("Program completed.")
    
file = open("data.txt", "w")

file.write("Hello Ujjwal\n")
file.write("Learning Python")

file.close()

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

with open("data.txt", "w") as file:

    file.write("Python Interview Practice\n")
    file.write("FastAPI\n")
    file.write("Generative AI\n")


with open("data.txt", "r") as file:

    content = file.read()

    print(content)