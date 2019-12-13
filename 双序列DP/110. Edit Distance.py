class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, s1, s2):
        # write your code here
        """
             r  o  s
        [  [0, 1, 2, 3],
         h [1, 1, 2, 3],
         o [2, 2, 1, 2],
         r [3, 2, 2, 2],
         s [4, 3, 3, 2],
         e [5, 4, 4, 3]  ]

        """
        n = len(s1)
        m = len(s2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:

                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[n][m]
