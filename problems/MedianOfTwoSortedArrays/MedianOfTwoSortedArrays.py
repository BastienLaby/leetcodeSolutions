class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int],) -> float:
        """
        median : value for which there are equals items before and equals items after

        if len(array) is odd --> median = middle element
        if len(array) is even --> median = mean of two middle elements

        exemple1 : median of [1, 5, 7] is 5
        exemple2 : median of [1, 2, 3, 4] is (2 + 3) / 2 = 2.5


        Given two sorted arrays (nums1, nums2), find the median M of the two sorted array.
        M = median(nums1 + nums2)
        nums1 and nums2 are supposed to be sorted

        """

        """
        Trivial solution :
        - merge the two arrays into one
        - sort the resulting array
        - compute the median of the merged array

        --> complexity ? # O(n.log(n))
        """

        nums = nums1 + nums2  # O(n)
        nums = sorted(nums)  # O(n.log(n)) (timsort)
        middle = len(nums) // 2  # O(1)
        if len(nums) % 2:  # odd
            median = nums[middle]  # O(1)
        else:  # even
            median = (nums[middle - 1] + nums[middle]) / 2.0  # O(1)
        return median
