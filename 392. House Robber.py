class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]

        dp = [0] * n
        dp[0] = A[0]
        dp[1] = max(A[1], A[0])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], A[i] + dp[i - 2])

        return dp[-1]