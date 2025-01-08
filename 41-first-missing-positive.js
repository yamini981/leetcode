/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {

    var setNums = new Set();

    for (let i = 0; i < nums.length; i++)
    {
        setNums.add(nums[i]);
    }

    for (let i = 1; i <= nums.length; i++)
    {
        if (!setNums.has(i))
        {
            return(i);
        }
    }
    return nums.length + 1;




};