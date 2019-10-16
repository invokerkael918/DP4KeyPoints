class Solution1:
    """
    Without optimization by scroll array
    From BOT to TOP
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]

        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]

        for i in range(n - 2, -1, -1):
            # 从n-1到0，每次递减1
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j + 1], dp[i + 1][j]) + triangle[i][j]
        return dp[0][0]


class Solution2:
    """
    optimized by scroll array
    From BOT to TOP
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        # dp = [[0]*(i+1) for i in range(n)]
        dp = [[0] * n, [0] * n]

        for i in range(n):
            dp[(n - 1) % 2][i] = triangle[n - 1][i]

        for i in range(n - 2, -1, -1):
            # 从n-1到0，每次递减1
            for j in range(i + 1):
                dp[i % 2][j] = min(dp[(i + 1) % 2][j + 1], dp[(i + 1) % 2][j]) + triangle[i][j]

        return dp[0][0]


class Solution3:
    """
    Without optimization by scroll array
    From TOP to BOT
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        if n == 1:
            return dp[0][0]

        for i in range(n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        for i in range(2, n):
            # 从 2 到 n 每次递增
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[n - 1])


class Solution4:
    """
    With optimization by scroll array
    From TOP to BOT
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here

        n = len(triangle)

        dp = [[0] * n, [0] * n]

        dp[0][0] = triangle[0][0]
        # if n == 1:
        #     return dp[0][0]

        for i in range(1, n):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
            dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]
            for j in range(1, i):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[(i - 1) % 2][j]) + triangle[i][j]

        return min(dp[(n - 1) % 2])


if __name__ == '__main__':
    a = [[-10]]
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    S = Solution4().minimumTotal(a)
    print(S)
