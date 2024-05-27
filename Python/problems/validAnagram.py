class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        totalS={}
        totalT={}

        for i in range(len(s)):
            totalS[s[i]] = 1+totalS.get(s[i],0)
        for i in range(len(t)):
            totalT[t[i]] = 1+totalT.get(t[i],0)

        for b in totalS:
            if totalS[b] != totalT.get(b,0):
                return False
        return True
        


