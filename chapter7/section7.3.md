#9 78. 子集，90. 子集 II

##9 78. 子集

子集反而是写法最简单的。

首先不是组合，不需要考虑target的问题

只有排列才具有顺序不一致的意义，所以每次都是从start=0开始。组合和子集，排列顺序都是无意义的，所以会记录一个startIndex。

排列一定需要 isUsed
子集只有有重复的时候才用isused。 （isUsed到底是干嘛的？）

```java
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


class Solution {
    List<List<Integer>> res;
    List<Integer> list = new ArrayList<>();
    public List<List<Integer>> subsets(int[] nums) {
        res = new ArrayList<>();
        backTracing(nums, 0);
        return res;
    }
    public void backTracing(int[] nums, int start){
        // 每更新一次list  都加入结果集  首次进来加的是空集
        res.add(new ArrayList<>(list));
        // 到数组末尾结束当前递归
        if(start == nums.length){
            return;
        }
        for(int i = start; i < nums.length; i++){
            // 将当前数加入list
            list.add(nums[i]);
            // 递归 不能重复使用当前数 因此下一轮从i+1开始
            backTracing(nums, i+1);
            // 回溯 回退刚刚加的数
            list.remove(list.size()-1);
        }
    }
}

```
##90. 子集 II



```java

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

 

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]



class Solution {
   List<List<Integer>> result = new ArrayList<>();// 存放符合条件结果的集合
   LinkedList<Integer> path = new LinkedList<>();// 用来存放符合条件结果
   boolean[] used;
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        if (nums.length == 0){
            result.add(path);
            return result;
        }
        Arrays.sort(nums);
        used = new boolean[nums.length];
        subsetsWithDupHelper(nums, 0);
        return result;
    }
    
    private void subsetsWithDupHelper(int[] nums, int startIndex){
        result.add(new ArrayList<>(path));
        if (startIndex >= nums.length){
            return;
        }
        for (int i = startIndex; i < nums.length; i++){
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]){
                continue;
            }
            path.add(nums[i]);
            used[i] = true;
            subsetsWithDupHelper(nums, i + 1);
            path.removeLast();
            used[i] = false;
        }
    }
}
```
