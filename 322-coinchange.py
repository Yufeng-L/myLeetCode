class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #要用动态规划去做
        if not coins:
            return -1
        if amount == 0:
            return 0
        dp = (amount + 1) * [-1]
        dp[0] = 0
        for i in range(1,amount + 1):
            res = []
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    res.append(dp[i-coin] + 1)
                if res != []:
                    dp[i] = min(res)
        return dp[-1]

        #贪心算法？在此题有很多case不会过-。-
        # #Amount也有可能为0的状态 返回0
        # if amount == 0:
        #     return 0
        # # 记得要Sorted
        # coins = sorted(coins)
        # count = 0
        # #last one to first one
        # for i in range(len(coins) - 1,-1,-1):
        #     while(amount >= coins[i]):
        #         amount = amount - coins[i]
        #         count += 1
        #         if amount == 0:
        #             return count
        # return -1