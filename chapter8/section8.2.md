#2 122.买卖股票的最佳时机II，55. 跳跃游戏，45.跳跃游戏II

##2 122.买卖股票的最佳时机II

贪心算法，把每一次利益都吃到手。

```java
public static int maxProfit(int[] prices) {
    if (prices.length == 0) {
        return 0;
    }
    int sum = 0;
    for (int i = 1; i < prices.length; i++) {
        if (prices[i] - prices[i-1] > 0) {
            sum += (prices[i] - prices[i-1]);
        }
    }
    return sum;
}

```
##55. 跳跃游戏



```java
/**
 * 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
 *
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 *
 * 判断你是否能够到达最后一个下标。
 *
 * 这道题理解了倒还好，我在理解边缘卡了n久
 */
public boolean canJump(int[] nums) {
    if (nums.length == 0) {
        return false;
    }
    int cover = 0;
    for (int i = 0; i <= cover; i++) { //一定要注意这个cover，表示当前能够覆盖的最大位置
        cover = Math.max(i + nums[i], cover);
        if (cover >= nums.length -1) {
            return true;
        }
    }
    return false;
}

```
##45.跳跃游戏II

还是利用了贪心，每次走到最大值的时候，才进行跳跃。

```java
/**
 * 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
 * <p>
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 * <p>
 * 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
 * <p>
 * 假设你总是可以到达数组的最后一个位置。
 */
public int jump(int[] nums) {
    // 记录当前能跳跃到的位置的边界下标
    int border = 0;
    // 记录在边界范围内，能跳跃的最远位置的下标
    int cover = 0;
    // 记录所用步数
    int steps = 0;
    for (int i = 0; i < nums.length - 1; i++) {
        // 继续往下遍历，统计边界范围内，哪一格能跳得更远，每走一步就更新一次能跳跃的最远位置下标
        // 其实就是在统计下一步的最优情况
        cover = Math.max(cover, nums[i] + i);
        if (cover >= nums.length - 1) {
            return steps + 1;
        }
        // 如果到达了边界，那么一定要跳了，下一跳的边界下标就是之前统计的最优情况maxPosition，并且步数加1
        if (i == border) {
            border = cover;
            steps++;
        }
    }
    return steps;
}

```
