def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]# we are making a 2D matrix of length =len(text2)+1 and len(text1)+1   row,column  and initialising it all to zeroes
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]# if the sting matches we are increasing dp by 1 
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]#because diagonally result is in the first box of the 2d matrix
    #tc and sc=O(m*n)
