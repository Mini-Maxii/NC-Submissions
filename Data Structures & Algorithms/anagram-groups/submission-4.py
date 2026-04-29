class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = {}
            for c in s:
                count[c] = count.get(c,0) +1
            key = tuple(sorted(count.items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())