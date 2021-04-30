#LISTS and Global Values

# Lists and dictionares: If you change part of a list or dictionary locally, you also change it globally,
# even without using the keyword "global", so be careful when making such local changes
a = [1,2,3]

def f1():
    a[0] = 5
    print(a)

def f2():
    a = 50
    print(a)

print(a)
f1()
f2()
print(a)