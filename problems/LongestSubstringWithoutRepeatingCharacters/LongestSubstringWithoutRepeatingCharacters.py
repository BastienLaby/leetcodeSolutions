class Solution1:
    """
    Easy to understand.
    Store each encoutered characters and the iterate over the string and test if the character was encountered.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        current = 0
        maximum = 0
        characters = []
        for i in s:
            if i in characters:
                charIndex = characters.index(i)
                characters = characters[charIndex + 1 :]
                characters.append(i)
                current = len(characters)
            else:
                characters.append(i)
                current += 1
                maximum = max(current, maximum)

        return maximum
class Solution2:
    """
    User sliding window instead of encountered characters list.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:

        maximum = 0
        i, j = 0, 0

        for idx, char in enumerate(s):
            print(f"{char} in {s[i:j] or []} ?")
            if char in s[i:j]:
                maximum = max(maximum, j - i)
                i += s[i:j].index(char) + 1
                j = idx + 1
            else:
                j += 1
                maximum = max(maximum, j - i)

        return maximum
