#0 654.最大二叉树，617.合并二叉树，700.二叉搜索树中的搜索，98.验证二叉搜索树

##0 654.最大二叉树

跟着卡子哥写出来了

遵循前序遍历的形式写出来的。

```java
private TreeNode construct(int[] nums, int left, int right) {
  if (right < left) {
     return null;
  }
  if (right == left) {
     return new TreeNode(nums[left]);
  }
  int maxIndex = left;
  int maxValue = nums[maxIndex];
  for (int i = left+1; i <= right; i++) {
     if (nums[i] > maxValue) {
        maxValue = nums[i];
        maxIndex = i;
     }
  }
  TreeNode root = new TreeNode(maxValue);
  if (maxIndex > 0) {
     root.left = construct(nums, left, maxIndex -1);
  }
  if (maxIndex < nums.length -1) {
     root.right = construct(nums, maxIndex + 1, right);
  }
  return root;
}

```
##617.合并二叉树

完全自己写出来的，不过没形成方法论，迷迷糊糊就写出来了

```java
public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
  if (root1 == null && root2 == null) {
     return null;
  }
  if (root1 == null) return root2;
  if (root2 == null) return root1;
  TreeNode newRoot = new TreeNode(root1.val + root2.val);
  newRoot.left = mergeTrees(root1.left, root2.left);
  newRoot.right = mergeTrees(root1.right, root2.right);
  return newRoot;
}

```
##700.二叉搜索树中的搜索

简单题，差不多能写出来。

```java
public TreeNode searchBST(TreeNode root, int val) {
    if (root == null) {
        return null;
    }
    while (root != null) {
        if (root.val > val) {
            root = root.left;
        } else if (root.val < val) {
            root = root.right;
        } else {
            return root;
        }
    }
    return null;
}

```
##98.验证二叉搜索树

学习学习一下

```java
/**
* 其实就是中序遍历，只要是一个自增序列即可
*/
public boolean isValidBST(TreeNode root) {
  //本来想的是递归的中序遍历，这里学习了一下迭代的中序遍历形式。
  Deque<TreeNode> deque = new LinkedList<>();
  double inOrder = -Double.MAX_VALUE;
  while (!deque.isEmpty() || root != null) {
     while (root != null) {
        deque.push(root);
        root = root.left;
     }
     root = deque.pop();
     if (root.val <= inOrder) {
        return false;
     }
     inOrder = root.val;
     root = root.right;
  }
  return true;
}

```
