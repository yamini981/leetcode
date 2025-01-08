class Solution {
    public int getSum(int a, int b) {
        // xor is like adding without carry
        // to find the carry, and both integers together and shift to the left by 1
        // then repeat by adding your result to the carry until no more carry bits
        int carry = b;
        int result = a;
        while (carry != 0) {
            int temp = (carry & result) << 1;
            result ^= carry;
            carry = temp;
        }

        return result;
    }
}