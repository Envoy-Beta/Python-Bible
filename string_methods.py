
#string methods...functions specific to the string data type
#Format Example: string.method()
#Example "hello".count("e")
# Variables that contain string can take the place of "string" in the example, as well. See below:

text = "happy birthday" 
text.count("a")
print(text.count("a"))

x = "Happy Birthday"

#Convert string to lowercase

x.lower()

print(x.lower())

#Convert string to uppercase
x.upper()

print(x.upper())

#Strings are an immutable datatype, i.e. they cannot be changed. See below:
print(x)

#Yet, "x" can be overwritten. See below:

x = x.upper()

print(x)

x = x.lower()

print(x)

# Capitalize Method - Capitalize the very first word

x.capitalize()

x = x.capitalize()

# Title Case Method - Capitalizes the first letter of each word
x.title()

x = x.title()

# Validate Case of String
# Example
x.islower()
print(x.islower())

x.isupper()
print(x.isupper())

x.istitle()
print(x.istitle())

# Validate whether string all letters, i.e. no spaces

x.isalpha()
print(x.isalpha())

# Verify string is all numbers, no spaces

x.isdigit()
print(x.isdigit())

# Validate that all of string is alphanumeric, no spaces, no punctuations

x.isalnum()
print(x.isalnum())

# Find pieces of string" --if not found, there will do a hard stop, yielding an error message
# Case-sensitive
x.index("happy birthday")
print(x.index("happy birthday"))

x.index("ssdssdfd")
# Find pieces of a string --will issue a "-1" if value is not found, not causing system to stop/crash
# Case-sensitive

x.find("happy birthday")

x.find("dddsdsd")

len(x)