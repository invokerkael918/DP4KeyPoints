class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, AA):
        """
        f[i][j]
        """
        n = len(AA)
        if n == 0:
            return 0

        A = [0] * (n + 2)
        A[0] = A[n + 1] = 1

        for i in range(1, n + 1):
            A[i] = AA[i - 1]
        n += 2
        # AA: 3 2 8 7 9
        # A: 1 3 2 8 7 9 1
        f = [[-1 for _ in range(n)] for _ in range(n)]
        # length = 2
        for i in range(n - 1):
            f[i][i + 1] = 0

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                f[i][j] = 0
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + A[i] * A[k] * A[j])
        #self.printMatrix(f)
        return f[0][n - 1]

    # def printMatrix(self, matrix):
    #     for row in matrix:
    #         print(row)