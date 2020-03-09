import string


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Time Complexity : O(N), where N is the length of the input string.
        Space Complexity = O(1) because we didnt s.split() to remove whitespace characters but handle whitespace characters themselves.
        """

        if not s:
            return 0

        i = 0
        sign = 1
        signAlreadyDefined = False
        parsingNumber = False

        signs = ["+", "-"]
        whitespace = " "

        for char in s:  # O(N) time complexity

            if char == whitespace:
                if parsingNumber:
                    break
                else:
                    continue

            if char in signs and (signAlreadyDefined or parsingNumber):
                break

            if char == "-":
                sign = -1
                signAlreadyDefined = True
                parsingNumber = True
                continue

            if char == "+":
                signAlreadyDefined = True
                parsingNumber = True
                continue

            if char not in string.digits:
                break

            i = 10 * i + int(char)
            parsingNumber = True
            signAlreadyDefined = True

        # overflow
        i = i * sign
        i = min(i, 2 ** 31 - 1)
        i = max(i, -(2 ** 31))

        return i
