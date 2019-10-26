class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for curr,value in enumerate(nums):

            for prev in range(curr):
                if nums[prev] < value:
                    dp[curr] = max(dp[curr],dp[prev]+1)

        return max(dp)

if __name__ == '__main__':
    S = Solution().longestIncreasingSubsequence([4,2,4,5,3,7])
