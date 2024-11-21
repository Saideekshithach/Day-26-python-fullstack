#global and local variables

#A variables inside and outside the function is global and local variables

#A variable defined above the function and is accessible to the entire global space is called a global variable.

#A variable is inside the function is called local variable

'''a=4
def check():
    print("inside the value is",a)
check()
print("outside the function",a)'''

#second case of global variables
'''a=2
def check2():
    a=5#creating a variable
    a=a**2
    print("inside the value",a)
check2()
'''

#third case of both global and local variables
'''a=3
b=4
def check3():
    a=6
    print("inside the value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b=b+a
    print("b value is",b)
check3()
print("a value is",a)
print("b value is",b)'''

#usage
#when user wants to access the global variable inside the function directly and carry forward the updated value even outside the function then we need to use global keyword.
'''a=4
b=5
def final():
    global a,b #global variable a,b
    print("inside value is",a)
    a=7
    print("updated value is",a)
    b=13#local variable
    b=b+a
    print("b value is",b)
final()
print("a value is",a)
print("b value is",b)'''

#max(),min(),sum()
print(max(3,6,8,9,1,2,4,5))
print(min(3,6,8,9,1,2,4,5))
a=(3,6,8,9,1,2,4,5)
print(sum(a))
print(sum((4,6,5,3,2,3)))
print(sum([5,7,8]))


