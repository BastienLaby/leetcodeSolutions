class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Cast the given integer to a string, then check if the string is a palindrome
        """

        s = str(x)

        """
        Test if the string is a palindrome.
        Create two pointers i and j, starting at 0 and len(s) - 1 respectively.
        For each iteration, compare s[i] and s[j] and continue if the two values are the same by increasing i by 1 and decreasing j by 1.
        If j < i without characters differenciation, the word is a palindrome.
        """

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
