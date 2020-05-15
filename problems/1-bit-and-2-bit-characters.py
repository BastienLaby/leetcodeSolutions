class Solution:
    def isOneBitCharacter(self, bits):

        skip = False
        last_char = None
        for b in bits:
            if skip:
                skip = False
                continue
            if b == 0:
                last_char = b
                continue
            elif b == 1:
                last_char = b
                skip = True

        return last_char == 0

    def moreElegantSolution(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1
