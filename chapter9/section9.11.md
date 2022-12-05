#0 123.买卖股票的最佳时机III，188.买卖股票的最佳时机IV

##0 123.买卖股票的最佳时机III

https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-iii-by-wrnt/

完全写不来。

```java
public int maxProfit(int[] prices) {
    int n = prices.length;
    int buy1 = -prices[0], sell1 = 0;
    int buy2 = -prices[0], sell2 = 0;
    for (int i = 1; i < n; ++i) {
        buy1 = Math.max(buy1, -prices[i]);
        sell1 = Math.max(sell1, buy1 + prices[i]);
        buy2 = Math.max(buy2, sell1 - prices[i]);
        sell2 = Math.max(sell2, buy2 + prices[i]);
    }
    return sell2;
}

```
##188.买卖股票的最佳时机IV

写不来，看一下吧。

```java


```
