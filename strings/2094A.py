for i in range(int(input())):
    s = input()
    print(s[0], end="")
    for x in range(len(s)):
        if " " == s[x]:
            print(s[x+1], end="")
        if x==len(s)-1:
            print()
            break    
    