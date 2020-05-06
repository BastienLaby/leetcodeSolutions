def get_next_pattern(full_pattern):
    if not full_pattern:
        return None
    elif len(full_pattern) == 1:
        return full_pattern
    elif len(full_pattern) > 1:
        if full_pattern[1] == "*":
            return full_pattern[:2]
        else:
            return full_pattern[0]


def match_pattern(char, pattern):
    """
    pattern must be a single character or a single character followed by "*".
    """
    return pattern[0] in {char, "."}


class Solution:

    def isMatch(self, text, pattern):

        if not pattern:
            return not text

        current_pattern = get_next_pattern(pattern)

        if not text:
            return False if "*" not in current_pattern else self.isMatch(text, pattern[2:])

        match_current = match_pattern(text[0], current_pattern)
        if "*" in current_pattern:
            # if the pattern with "*" match, we need to test two different cases:
            #   - next text char with current pattern
            #   - same text with next pattern
            # To avoid a False result with exemple input : text="aaa", pattern="a*a"
            return self.isMatch(text, pattern[2:]) or (
                match_current and self.isMatch(text[1:], pattern)
            )
        else:
            return match_current and self.isMatch(text[1:], pattern[1:])
