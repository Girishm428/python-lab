slice1="slice me anywhere you want"

#slicefomat is string[start: stop: step]
a=slice1[5:8],slice1[5:],slice1[:8], slice1[:]
b=slice1[-9:-5]
c=slice1[::4],slice1[::-1]

print(a)
print(b)
print(c)


#slice & string

number1="0123456789"

d=number1[1::2], number1[1:5:2]

print(d)