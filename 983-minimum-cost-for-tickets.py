class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayPrice = costs[0]
        weekPrice = costs[1]
        monthPrice = costs[2]
        dayIndex = 0

        dp = [0] * (days[-1] + 1)
        for i in range(1, days[-1] + 1):
            if i != days[dayIndex]:
                dp[i] = dp[i - 1]
            else:
                dayIndex += 1
                if i - 1 >= 0:
                    minDayPrice = dp[i - 1] + dayPrice
                else:
                    minDayPrice = dayPrice
                if i - 7 >= 0:
                    minWeekPrice = dp[i - 7] + weekPrice
                else:
                    minWeekPrice = weekPrice
                if i - 30 >= 0:
                    minMonthPrice = dp[i - 30] + monthPrice
                else:
                    minMonthPrice = monthPrice

                dp[i] = min(minDayPrice, minWeekPrice, minMonthPrice)
        
        return dp[i]
