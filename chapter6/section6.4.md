#6 104.二叉树的最大深度，559.n叉树的最大深度，111.二叉树的最小深度，222.完全二叉树的节点个数

##6 104.二叉树的最大深度

基础题，熟读背诵的情况。

```java
public int maxDepth(TreeNode root) {
  if (root == null) {
     return 0;
  }
  int leftDepth = maxDepth(root.left);
  int rightDepth = maxDepth(root.right);
  return 1 + Math.max(leftDepth, rightDepth);
}

```
##559.n叉树的最大深度

基础题的变形，很容易理解。

```java
public int maxDepth(TreeNode root) {
  if (root == null) {
     return 0;
  }
  int maxDepth = 0;
  for (int i = 0; i < root.children.size(); i++) {
     int depthI = maxDepth(root.children.get(i));
     maxDepth = Math.max(maxDepth, depthI);
  }
  return 1 + maxDepth;
}

```
##111.二叉树的最小深度

有点难以理解了。。。

事实上第三遍看的时候还是没有理解。

```java
public int minDepth(TreeNode root) {
  if (root == null) {
     return 0;
  }
  int leftDepth = minDepth(root.left);
  int rightDepth = minDepth(root.right);
  //如果一个为空，另一个不为空，则不是叶子节点。
  //而求最大深度的时候则没有这个问题，相当于问题被掩盖了。
  if (root.left == null && root.right != null) {
     return 1 + rightDepth;
  }
  if (root.left != null && root.right == null) {
     return 1 + leftDepth;
  }
  return 1 + Math.min(leftDepth, rightDepth);
}

```
##222.完全二叉树的节点个数

1.掌握位运算

2.完全二叉树包含的满二叉树的概念

3.leftHeight == rightHeight，则左边是满二叉树，否则右边是满二叉树。

```java
/**
* 完全二叉树的定义：
*
* 1.除了底层没有填满，其他层都填满了。
* 2.底层的节点一定是存在最左边的若干位置。
* 3.完全二叉树里面一定有满二叉树。
* 4.如果左边的深度 === 右边的深度，则左边一定填满了。
* 5.否则右边的深度一定填满了。
* 6.然后继续使用递归即可。
*/
public int countNodes(TreeNode root) {
  if (root == null) {
     return 0;
  }
  if (root.left == null && root.right == null) return 1;
  int leftDepth = getDepth(root.left);
  int rightDepth = getDepth(root.right);
  if (leftDepth == rightDepth) {
     //1 << leftDepth = 2 ^ leftDepth，实际上是先减1，然后再加1
     return (1 << leftDepth) + countNodes(root.right);
  } else {
     return (1 << rightDepth) + countNodes(root.left);
  }
}

public int getDepth(TreeNode node) {
  if (node == null) {
     return 0;
  }
  int depth = 1;
  while (node.left != null) {
     node = node.left;
     depth += 1;
  }
  return depth;
}

```
