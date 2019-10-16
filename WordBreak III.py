class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak3(self, s, dict):
        # write your code here

        if not s or not dict:
            return 0
        n = len(s)
        dict = [x.lower() for x in dict]
        s = s.lower()

        f = [0] * (n + 1)
        f[0] = 1

        maxLength = max([len(w) for w in dict])
        for i in range(n + 1):
            for j in range(1, min(i, maxLength) + 1):

                if f[i - j] == 0:
                    continue
                if s[i - j:i] in dict:
                    f[i] += f[i - j]

        return f[-1]
