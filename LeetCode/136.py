nums = [4,1,2,1,2]
nums = sorted(nums)
l = len(nums)
print(nums)

i = 0
while(i<l):
    if(i==(l-1)):
        print(nums[i])
    elif (nums[i]!=nums[i+1]):
        print(nums[i])
        break
    else:
        i+=1
    i+=1    
    
        

 
