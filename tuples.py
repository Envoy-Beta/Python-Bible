our_tuple = 1,2,3,"A","B","C"
print(type(our_tuple))

our_tuple = (1,2,3,"A","B","C")
print(type(our_tuple))

print(our_tuple[0:3])

#Turn list into a Tuple
A = [1,2,3]
A = tuple(A)
print(type(A))

#Store Multiple Variables with Tuples, All at Once

(A,B,C) = 1,2,3
print(A)
print(B)
print(C)

#Store Multiple Variables with Lists, All at Once (For Tuples on the Left Side of equation)
D,E,F = [4,5,6]
print(D)
print(E)
print(F)

#Store Multiple Variables with Strings, All at Once
G,H,I = "789"
print(G)
print(H)
print(I)
