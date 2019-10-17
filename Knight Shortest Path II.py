import sys
from collections import deque

direction = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1)
]
directionBFS = [
    (1, 2),
    (-1, 2),
    (2, 1),
    (-2, 1)
]


# 取相反数是因为要看从哪个点来

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

        dp = [[100 for j in range(m)] for _ in range(n)]
        dp[0][0] = 0
        for j in range(m):
            for i in range(n):
                if grid[i][j]:
                    continue
                for delta_x, delta_y in direction:

                    x, y = i + delta_x, j + delta_y
                    print(x, y)
                    # 在 x,y 到 区间范围内，之前找了很多 0 0 的前记节点，但是他们不存在棋盘内
                    # DP是在找从哪个点到当前点的最短路径，逆向求得最短路径
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)
                        self.printBoard(dp)
                        print("")
        if dp[n - 1][m - 1] == sys.maxsize:
            return -1

        return dp[n - 1][m - 1]

    def printBoard(self, dp):
        for ele in dp:
            print(ele)


if __name__ == '__main__':
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    S = Solution().shortestPath2(grid)
    print(S)


class SolutionBFS:

    def shortestPath2(self, grid):
        if not grid or grid[-1][-1] == 1:
            return -1

        queue = deque([(0, 0)])
        n, m = len(grid), len(grid[0])

        count = 0

        while queue:
            count += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for delta_x, delta_y in directionBFS:
                    next_x, next_y = x + delta_x, y + delta_y
                    if next_x == n - 1 and next_y == m - 1:
                        return count
                    if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] != 1:
                        grid[next_x][next_y] = 1
                        # 标记为访问过
                        queue.append((next_x, next_y))

        return -1


if __name__ == '__main__':
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    S = SolutionBFS().shortestPath2(grid)
    print(S)
