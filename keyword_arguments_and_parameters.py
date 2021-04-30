def about(name, age, likes): # --> These are parameters, as tey are used to help define the function
    sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
    return sentence

print(about("Jax", 24, "Python")) # --> These are arguments,as they are passed to the function when we call it

#Keyword arguments allow you to input arguments, in any order, by using keys. See below:

print(about(likes = "Python", name = "Seren", age = 28))

# If missing a piece of input/information about user, input a default 
# response for said parameter using the assignment operator. Default vaulues
# have to go last, in your list of parameters. See below:

def about(name, age, likes = "Python"): # --> These are parameters, as tey are used to help define the function
    sentence = "Meet {}! They are {} years old and they like {}.".format(name, age, likes)
    return sentence

print(about("Xander", 21, "soccer"))

