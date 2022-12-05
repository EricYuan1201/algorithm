#2 300.最长递增子序列，674. 最长连续递增序列，718. 最长重复子数组

##2 300.最长递增子序列

https://leetcode.cn/problems/longest-increasing-subsequence/

之前竟然写过，复习一遍。

```java
public int lengthOfLIS(int[] nums) {
   //dp[i]（是一个值，一个int值）：当到第i个元素的时候，最长的自增子序列的长度
    //最后发现是我的定义错误
    //真正的定义应该是：以第i个元素结尾，最长的自增子序列。
    int[] dp = new int[nums.length];
    if (nums.length > 0) dp[0] = 1;
    int max = 1;
    for (int i = 0; i < nums.length; i++) {
        dp[i] = 1;
        for (int j = 0; j < i; j++) {
            //核心是从第j个元素的最长递增子序列 取一个最大值。
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[j] + 1, dp[i]);
            } else {
                //真正走一遍代码之后发现了其中的错误的地方，比如 4, 10 ,4, 8
//                    dp[i] = Math.max(dp[j], dp[i]);
            }
        }
        max = Math.max(max, dp[i]);
    }
    return max;
}

```
##674. 最长连续递增序列

https://leetcode.cn/problems/longest-continuous-increasing-subsequence/
之前写过，经典题

```java
public int findLengthOfLCIS(int[] nums) {
//dp[i]以第i个元素结尾最长的连续自增子序列。
    int[] dp = new int[nums.length];
    if (nums.length == 0) return 0;
    if (nums.length == 1) return 1;
    dp[0] = 1;
    int max = 0;
    for (int i = 1; i < nums.length; i++) {
        dp[i] = 1;
        if (nums[i] > nums[i - 1]) {
            dp[i] = dp[i - 1] + 1;
        }
        max = Math.max(dp[i], max);
    }
    return max;
}

```
##718. 最长重复子数组

https://leetcode.cn/problems/maximum-length-of-repeated-subarray/

之前竟然写过

```java
public int findLength(int[] nums1, int[] nums2) {
    //需要多重遍历
    //
//        int length1 = nums1.length;
//        int length2 = nums2.length;
//        //对多的遍历，还是对少的遍历。
//        int maxLength = Math.max(length1, length2);
//        //dp[i]代表以i结尾的时候，最长的子数组的长度
//        int[] dp = new int[maxLength];
//        for (int i = 0; i < maxLength; i++) {
//
//        }
    //dp[i][j]以i结尾的nums1和以j结尾的nums[2]的最长子数组的长度。
          int[][] dp = new int[nums1.length][nums2.length];
    if (nums1.length == 0 || nums2.length == 0) return 0;
    if (nums1[0] == nums2[0]) {
        dp[0][0] = 1;
    } else {
        dp[0][0] = 0;
    }
    int max = dp[0][0];
    for (int i = 0; i < nums1.length; i++) {
        //固定i，遍历j。
        //这个好复杂啊！！！
        //nums1[i] = 2，开始遍历【3，2，1】
        for (int j = 0; j < nums2.length; j++) {
            //这个时候需要找核心了。
            if (nums1[i] == nums2[j]) {
                if (i < 1 || j < 1) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
            }
            max = Math.max(max, dp[i][j]);
        }
    }
    return max;
}

```
