#7 110.平衡二叉树，257. 二叉树的所有路径，404.左叶子之和

##7 110.平衡二叉树

从上到下写出来了，从下到上没写出来

```java
public boolean isBalanced2(TreeNode root) {
  if (root == null) {
     return true;
  }
  if (root.left == null && root.right == null) {
     return true;
  }
  int leftDepth = getDepth(root.left);
  int rightDepth = getDepth(root.right);
  return Math.abs(leftDepth - rightDepth) <= 1 && isBalanced2(root.left) && isBalanced2(root.right);
}

public int getDepth(TreeNode node) {
  if (node == null) {
     return 0;
  }
  int leftDepth = getDepth(node.left);
  int rightDepth = getDepth(node.right);
  return 1 + Math.max(leftDepth, rightDepth);
}

解法二：
public boolean isBalanced(TreeNode root) {
  return getHeight(root) != -1;
}

public int getHeight(TreeNode node) {
  if (node == null) {
     return 0;
  }
  int leftHeight = getHeight(node.left);
  if (leftHeight == -1) {
     return -1;
  }
  int rightHeight = getHeight(node.right);
  if (rightHeight == -1) {
     return -1;
  }
  if (Math.abs(leftHeight - rightHeight) > 1) {
     return -1;
  }
  return 1 + Math.max(leftHeight, rightHeight);
}
```
##257. 二叉树的所有路径

这个题之前做过，不过这次完全忘了

```java
public List<String> binaryTreePaths(TreeNode root) {
  List<String> list = new ArrayList<>();
  if (root == null) {
     return list;
  }
  String path = "" + root.val;
  findPath(list, path, root);
  return list;
}

private void findPath(List<String> list, String path, TreeNode root) {
  if (root.left == null && root.right == null) {
     list.add(path);
     return;
  }
  if (root.left != null) {
     findPath(list, path + "->" + root.left.val, root.left);
  }
  if (root.right != null) {
     findPath(list, path + "->" + root.right.val, root.right);
  }
}

```
##404.左叶子之和

其实都是递归，我觉得需要好好理解一下递归的概念了。

```java
public int sumOfLeftLeaves(TreeNode root) {
//      int sum = 0;
//      return sumLeftLeaves(root, sum);

//   }
  return root != null ? dfs(root) : 0;
}

public int dfs(TreeNode node) {
  int ans = 0;
  if (node.left != null) {
     ans += isLeafNode(node.left) ? node.left.val : dfs(node.left);
  }
  if (node.right != null && !isLeafNode(node.right)) {
     ans += dfs(node.right);
  }
  return ans;
}

public boolean isLeafNode(TreeNode node) {
  return node.left == null && node.right == null;
}

```
