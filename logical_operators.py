C = 10 
D = 5

#Comparison operators compare pieces of information, in order to make conditions
#Logical operators combine and modify conditions, in order to create larger and more complex conditions


#"not" operator "not"
# Examples

# not True

# not False

# not 2 < 3

# "and" operator 
#Example


if C > 10 and D > 1:
    print("It worked!")

if not (C > 10 and D > 1):
    print("It worked!")

#"or" operator 

# Example

# C = 10 
# D = -1
if C > 1 or D > 1:
    print("It worked!")

# C = 6
# D = 2
if (C > 5 and D > 5) or (C > 1  and D > 1):
   print("It worked!") 

# C = 6
# D = 2

if not ((C > 5 and D > 5) or (C > 1 and D > 1)):
   print("It worked!")