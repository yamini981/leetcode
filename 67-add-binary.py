class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aPtr = len(a) - 1
        bPtr = len(b) - 1
        carry = False
        ret = ""

        # 1010  11011
        while aPtr != -1 and bPtr != -1:
            currA = a[aPtr]
            currB = b[bPtr]
            if carry:
                if currA == '1' and currB == '1':
                    carry = True
                    ret = "1" + ret
                elif (currA == '1' and currB == '0') or (currB == '1' and currA == '0'):
                    carry = True
                    ret = "0" + ret
                else:
                    ret = "1" + ret
                    carry = False
            else:
                if currA == '1' and currB == '1':
                    carry = True
                    ret = "0" + ret
                elif (currA == '1' and currB == '0') or (currB == '1' and currA == '0'):
                    ret = "1" + ret
                else:
                    ret = "0" + ret

            aPtr -= 1
            bPtr -= 1

        while bPtr != -1:
            currB = b[bPtr]
            if carry:
                if currB == '1':
                    carry = True
                    ret = "0" + ret
                else:
                    ret = "1" + ret
                    carry = False
            else:
                if currB == '1':
                    ret = "1" + ret
                else:
                    ret = "0" + ret
            bPtr -= 1

        while aPtr != -1:
            currA = a[aPtr]
            if carry:
                if currA == '1':
                    carry = True
                    ret = "0" + ret
                else:
                    ret = "1" + ret
                    carry = False
            else:
                if currA == '1':
                    ret = "1" + ret
                else:
                    ret = "0" + ret

            aPtr -= 1

        if carry:
            ret = "1" + ret

        return ret
