class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        requires:
            coin is not null
            coins are positive
            amount is not negative
            amount > min(coin)
        ensures:
            res <= (amount // min(coin)) + 1
        algo:
            y = fewest number of coins needed to make up target amount
            f(amount) = 1 for each coin in coins
            f(0) = 0
        '''

        # edge cases
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1

        # general case

        amts = {coin:1 for coin in coins}
        while len(amts) > 0:
            new_amts = {}
            for amt in amts:
                for coin in reversed(coins):
                    new_amt = amt + coin
                    if new_amt > amount:
                        continue
                    elif new_amt == amount:
                        return amts[amt] + 1
                    elif new_amt not in amts:
                        new_amts[new_amt] = amts[amt] + 1
            amts = new_amts

        return -1