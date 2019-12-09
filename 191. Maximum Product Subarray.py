class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # write your code here

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        res = 0
        res = max(res, nums[0])
        maxf = [0] * n
        minf = [0] * n
        maxf[0] = nums[0]
        minf[0] = nums[0]

        for i in range(1, n):
            if nums[i] > 0:
                maxf[i] = max(maxf[i - 1] * nums[i], nums[i])
                minf[i] = min(minf[i - 1] * nums[i], nums[i])
            elif nums[i] < 0:
                maxf[i] = max(minf[i - 1] * nums[i], nums[i])
                minf[i] = min(maxf[i - 1] * nums[i], nums[i])
            res = max(res, maxf[i])
        return res