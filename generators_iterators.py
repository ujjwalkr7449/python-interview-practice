def numbers():

    for i in range(1, 6):
        yield i


for number in numbers():
    print(number)
    
def even_numbers(limit):

    for i in range(limit + 1):

        if i % 2 == 0:
            yield i


for number in even_numbers(10):
    print(number)

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

def large_numbers():

    for i in range(1000000):
        yield i


numbers = large_numbers()

print(next(numbers))
print(next(numbers))