import string

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = ''.join([c for c in s if c in string.ascii_lowercase or c in string.digits])
        return s == s[::-1]