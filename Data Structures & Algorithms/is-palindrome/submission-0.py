class Solution:
    def isPalindrome(self, s: str) -> bool:
        c ="".join(char.lower() for char in s if char.isalnum())
        return c==c[::-1]
