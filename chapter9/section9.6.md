#4 完全背包，518. 零钱兑换 II，377. 组合总和 Ⅳ

##4 完全背包



```java


```
##518. 零钱兑换 II

之前竟然看过。

```java
public int change(int amount, int[] coins) {
    //完全背包问题了。
    int[] dp = new int[amount + 1];
    dp[0] = 1;
    for (int i = 0; i < coins.length; i++) {
        for (int j = coins[i]; j <= amount; j++) {
            //核心是第i个元素到底选还是不选
            //然后一维数组比二维数组更加抽象
            //这个还是组合
            //每一道题都异常经典，简直不能错过每一道题
            dp[j] +=  dp[j - coins[i]];
        }
    }
    return dp[amount];
}

```
##377. 组合总和 Ⅳ

之前竟然看过

```java
public int combinationSum4(int[] nums, int target) {
    int[] dp = new int[target + 1];
    dp[0] = 1;
    for (int i = 0; i <= target; i++) {
        for (int j = 0; j < nums.length; j++) {
            if (i >= nums[j]) {
                dp[i] += dp[i - nums[j]];
            }
        }
    }
    return dp[target];
}

```
