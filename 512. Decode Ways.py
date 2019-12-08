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
                dp[i] += dp[i - 1]

            if s[i - 1] + s[i] in twoDigits:

                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[-1]
