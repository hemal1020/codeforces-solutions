x = int(input())
a = input().rstrip().split(" ")

for i in a:
    if i=="1":
        print("Hard")
        exit()

print("EASY")