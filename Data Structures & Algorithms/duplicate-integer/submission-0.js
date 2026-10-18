class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        nums.sort();
        const seen = new Set();

        for(let i=0; i< nums.length;i++){
            if (seen.has(nums[i])) {
                // We've encountered this before!
                return true;
            }
            seen.add(nums[i]);
        }
        return false;
    }
}
