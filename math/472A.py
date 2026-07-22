def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


a = int(input())
if a % 2 == 0:
    print(4, a-4)
    exit()
else:
    c = 6
    while (1):
        if is_prime(c) or is_prime(a-c):
            c += 1
        else:
            print(c, a-c)
            exit()
