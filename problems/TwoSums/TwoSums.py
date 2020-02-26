class Solution(object):
    def twoSum(self, nums, target):

        numsMap = {}
        
        for i, num in enumerate(nums):
            
            complement = target - num
            if complement in numsMap:
                return [i, numsMap[complement]]
            numsMap[num] = i


if __name__ == "__main__":
    solution = Solution()
    solution.twoSum([2, 7, 11, 15], target=9)
