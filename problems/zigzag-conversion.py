"""
Time complexity : O(N) where N is the length of the string
Space complexity : O(N) (the array used to save the rows)
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        array = []
        index = 0
        direction = 1

        for char in s:

            if len(array) < index + 1:
                array.append([])
            array[index].append(char)

            if index + direction == numRows or index + direction == -1:
                direction = -direction
            index += direction

        return "".join(["".join(i) for i in array])
