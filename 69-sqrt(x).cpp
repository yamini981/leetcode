class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        if (x == 1 || x == 2 || x == 3) return 1;
        if (x == 4 || x == 5) return 2;
        int currVal = 2;
        while (currVal < 46341) {
            if (currVal * currVal > x) {
                return currVal - 1;
            }
            currVal++;
        }
        return currVal - 1;
    }
};