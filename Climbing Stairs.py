class Solution:
    """
    @param n: An integer
    @return: An integer
    1.如果起始跳一阶的话，剩余的n-1阶就有 f(n-1) 种跳法；
    2.如果起始跳二阶的话，剩余的n-2阶就有 f(n-2) 种跳法；
    所以f(n) = f(n-1) + f(n-2)，实际结果即为斐波纳契数。
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        # if n == 2:
        #     return 2
        result = [1, 2]

        for _ in range(n - 2):
            result.append(result[-1] + result[-2])
        return result[-1]


if __name__ == '__main__':
    S = Solution().climbStairs(7)
    print(S)
