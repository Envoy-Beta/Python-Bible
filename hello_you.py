# Ask user for name

name = input("What is your name?: ")
print(name)

#Ask user for age

age = input("What is your age?: ")

print(age)

#Ask user for city

city = input("What city do you live in?: ")

print(city)

#Ask user what they enjoy doing

hobby = input("What do you enjoy doing?: ")

print(hobby)

#Create output text - format function "{} {}".format()

string = "Your name is {} and you are {} years old. You live in {} and love {}."

output = string.format(name, age, city, hobby)

#Print output to screen

print(output)