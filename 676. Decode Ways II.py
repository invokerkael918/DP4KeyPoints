class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """

    def numDecodings(self, s):
        # write your code here
        mod = 1000000007
        n = len(s)
        f = [0] * (n + 1)

        f[0] = 1

        for i in range(1, n + 1):
            f[i] = f[i - 1] * self.count1(s[i - 1])
            if (i > 1):
                f[i] += f[i - 2] * self.count2(s[i - 2], s[i - 1])
            f[i] = f[i] % mod
        return int(f[n])

    def count1(self, c):
        if c == '0':
            return 0
        if c != '*':
            return 1
        return 9

    def count2(self, c2, c1):
        if (c2 == '0'):
            return 0
        if (c2 == '1'):
            if c1 == "*":
                return 9  # 11-19
            return 1

        if c2 == "2":
            if c1 == "*":
                return 6  # 21-26

            if c1 <= "6":
                return 1

            else:
                return 0
        if c2 >= "3" and c2 <= "9":
            return 0

        # c2 = *
        if c1 >= "0" and c1 <= '6':
            # 10 20
            return 2
        if c1 >= "7" and c1 <= "9":
            return 1

        return 15
