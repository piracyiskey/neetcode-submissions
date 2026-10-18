class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let max = 0;
        for (let i=0; i<prices.length;i++){
            for (let j=1; j<prices.length;j++){
                if (i < j && prices[j]-prices[i] > max){
                    max = prices[j]-prices[i];
                }
            }
        }

        return max;

        
    }
}
