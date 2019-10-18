direction = [
    (-1, 0),
    (0, -1)
]


class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        """
        :type n: int row
        :type m: int col
        :rtype: int
        """

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[0][0]:
            return 0

        if n == 1 and 1 not in obstacleGrid[0]:
            return 1
        if m == 1 and n != 1:
            firstCol = [x[0] for x in obstacleGrid]
            if 1 not in firstCol:
                return 1
            else:
                return 0

        dp = [[0 for i in range(m)] for _ in range(n)]
        dp[0][0] = 1

        for j in range(m):
            for i in range(n):
                if obstacleGrid[i][j]:
                    continue

                for delta_x, delta_y in direction:
                    x, y = i + delta_x, j + delta_y
                    if obstacleGrid[x][y]:
                        continue
                    dp[i][j] += dp[x][y]

        return dp[n - 1][m - 1]
