a="Name: {} Age: {} Gender: {}".format("Girish",32,"Male")

print(a)

b="Name: {2} Age: {1} Gender: {0}".format("Girish",32,"Male")

print(b)

c="Name: {2} Age: {1} Gender: {2}".format("Girish",32,"Male")

print(c)

name="Pooja"
age=29
gen="female"

d=f"Name: {name}, Age: {age}, Gender: {gen}"

print(d)

e=f"Name: {name.upper()}, Age: {age}, Gender: {gen[1]}, index: {gen.index("f")}"

print(e)
