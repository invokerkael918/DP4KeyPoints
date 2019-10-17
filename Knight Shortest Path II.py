import sys

direction = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1)
]


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])

        dp = [[sys.maxsize for j in range(m)] for _ in range(n)]
        dp[0][0] = 0
        for j in range(m):
            for i in range(n):
                if grid[i][j]:
                    continue
                for delta_x, delta_y in direction:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)
        if dp[n - 1][m - 1] == sys.maxsize:
            return -1

        return dp[n - 1][m - 1]


if __name__ == '__main__':
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    S = Solution().shortestPath2(grid)
    print(S)
