class Solution {
    public int maxProfit(int[] prices) {
        int purchasePrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < purchasePrice) {
                purchasePrice = price;
            } else if (price - purchasePrice > maxProfit){
                maxProfit = price - purchasePrice;
            }
        }

        return maxProfit;
    }
}
