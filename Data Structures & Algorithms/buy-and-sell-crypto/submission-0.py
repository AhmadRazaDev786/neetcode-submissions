class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        l = 0
        r = 1
        while(r<len(prices)):
            if prices[r]>prices[l]:
                maxprof= max(maxprof, prices[r]-prices[l])
            else:
                l = r
            r+=1
        return maxprof