#9 491.递增子序列，46.全排列，47.全排列 II

##9 491.递增子序列



```java


```
##46.全排列

这两个题目和昨天的组合真的是非常的像。

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

	大概知道为啥不能用begin了，因为1,2，3 和 2,1,3都是正确的解，所以应该是用完1之后，再用2进行遍历。
	脑子里的那个模型就是递归，就是全排列。其实不用回溯当然也能做。
	后来想想，可能回溯是唯一的解了吧。
	为什么不用begin开始啊？因为还可以用这个元素，必须从0开始。

![2022-11-08_62ccc582b449.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-08_fb5c3aff34ec.jpg)


```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> lists = new ArrayList<>();
        int lenght = nums.length;
        if (lenght == 0) {
            return lists;
        }
        boolean[] isUsed = new boolean[lenght];
        List<Integer> path = new ArrayList<>();
        dfs(lists, path, 0, lenght, nums, isUsed);
        return lists;
    }

    private void dfs(List<List<Integer>> lists, List<Integer> path, int depth, int length, int[] nums, boolean[] isUsed) {
        if (depth == length) {
            lists.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < length; i++) {
            if (!isUsed[i]) {
                path.add(nums[i]);
                isUsed[i] = true;
                dfs(lists, path, depth + 1, length, nums, isUsed);
                isUsed[i] = false;
                path.remove(path.size() -1);
            }
        }
    }
}

```
##47.全排列 II

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
直觉上觉得应该是要排序了。



```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> lists = new ArrayList<>();
        int lenght = nums.length;
        if (lenght == 0) {
            return lists;
        }
        Arrays.sort(nums);
        boolean[] isUsed = new boolean[lenght];
        List<Integer> path = new ArrayList<>();
        dfs2(lists, path, 0, lenght, nums, isUsed);
        return lists;
    }

    private void dfs2(List<List<Integer>> lists, List<Integer> path, int depth, int length, int[] nums, boolean[] isUsed) {
        if (depth == length) {
            lists.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < length; i++) {
            if (isUsed[i]) continue;
            if (i >= 1 && nums[i] == nums[i - 1] && !isUsed[i-1]) continue;
            path.add(nums[i]);
            isUsed[i] = true;
            dfs2(lists, path, depth + 1, length, nums, isUsed);
            isUsed[i] = false;
            path.remove(path.size() - 1);

        }
    }
}

```
