class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            ar = set(s)
            for i in ar:
                if(s.count(i)==t.count(i)):
                    pass
                else:
                    return False
            return True
        else:
            return False     




sol = Solution()
print(sol.isAnagram("anagram","gaanamr"))
        