class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        singleDigit = set()
        # 1-9
        for i in range(1, 10):
            singleDigit.add(str(i))

        twoDigits = set()
        # 10-26
        for j in range(10, 27):
            twoDigits.add(str(j))

        if not s or int(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        dp = [0] * (len(s))
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] in singleDigit:
                # 先检查当前位置，如果在1位set里，延续dp[i-1]
                dp[i] += dp[i - 1]
                # 不能continue
            if s[i - 1] + s[i] in twoDigits:
                # 如果
                if i == 1:
                    dp[i] += 1
                # 继续检查如果前两位在2位set里，在dp[i-1]基础上继续加上dp[i-2]
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]

if __name__ == '__main__':
    S = Solution().numDecodings("456")
    print(S)