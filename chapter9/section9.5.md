#3 1049. 最后一块石头的重量 II，494. 目标和，474.一和零

##3 1049. 最后一块石头的重量 II



```java


```
##494. 目标和

之前竟然写过

```java
public int findTargetSumWays(int[] nums, int target) {
    if (nums.length == 1) {
        if (Math.abs(nums[0]) == Math.abs(target)) {
            return 1;
        } else {
            return 0;
        }
    }
    int sum = 0;
    for (int i = 0; i < nums.length; i++) {
        sum += nums[i];
    }

//        int[] dp = new int[nums.length];
//        //dp[i]的含义是，当i个元素的时候，能够组成的最大价值是多少。
//        for (int i = 0; i < nums.length; i++) {
//            //这一个题目对背包的理解需求非常之深，反正我是没想出来。
//            //但凡有一个点理解不了，就做不出来这道题目
//            int curMax = 0;
//            for (int j = sum; j > nums[i]; j--) {
//                int pTarget = dp[j]
//            }
//        }

    //就是构建2个组，left right，让left - right = target。
    //left + right = sum
    //left = (sum + target) / 2
    //如果  left % 2 == 1，则无解
    //于是就变成了背包问题。构建j组，一共有多少种解法。
    if ((sum + target) % 2 == 1) return 0;
    if (target > sum) return 0;
    int bagSize = (sum + target) / 2;
    int[] dp = new int[bagSize + 1];
    dp[0] = 1;
    for (int i = 0; i < nums.length; i++) {
        for (int j = bagSize; j >= nums[i]; j--) {
            //这一句的核心依然是第i个元素选与不选
            dp[j] += dp[j - nums[i]];
        }
    }
    return dp[bagSize];
}

```
##474.一和零

https://leetcode.cn/problems/ones-and-zeroes/solution/dong-tai-gui-hua-zhuan-huan-wei-0-1-bei-bao-wen-ti/

```java
public class Solution {

    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        dp[0][0] = 0;
        for (String s : strs) {
            int[] zeroAndOne = calcZeroAndOne(s);
            int zeros = zeroAndOne[0];
            int ones = zeroAndOne[1];
            for (int i = m; i >= zeros; i--) {
                for (int j = n; j >= ones; j--) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }

    private int[] calcZeroAndOne(String str) {
        int[] res = new int[2];
        for (char c : str.toCharArray()) {
            res[c - '0']++;
        }
        return res;
    }
}

```
