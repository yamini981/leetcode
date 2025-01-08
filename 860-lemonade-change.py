class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # array of bill count where 0 is $5, 1 is $10, 2 is $20
        # potential change - if they give 20, we need to give 10 and 5
        # or 5 and 5 and 5
        # if they give 5, give nothing
        # if they give 10, give 5

        heldBills = [0, 0] # no need to track 20's

        for bill in bills:
            if bill == 5:
                heldBills[0] += 1
            if bill == 10:
                heldBills[1] += 1

                if heldBills[0] > 0:
                    heldBills[0] -= 1
                else:
                    return False

            if bill == 20:
                if heldBills[1] > 0 and heldBills[0] > 0:
                    heldBills[1] -= 1
                    heldBills[0] -= 1
                elif heldBills[0] > 2:
                    heldBills[0] -= 3
                else:
                    return False

        return True