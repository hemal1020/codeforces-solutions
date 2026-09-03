class Solution(object):
    def isHappy(self, n):
        a=n
        while(1):
            count = 0
            while(a//10!=0):
                count = count +  (a %10)**2
                a = a//10
            count = count + a**2 
            a = count 
            if(a==2 or a==3 or a==4 or a==9 or a==5 or a==6 or a==8):
                return False
            elif(a ==1  or a==7  ):
                return True

sol = Solution()
print(sol.isHappy(12))             