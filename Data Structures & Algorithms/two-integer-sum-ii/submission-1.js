class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        const n = numbers.length;
        let map = new Map();

        for (let i =0; i<n ; i++){
            let currentNum = numbers[i];
            let diff = target - numbers[i];
            if (map.has(diff)){
                return [map.get(diff), i + 1]
            }

            map.set(numbers[i] , i + 1);
        }
        return [];
    }
}
