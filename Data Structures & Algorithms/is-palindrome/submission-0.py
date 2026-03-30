class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum())
        no_space = "".join(clean.split())

        reverse = no_space[::-1]

        if no_space.lower() == reverse.lower():
            return True
        return False