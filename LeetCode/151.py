class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        print(words)
        return " ".join(reversed(words))  


sol = Solution()
print(sol.reverseWords("the sky is blue"))