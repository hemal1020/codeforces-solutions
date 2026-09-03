class Solution(object):
    def exist(self, board, word):
        r,c= None,None 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==word[0]):
                     r = i
                     c = j
                     break
            if(r!=None):
                break    
        print(r,c)
        pr,pc = r,c    
        for i in range(len(word)-1):
            if (word[r][c+1]==word[i+1]):
                c+=1
            elif (word[r][c-1]==word[i+1]):    
                c-=1
            elif (word[r+1][c]==word[i+1]):
                r+=1
            elif (word[r-1][c]==word[i+1]):    
                r-=1   
            if(c==pc and r==pr):
                return False  
            else:
                pc =c 
                pr = r         
        return True  


                
sol = Solution()
print(sol.exist( [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
