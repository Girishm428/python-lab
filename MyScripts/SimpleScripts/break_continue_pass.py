list1=[4,6,8]
list2=[2,3]

for i in list1:
    for j in list2:
        if j == 3:
            break
        print(i//j)
    print("can't do a perfect division with", i, "by", j)


for i in list1:
    for j in list2:
        if j == 3:
            continue
        print(i//j)
    print("can't do a perfect division with", i, "by", j)