a = input().lower()
vowel = "aeiouy"
for x in a:
    if x not in vowel:
        print("."+x,end="") 

# Method 2
print()
[print("."+x,end="") for x in input().lower() if x not in "aeiouy"]
