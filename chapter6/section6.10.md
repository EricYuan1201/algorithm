#3 538.把二叉搜索树转换为累加树，108.将有序数组转换为二叉搜索树 ，669. 修剪二叉搜索树

##3 538.把二叉搜索树转换为累加树


```java
int preSum = 0;

public TreeNode convertBST(TreeNode root) {
    preSum = 0;
    nodeSum(root);
    return root;
}

// 记录前一个节点的累加值
public void nodeSum(TreeNode root) {
    if (root == null) {
        return;
    }
    // 遍历右子树
    nodeSum(root.right);
    // 对节点值累加
    root.val += preSum;
    // 更新 preSum 值
    preSum = root.val;
    // 遍历左子树
    nodeSum(root.left);
}

```
##108.将有序数组转换为二叉搜索树



```java
public TreeNode sortedArrayToBST(int[] nums) {
    return build(nums, 0, nums.length - 1);
}

private TreeNode build(int[] nums, int left, int right) {
    if (left > right) {
        return null;
    }
    int middle = (left + right) / 2;
    TreeNode root = new TreeNode(middle);
    root.left = build(nums, left, middle - 1);
    root.right = build(nums, middle + 1, right);
    return root;
}

```
##669. 修剪二叉搜索树



```java


```
