l = int(input())
a = list(map(int, input().split()))[1:]  # skips 1st element of array
b = list(map(int, input().split()))[1:]
list = set(a+b)
print(list)
for i in list:
    if l == len(list):
        print("I become the guy.")
        exit()
print("Oh, my keyboard!")
