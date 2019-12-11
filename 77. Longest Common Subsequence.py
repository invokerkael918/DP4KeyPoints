class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        # write your code here
        """
        dp[i][j]: A[i] 到 B[j] 有多少个一样的
                  如果最后两个一样: if     A[i]=B[j], dp[i][j] = dp[i-1][j-1]+=1
        如果B最后一个和A砍掉尾巴一样：if A[i-1] = B[j], dp[i][j] = dp[i-1][j]
        如果A最后一个和B砍掉尾巴一样：if A[i] = B[j-1], dp[i][j] = dp[i][j-1]

        转移方程： dp[i][j] = max{dp[i-1][j],dp[i][j-1], dp[i-1][j-1]+=1 if A[i]=B[j]}
        """
        n, m = len(A), len(B)
        dp = [[0 for _ in range(n + 2)] for _ in range(m + 2)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                self.printMatrix(dp)
                print("")
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                self.printMatrix(dp)
                print("")
        return dp[n][m]

    def printMatrix(self, matrix):
        for row in matrix:
            print(row)


if __name__ == '__main__':
    S = Solution().longestCommonSubsequence("jiuzhang", "lijiang")
