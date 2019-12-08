class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dpInc = [0] * n
        dpDec = [0] * n
        dpInc[0] = 1
        dpDec[0] = 1
        for i in range(1, n):
            if A[i] > A[i - 1]:
                dpInc[i] = dpInc[i - 1] + 1
                dpDec[i] = 1
                continue
            if A[i] < A[i - 1]:
                dpDec[i] = dpDec[i - 1] + 1
                dpInc[i] = 1
                continue
            else:
                dpInc[i] = dpInc[i - 1]
                dpDec[i] = dpDec[i]

        return max(max(dpDec), max(dpInc))
