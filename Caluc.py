print("Hello")
name = 'Rohin'

def add(name):
    name = 'kumar'
    a = 10
    b = 40
    c = a + b
    print(c)
    print(name)
    if a == 10:
        print(a)

myfloat = 7.0
print(myfloat)
myfloat = int(7)
print(myfloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
hello = "hello"

print(one)

a, b = 3, 4
print(a,b)

add(name)



mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append("Hello")
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x - int(0))
    print(x)

helloworld = "hello" + " " + "world"
print(helloworld)