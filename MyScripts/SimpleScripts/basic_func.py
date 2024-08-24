x = "hello2"


def func1():
    print("hello1")

func1()

def func2(x):
    print(x)

func2(x)
func2("hello3")

y=10
z=20

def func3(y,z):
    sum=y+z
    return sum

print(func3(y,z))
print(func3(y,11))
