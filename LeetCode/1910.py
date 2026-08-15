class Solution(object):
    def removeOccurrences(self, s, part):
        while(1):
            if(part in s):
                s = s.replace(part, "",1)
            else:
                break    
        return s   
                