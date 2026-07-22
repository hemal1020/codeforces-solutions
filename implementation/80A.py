def is_prime(n):
    if n <= 1:
        return -1
    for i in range(2, int(n**0.5) + 1):  # check up to square root of n
        if n % i == 0:
            return -1
    return n


a, b = map(int, input().split())
for i in range(a+1, b+1):
    x = is_prime(i)
    if x == -1:
        pass
    else:
        if b == x:
            print("YES")
            break
        else:
            print('NO')
            break
    if i == b:
        print("NO")
