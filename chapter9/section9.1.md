#8 509. 斐波那契数， 70. 爬楼梯，746. 使用最小花费爬楼梯

##8 509. 斐波那契数



```java


```
##70. 爬楼梯

斐波那契数列的变形？


```java
public int climbStairs(int n) {
    int[] arr = new int[n + 1];
    arr[0] = 1;
    arr[1] = 1;
    for (int i = 2; i < n + 1; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    return arr[n];
}

```
##746. 使用最小花费爬楼梯

之前写过了，都是从小到大的形式来写动态规划的

```java
    public int minCostClimbingStairs(int[] cost) {
      int n = cost.length;
      int pre = 0;
      int cur = 0;
      for (int i = 2; i < n + 1; i++) {
         int next = Math.min(pre + cost[i-2], cur + cost[i-1]);
         pre = cur;
         cur = next;
      }
      return cur;
    }

```
