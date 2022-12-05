#8 198.打家劫舍，213.打家劫舍II， 337.打家劫舍III

##8 198.打家劫舍

之前做过，复习一下

```java
public int rob(int[] nums) {
    //dp[i]代表抢到第i家的时候能抢到的最多的钱。
    int[] dp = new int[nums.length];
    dp[0] = nums[0];
    if (nums.length >= 2) dp[1] = Math.max(nums[0], nums[1]);
    for (int i = 2; i < nums.length; i++) {
        dp[i] = Math.max((dp[i - 2] + nums[i]), dp[i - 1]);
    }
    return dp[nums.length - 1];
}

```
##213.打家劫舍II

虽然只是一个变种，感觉麻烦了很多。

```java
public int rob(int[] nums) {
    int length = nums.length;
    if (length == 1) {
        return nums[0];
    } else if (length == 2) {
        return Math.max(nums[0], nums[1]);
    }
    return Math.max(robRange(nums, 0, length - 2), robRange(nums, 1, length - 1));
}

public int robRange(int[] nums, int start, int end) {
    int first = nums[start], second = Math.max(nums[start], nums[start + 1]);
    for (int i = start + 2; i <= end; i++) {
        int temp = second;
        second = Math.max(first + nums[i], second);
        first = temp;
    }
    return second;
}

```
##337.打家劫舍III

看不出来

```java


```
