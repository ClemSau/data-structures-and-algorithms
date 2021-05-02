# 1672. Richerst customer wealth 

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer_accounts in accounts:
            if sum(customer_accounts) > max_wealth:
                max_wealth = sum(customer_accounts)
        return max_wealth
        