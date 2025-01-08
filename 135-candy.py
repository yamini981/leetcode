class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sliding window...?
        candy = [1] * len(ratings)
        if len(ratings) == 1:
            return 1
        if ratings[0] > ratings[1]:
            candy[0] = 2

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candy[j] = max(candy[j + 1] + 1, candy[j])
        
        return sum(candy)
