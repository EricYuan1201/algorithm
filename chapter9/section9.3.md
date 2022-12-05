#1 343. 整数拆分，96.不同的二叉搜索树

##1 343. 整数拆分

https://leetcode.cn/problems/integer-break/

```java
public int integerBreak(int n) {
    int[] dp = new int[n + 1];
    if (n >= 0) dp[0] = 0;
    if (n >= 1) dp[1] = 1;
    if (n >= 2) dp[2] = 1;
    for (int i = 3; i <= n; i++) {
        int curMax = 0;
        for (int j = 0; j <= i; j++) {
            //和谁比较呢？
            //
            curMax = Math.max(curMax, Math.max(dp[i - j], (i - j)) * j);
        }
        dp[i] = curMax;
    }
    return dp[n];
}

```
##96.不同的二叉搜索树

之前竟然写过

```java
public int numTrees(int n) {
    //定义二叉搜索树的节点。从1到n
    //二叉搜索树，中序遍历是一个递增序列。
    int[] dp = new int[n + 1];
    if (n >= 0) dp[0] = 1;
    if (n >= 1) dp[1] = 1;
    if (n >= 2) dp[2] = 2;
    for (int i = 3; i <= n ; i++) {
        //现在最关键的是递推关系，想不出来了，包括上面那道题也是，想不出来递推关系。
        //难的动态规划都是想不出来递推公式。
        for (int j = 0; j < i; j++) {
            dp[i] += (dp[j] * dp[i-j-1]);
        }
    }
    return dp[n];
}

```
