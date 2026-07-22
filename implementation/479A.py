a = int(input())
b = int(input())
c = int(input())

maximum = max(a+b*c, a*(b+c), a*b*c, (a+b)*c, a*b+c, a+b+c)
print(maximum)
