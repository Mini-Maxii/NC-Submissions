class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])): #take the first word only
            for j in range(1,len(strs)): #go through the other words
                if i >= len(strs[j]) or strs[j] == "":
                    return res
                if strs[0][i] != strs[j][i]: #compare each letter of first word
                    return res
            res += strs[0][i]
        return res
            