A = [5, 12, 72, 55,81, 7]
#Add items  to lists
A = A + ["BCD"]
print(A)

#Will add each index of list individually to existinh list
A = A + list("BCD")
print(A)

#Add list as its own element, within existing list
A = A + [[5,6,7,8]]
print(A)
 
#OR use

A.append([21,42, 39, 13])
print(A)


A = [5, 12, 72, 55,81, 7]

#Insert a specific item at a specific index
A.insert(2, 75)
print(A)

A.insert(2, 100)
print(A)

A.insert(2, [10, 20, 30])
print(A)


A.insert(4, "Stop Listening to Music!")
print(A)


