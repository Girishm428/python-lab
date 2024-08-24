list1=[5,6,7]
list2=[0,1,2]

for i in list1:
    for j in list2:
        try:
             print(i/j)
        except ZeroDivisionError as e:
            print(e,",Error Not allowed")
        else:
            print("Division sucessful")