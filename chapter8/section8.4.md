#4 135. 分发糖果，1005.K次取反后最大化的数组和，134. 加油站

##4 135. 分发糖果

左规则，右规则

```java
public static int candy(int[] ratings) {
    int n = ratings.length;
    int[] left = new int[n];
    left[0] = 1;
    for (int i = 1; i < n; i++) {
        if (ratings[i] > ratings[i - 1]) {
            left[i] = left[i - 1] + 1;
        } else {
            left[i] = 1;
        }
    }
    int res = 0;
    int[] right = new int[n];
    for (int i = n - 1; i >= 0; i--) {
        if (i < n - 1 && ratings[i] > ratings[i + 1]) {
            right[i] = right[i + 1] + 1;
        } else {
            right[i] = 1;
        }
        res += Math.max(left[i], right[i]);
    }
    return res;
//        int right = 0, ret = 0;
//        for (int i = n - 1; i >= 0; i--) {
//            if (i < n - 1 && ratings[i] > ratings[i + 1]) {
//                right++;
//            } else {
//                right = 1;
//            }
//            ret += Math.max(left[i], right);
//        }
//        return ret;
}

```
##1005.K次取反后最大化的数组和

很考验数学知识

```java
/**
 * 有一点点思路，贪心算法，只看负数
 */
public int largestSumAfterKNegations(int[] nums, int k) {
    if (nums.length == 0) {
        return 0;
    }
    Arrays.sort(nums);
    int sum = 0;
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] < 0 && k > 0) {
            nums[i] = -nums[i];
            k--;
        }
        sum += nums[i];
    }
    Arrays.sort(nums);
    return sum + (k % 2) == 0 ? 0 : -nums[0];
}

```
##134. 加油站



```java


```
