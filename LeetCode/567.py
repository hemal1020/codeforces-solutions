class Solution(object):
    def checkInclusion(self, s1, s2):
        l = len(s1)
        fl = len(s2)
        d = list(set(s1))
        dl = len(d)
        i,j=0,0
        while(1):
            if(s2[j] in s1):
                if(s1.count(d[i])==s2[j:(l+j)].count(d[i])):
                    i+=1
                else:
                    j+=1
                    i=0
            else:
                j+=1
                i=0 
            if(i==dl):
                return True
            elif(j>fl-l):
                return False                



sol = Solution()
print(sol.checkInclusion("ab",  "eidboaoo"))    