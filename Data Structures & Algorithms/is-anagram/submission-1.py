class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check length because if length is not equal then it's not an anamgram
        if len(s) != len(t):
           return False
        
        #solutions

        #solution 1
        #easy one is just sort and compare
     
        
        #solution 2
        #use a hashmap to count the occurance of each letter
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
   
        