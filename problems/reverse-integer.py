def overflow(x):
    return x < -2147483648 or x > 2147483647


class Solution:
    def reverse(self, x: int) -> int:
        """
        Solution 1, type-based operation.
        Cast the given integer ton a string object, reverse the string, then cast it back to integer.
        Save the sign before casting and reapply it at the end of the operation.
        Time Complexity : In theory, O(N) with N = size of the str(x) string. In pratice, w <= len('2147483648'), so very fast
        Space Complexity : O(1)
        """

        # overflow test

        if overflow(x):
            return 0

        strX = str(x) if x >= 0 else str(x)[1:]
        reverseX = int(strX[::-1])

        if overflow(reverseX):
            return 0

        return reverseX * (1 if x > 0 else -1)

    def reverse_v2(self, x: int) -> int:
        """
        Solution 2, mathematical solution
        Divide (integer division) the given number by 10 and store the rest, while the resulting quotient is not 0.
        Multiply the resulting quotients by powers of 10 to retrieve the reversed number.
        Time Complexity : In theory, ?
        Space Complexity : In theory, O(N) with N = size of the str(x) string. In pratice, w <= len('2147483648'), so not very greedy.
        """

        sign = 1 if x >= 0 else -1
        x = sign * x

        reverseNumbers = []
        quotient = x // 10
        rest = x - quotient * 10
        reverseNumbers.append(rest)

        while quotient != 0:
            number = quotient
            quotient = number // 10
            rest = number - quotient * 10
            reverseNumbers.append(rest)

        k = len(reverseNumbers)
        reverseX = 0
        for i, y in enumerate(reverseNumbers):
            reverseX += 10 ** (k - i - 1) * y

        if overflow(reverseX):
            return 0

        return reverseX * sign
