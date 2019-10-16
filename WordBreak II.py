class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        # partitions initilization
        partitions = []

        # for loop 1-len(s)
        for i in range(1, len(s)):
            # check 前缀
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            # sub_partition = dfs后缀
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            # 循环sub_partition 检查是否在dict里，如果在加入进partitions
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)

        # 如果 s 在 dict， partitions加入s本身
        if s in wordDict:
            partitions.append(s)
        # 记忆化
        memo[s] = partitions

        # 返回
        return partitions


if __name__ == '__main__':
    a = "lintcode"
    b = ["de", "ding", "co", "code", "lint"]
    S = Solution().wordBreak(a, b)
    print(S)
