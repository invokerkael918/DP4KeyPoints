class SolutionBFS:
    """
    Time exceed on lintcode
    Passed on Leetcode
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = [s]
        already_seen = set()

        while len(q) > 0:
            curr_s = q.pop(0)

            if curr_s not in already_seen:
                already_seen.add(curr_s)
                if curr_s == '':
                    return True
                for w in wordDict:
                    if curr_s.startswith(w):
                        q.append(curr_s[len(w):])
        return False

class Solution2:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here

        if len(dict) == 0:
            return len(s) == 0
        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        maxLength = max([len(w) for w in dict])
        for i in range(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):

                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break
        return f[n]


if __name__ == '__main__':
    S = Solution().wordBreak("lintcode", ["lint", "code"])
    print(S)
