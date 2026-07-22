n, k, l, c, d, p, nl, np = map(int, input().split())
total_litre = l*k
total_slice = c*d
f = 1
while (1):
    if (n*nl*f) <= total_litre and (n*np*f) <= p and (n*f) <= total_slice:
        f += 1
    else:
        break

print(f-1)
