import re
a = input()
numbers = re.findall(r'\d+', a)
x= sorted(numbers)
for i in range(len(x)):
    if i == len(x)-1:
        print(x[i],end="")
    else:
        print(x[i],end="+")


