class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #A hashmap that can will be returned a list

        for s in strs: #go through the elements of the array
            count = [0] * 26 #an array to keep count of element frequency
            for c in s: #go through the characters of each string
                count[ord(c) - ord("a")] += 1 #using -"a" to get the index in the right position
            res[tuple(count)].append(s) #check the count of each string tuple count and add it to one list
        return list(res.values()) #return the list of values in the map



        