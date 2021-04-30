#Unpacking: Each element of a list or string becomes its own argument in a function
# *args = shorthand for arguments
print(1,2,3,4,5)

numbers = [1,2,3,4,5]

print(numbers)

print(*numbers)

print ("abc")

print(*"abc")

print("a", "b", "c")

#Packing Arguments

def add(x,y): #Only adds two numbers
    return x + y

add(10,10)

#Pack in as many numbers as possible, so whatever numbers you pass through the variable are going to
# to be packed into one tuple called numbers
#Because tuples are iterable and we can loop through them and we can add them up
def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return (total)

print(add(1,2,3,4,5,6,7,8,9))

#Packing and Unpacking Keyword Arguments...will use dictionaries

# Unpacking Example of a Keyword Argument

def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
    return sentence

dictionary = {"name": "Ziyad", "age": 23, "likes": "Python"}

# Use one star for normal arguments
# Use two stars for Keyword Arguments
# Doesn't matter what order you put parameter:argument pairs in, so the age pair and likes pair can
#go before the name pair

about(**dictionary)

print(about(**dictionary))




# Packing Example of a Keyword Argument

def foo(**kwags): # Kwags = Keyword Arguments
    for key, value in kwags.items():
        print("{}:{}".format(key, value))

foo(Huda = "female", Ziyad = "male", John = "male")
