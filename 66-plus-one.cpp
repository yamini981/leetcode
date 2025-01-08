class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        digits[digits.size() - 1] += 1;
        if (digits[digits.size() - 1] != 10) {
            return digits;
        }
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (i-1 == -1) {
                if (digits[i] == 10) {
                    digits.insert(digits.begin(), 1);
                    digits[i+1] = 0;

                }
            }
            else if (digits[i] == 10) {
                
                digits[i] = 0;
                digits[i-1] += 1;
            }
            else {
                break;
            }
        }
        return digits;
    }
};