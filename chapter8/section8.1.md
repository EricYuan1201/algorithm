#1 53. 最大子序和，455.分发饼干，376. 摆动序列

##1 53. 最大子序和

maxSum, curSum

无后向行，不过那个判断条件挺有意思的。

```java
/**
 * 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
 * <p>
 * 子数组 是数组中的一个连续部分。
 */
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
##455.分发饼干



```java
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int count = 0;//满足小孩的计数

        //从数组最大值开始遍历
        for(int i = g.length-1,j = s.length-1; i >= 0 && j >= 0;){
            //饼干大于小孩胃口，即分配饼干，满足小孩+1，g和s数组同时下标-1
            if(s[j] >= g[i]){
                count++;
                j--;
                i--;
            //饼干小于小孩胃口，胃口数组g下标-1
            }else{
                i--;
            }
        }
        return count;
    }
}

```
##376. 摆动序列



```java


```
