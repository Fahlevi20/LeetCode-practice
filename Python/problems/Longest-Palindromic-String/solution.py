class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0

        for i in range(len(s)):
            #Single Center
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen: # example 0, 0 (0-0+1) = 1 > reslen
                    res = s[l:r+1] # s[0:0+1] = [0:1]
                    resLen = r-l+1 #resLen = 0-0+1 = 1
                l-=1 #update l = 0-1 = -1
                r+=1 #update r = 0 +1 = 1 
              # l = -1, r = 1
            #Double Center    
            l,r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]: #example l = 0 >=0 and r = 1 > len(s) and s[l] 'b' == s[r] = a !=
                if (r-l+1)> resLen: #example l = 0, r = 1 (0+1) > resLen
                    res = s[l:r+1]
                    resLen = r-l +1
                l -= 1
                r+=1
        return res
