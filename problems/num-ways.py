class Solution:
    def numWays(self, n, ways):
        if n == 0:
            ways[0] = 1
        if n == 1:
            ways[1] = 1
        if n not in ways:
            ways[n] = self.numWays(n - 1, ways) + self.numWays(n - 2, ways)
        return ways[n]


    def numWaysBottomUp(self, n):
        '''
        from : https://www.youtube.com/watch?v=5o-kdjv7FD0
        '''
        if n == 0 or n == 1:
            return 1

        nums = [1, 1]
        for i in range(2, n + 1):
            nums.append(nums[i - 1] + nums[i - 2])
        return nums[n]


    def numWaysRestricted(self, n, ways, steps):

        ways.setdefault(0, 1)

        if n in ways:
            return ways[n]

        total = 0
        leadingPaths = [n - s for s in steps if n - s >= 0]

        for l in leadingPaths:
            total += self.numWaysRestricted(l, ways, steps)
        ways[n] = total

        return ways[n]

    def numWaysRestrictedBottomUp(self, n, steps):
        '''
        from : https://www.youtube.com/watch?v=5o-kdjv7FD0
        '''
        if n == 0:
            return 1
        nums = [1]
        for i in range(1, n+1):
            total = 0
            for s in steps:
                if i - s >=0:
                    total += nums[i - s]
            nums.append(total)
        return nums[n]


if __name__ == '__main__':

    import timeit

    s = Solution()

    def numWays(n):
        ways = {}
        return s.numWays(n, ways)

    def numWaysRestricted(n, steps):
        ways = {}
        return s.numWaysRestricted(n, ways, steps)

    number = 10000

    print(timeit.timeit(lambda: numWays(100), number=number))
    print(timeit.timeit(lambda: s.numWaysBottomUp(100), number=number))
    print(timeit.timeit(lambda: numWaysRestricted(100, (1, 3, 5)), number=number))
    print(timeit.timeit(lambda: s.numWaysRestrictedBottomUp(100, (1, 3, 5)), number=number))
