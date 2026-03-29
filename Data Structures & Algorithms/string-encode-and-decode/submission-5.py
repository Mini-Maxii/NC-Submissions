class Solution:

    def encode(self, strs: List[str]) -> str:
        #create a string using the length of the word and a delimiter to seperate words
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_list.append(word)
            i = j + 1 + length

        return decoded_list