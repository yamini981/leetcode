class Solution:
    def intToRoman(self, num: int) -> str:
        ones = num % 10
        tens = ((num - ones) % 100) // 10
        hundreds = ((num - ones - tens) % 1000) // 100
        thousands = (num - hundreds - ones - tens) // 1000
        
        ret = ""

        for _ in range(thousands):
            ret += "M"

        if hundreds == 4:
            ret += "CD"
        elif hundreds == 9:
            ret += "CM"
        else:
            if hundreds >= 5:
                ret += "D"
                hundreds -= 5
            for _ in range(hundreds):
                ret += "C"
        
        if tens == 4:
            ret += "XL"
        elif tens == 9:
            ret += "XC"
        else:
            if tens >= 5:
                ret += "L"
                tens -= 5
            for _ in range(tens):
                ret += "X"

        if ones == 9:
            ret += "IX"
        elif ones == 4:
            ret += "IV"
        else:
            if ones >= 5:
                ret += "V"
                ones -= 5
            for _ in range(ones):
                ret += "I"
        

        return ret

        

        