class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): #go through the first string only
            for s in strs: #go through all the strings in the array
                if i == len(s) or s[i] != strs[0][i]: #if i reaches the length of the current string
                                                        #or the current string character does not equal the the first strings i character
                    return s[:i] #return the string and from the start to the current index 
        return strs[0] #return 