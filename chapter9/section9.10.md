#49 121. 买卖股票的最佳时机，122.买卖股票的最佳时机II

##121. 买卖股票的最佳时机

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
参考文档：
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solution/si-wei-dao-tu-zheng-li-gu-piao-wen-ti-da-9jir/

```java
public int maxProfit(int[] prices) {
    int[] dp = new int[prices.length];
    dp[0]=0;
    int minprice=prices[0];//minprice代表历史最低价格，
    // 所以i从1开始历史最低价格肯定是prices[0]
    for (int i = 1; i < prices.length; i++) {
        dp[i]=Math.max(dp[i-1],prices[i]-minprice);
        minprice=Math.min(minprice,prices[i]);

    }
    return dp[prices.length-1];
}

```
##122.买卖股票的最佳时机II

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

```java
public static int maxProfit(int[] prices) {
    if (prices.length == 0) {
        return 0;
    }
    int sum = 0;
    for (int i = 1; i < prices.length; i++) {
        if (prices[i] - prices[i-1] > 0) {
            sum += (prices[i] - prices[i-1]);
        }
    }
    return sum;
}

```
