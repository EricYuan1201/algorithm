#3 1143.最长公共子序列，1035.不相交的线，53. 最大子序和

##3 1143.最长公共子序列

https://leetcode.cn/problems/longest-common-subsequence/solution/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/

经典题，甚至达到熟读背诵的情况

```java
public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length(), n = text2.length();
    int[][] dp = new int[m + 1][n + 1];
    //初始化dp[0][] 和dp[][0]为0，因为当一个字符串长度为0时，那么他们的LCS长度也为0
    Arrays.fill(dp[0], 0);
    for(int i = 0; i <= m; i++){
        dp[i][0] = 0;
    }

    for(int i = 1; i <= m; i++){
        for(int j = 1; j <= n; j++){
            if (text1.charAt(i - 1) == text2.charAt(j - 1)){
                 //该字符可以加入LCS
                 dp[i][j] = 1 + dp[i - 1][j - 1];
            } else{
               //该位置的字符不相等，至少有一个不能加入LCS，先选择当前局部最优解，即选择前面的较大值
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[m][n];
}

```
##1035.不相交的线

https://leetcode.cn/problems/uncrossed-lines/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-bkaas/
参考了题解。

```java

public int maxUncrossedLines(int[] s1, int[] s2) {
    int n = s1.length, m = s2.length;
    int[][] f = new int[n + 1][m + 1];
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            f[i][j] = Math.max(f[i - 1][j], f[i][j - 1]);
            if (s1[i - 1] == s2[j - 1]) {
                f[i][j] = Math.max(f[i][j], f[i - 1][j - 1] + 1);
            }
        }
    }
    return f[n][m];
}

```
##53. 最大子序和

之前竟然写过！！
https://leetcode.cn/problems/maximum-subarray/

```java
public int maxSubArray(int[] nums) {
    if (nums.length == 0) {
        return 0;
    }
    int maxSum = nums[0];
    int curSum = nums[0];
    for (int i = 1; i <= nums.length - 1; i++) {
        if (curSum > 0) {
            curSum += nums[i];
        } else {
            curSum = nums[i];
        }
        maxSum = Math.max(maxSum, curSum);
    }
    return maxSum;
}

```
