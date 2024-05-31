class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sumS={}
        sumT={}

        for i in range(len(s)):
            sumS[s[i]] = 1+sumS.get(s[i],0)
        for i in range(len(t)):
            sumT[t[i]] = 1+ sumT.get(t[i],0)
        return sumS == sumT
