students = {}
students = {"Alice":25, "Bob":27, "Claire":17, "Dan": 21, "Emma":22}
students["Dan"]
print(students["Dan"])

students["Fred"] = 25
print(students["Fred"])

#Alice had a birthday; it needs to be updated in the dictionary
students["Alice"] = 26
print(students["Alice"])

#Fred dropped out of class and needs to be removed from the dictionary
#del students["Fred"]
#print(students["Fred"])

#How to use the Dictionary Keys Method
students.keys()

a = list(students.keys())
print(a[0])
print(a[1])
print(a[2])

#How to get values out of a dictionary with Values method
students.values()
b = list(students.values())
print(b[0])
print(b[1])
print(b[2])

#OR (Which is still WRONG)
#Dictionaries do not have an order like Lists and Tuples, so Indexing items will not work
#See below, for issues
#Will have to use key in order to get desired values
list(students.values())[2:]
print(list(students.values())[2:])

#Pull out items
c = list(students.items())
print(c)

