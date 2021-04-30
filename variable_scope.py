# 1) Global Scope:
        #-creates global variables and can be seen anywhere in your program
# 2) Local Scope:
#       -creates local variables that can only be seen within the specific local scope that it is in
#       -functions create local scopes
#       -Loops and If statements do not create local scopes

a = 250

def f1():
    a = 100
    print(a)

def f2():
    a = 50
    print(a)

def f3():
    b = a + 20 #Can use global value of "a" inside of a local scope, if you do not change the global variable
    print(b)

def f4():
    global a
    a = 100
    print(a)


f1()
f2()
f3()
print(a)
f4()
print(a)


