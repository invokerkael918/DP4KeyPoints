import sys

direction = [
    (-1, -2),
    (1, -2),
    (-2, -1),
    (2, -1)
]
#取相反数是因为要看从哪个点来

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
                    print(x,y)
                    # 在 x,y 到 区间范围内，之前找了很多 0 0 的前记节点，但是他们不存在棋盘内
                    # DP是在找从哪个点到当前点的最短路径，逆向求得最短路径
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)
                        self.printBoard(dp)
                        print("")
        if dp[n - 1][m - 1] == sys.maxsize:
            return -1

        return dp[n - 1][m - 1]

    def printBoard(self,dp):
        for ele in dp:
            print(ele)



if __name__ == '__main__':
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    S = Solution().shortestPath2(grid)
    print(S)
