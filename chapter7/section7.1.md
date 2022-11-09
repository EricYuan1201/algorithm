#6 39. 组合总和，40.组合总和II，131.分割回文

##6 39. 组合总和
![2022-11-07_c6546edf955f.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-07_c6546edf955f.jpg)

![2022-11-07_98f985920404.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-07_98f985920404.jpg)



回溯的理解：

	1. 是一棵树，需要用dfs
	2. 记录begin, len 然后进行for循环
	3. 如果是可以重复的，下一次依然是i，如果是不可以重复的，下一次是i+1
	4. 回溯的本质是递归 + 回溯。
	5. 一个进行了排序，一个未进行排序

```java
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
   public List<List<Integer>> combinationSum(int[] candidates, int target) {
      int len = candidates.length;
      List<List<Integer>> res = new ArrayList<>();
      if (len == 0) {
         return res;
      }
      Arrays.sort(candidates);
      Deque<Integer> path = new ArrayDeque<>();
      dfs(candidates, 0, len, target, path, res);
      return res;
   }
   /**
    * @param candidates 候选数组
    * @param begin      搜索起点
    * @param len        冗余变量，是 candidates 里的属性，可以不传
    * @param target     每减去一个元素，目标值变小
    * @param path       从根结点到叶子结点的路径，是一个栈
    * @param res        结果集列表
    */
   private void dfs(int[] candidates, int begin, int len, int target, Deque<Integer> path, List<List<Integer>> res) {
      // target 为负数和 0 的时候不再产生新的孩子结点
//      if (target < 0) {
//         return;
//      }
      if (target == 0) {
         res.add(new ArrayList<>(path));
         return;
      }
      // 重点理解这里从 begin 开始搜索的语意
      for (int i = begin; i < len; i++) {
         // 还是有不同的，因为本身不是有序的
         if (target - candidates[i] < 0) {
            break;
         }
         //如果不可重复，就多个这个步骤
         //if (i > begin && candidates[i] == candidates[i - 1]) {
            //continue;
         //}
         path.addLast(candidates[i]);
         // 注意：由于每一个元素可以重复使用，下一轮搜索的起点依然是 i，这里非常容易弄错
         dfs(candidates, i, len, target - candidates[i], path, res);
         // 状态重置
         path.removeLast();
      }
   }
```
##40.组合总和II



```java
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。
   public List<List<Integer>> combinationSum(int[] candidates, int target) {
      int len = candidates.length;
      List<List<Integer>> res = new ArrayList<>();
      if (len == 0) {
         return res;
      }
      Arrays.sort(candidates);
      Deque<Integer> path = new ArrayDeque<>();
      dfs(candidates, 0, len, target, path, res);
      return res;
   }
   /**
    * @param candidates 候选数组
    * @param begin      搜索起点
    * @param len        冗余变量，是 candidates 里的属性，可以不传
    * @param target     每减去一个元素，目标值变小
    * @param path       从根结点到叶子结点的路径，是一个栈
    * @param res        结果集列表
    */
   private void dfs(int[] candidates, int begin, int len, int target, Deque<Integer> path, List<List<Integer>> res) {
      // target 为负数和 0 的时候不再产生新的孩子结点
//      if (target < 0) {
//         return;
//      }
      if (target == 0) {
         res.add(new ArrayList<>(path));
         return;
      }
      // 重点理解这里从 begin 开始搜索的语意
      for (int i = begin; i < len; i++) {
         // 还是有不同的，因为本身不是有序的
         if (target - candidates[i] < 0) {
            break;
         }
         //如果不可重复，就多个这个步骤
         if (i > begin && candidates[i] == candidates[i - 1]) {
            continue;
         }
         path.addLast(candidates[i]);
         // 注意：由于每一个元素可以重复使用，下一轮搜索的起点依然是 i，这里非常容易弄错
         dfs(candidates, i+1, len, target - candidates[i], path, res);
         // 状态重置
         path.removeLast();
      }
   }
```
##131.分割回文



```java
```