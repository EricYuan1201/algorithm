#1 01背包问题，416. 分割等和子集

##1 01背包问题



```java


```
##416. 分割等和子集

之前竟然写过。

```java
public boolean canPartition(int[] nums) {
    int sum = 0;
    for (int i = 0; i < nums.length; i++) {
        sum += nums[i];
    }
    if (sum % 2 != 0) return false;
    int target = sum / 2;
    //下面就变成背包问题了，有nums个元素，只能选特定的，然后组成halfSum，如果能组成，就算成功了。
    //这和背包也没啥关系啊。
    //每一个元素都有两种结果，选和不选。如果超过half了肯定不行，直接break了。
    //如果小于half的话呢？
    //定义第i个元素选和不选的值，列只有0和1。
    //核心点就在于第i个元素选和不选。
    //这个本质是01背包问题。
    //背包三要素：1.多个物品，2.构成体积，3.最大价值。
//        int[][] dp = new int[nums.length][2];
//        dp[0][0] = 0;
//        dp[0][1] = nums[0];
//        for (int i = 0; i < nums.length; i++) {
//            for (int j = 0; j < 2; j++) {
//                if (j == 0) {
//                    dp[i][j] = dp[i-1][]
//                }
//            }
//        }
    int[] dp = new int[target + 1];
    //dp的定义：体积为i的时候，构成的最大价值。
    //其实这里是多个一维数组。
    //
    for (int i = 0; i < nums.length; i++) {
        for (int j = target; j >= nums[i] ; j--) {
            dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i]);
        }
    }
    return dp[target] == target;
}

```
