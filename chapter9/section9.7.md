#5 70. 爬楼梯，322. 零钱兑换，279.完全平方数

##5 70. 爬楼梯

就是斐波那契数列

```java
 public int climbStairs(int n) {
    int[] dp = new int[n + 1];
    dp[0] = 1;
    dp[1] = 1;
    for(int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
 return dp[n];

```
##322. 零钱兑换

总感觉这道题做过...

```java
//给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
//
//计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
//
//你可以认为每种硬币的数量是无限的。
//
//链接：https://leetcode.cn/problems/coin-change
public static int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}

```
##279.完全平方数

动态规划，for循环，也算是一个模板部分。

模板 + 数学思维。

```java
//给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
//
//完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
//https://leetcode.cn/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode-solut-t99c/
/**
 * 有时候看题解，如此精妙。
 */
public int numSquares(int n) {
    int[] dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;
    //第一步，模板代码。
    for (int i = 1; i <= n; i++) {
        int minn = Integer.MAX_VALUE;
        //第2步，利用了for循环
        //恰好的利用了之前的值都计算过
        for (int j = 1; j * j <= i; j++) {
            minn = Math.min(minn, dp[i - j * j]);
        }
        dp[i] = minn + 1;
    }
    return dp[n];
}

```
