#5 层序遍历，226.翻转二叉树，101.对称二叉树 2

##5 层序遍历

层序遍历是最基础的题了。核心是队列，for循环遍历队列

```java
public List<List<Integer>> levelOrder(TreeNode root) {
    if (root == null) {
        return null;
    }
    List<List<Integer>> res = new ArrayList<>();
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
        List<Integer> list = new ArrayList<>();
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            TreeNode poll = queue.poll();
            if (poll != null) list.add(poll.val);
            if (poll != null && poll.left != null) queue.offer(poll.left);
            if (poll != null && poll.right != null) queue.offer(poll.right);
        }
        res.add(list);
    }
    return res;
}

```
##226.翻转二叉树

之前做过，再写一遍吧。有点像反转链表，不过链表是while循环，这个是递归。

```java
public TreeNode invertTree(TreeNode root) {
  innerInvertTree(root);
  return root;
}

private void innerInvertTree(TreeNode root) {
  if (root == null) {
     return;
  }
  if (root.left == null && root.right == null) {
     return;
  }
  TreeNode temp = root.left;
  root.left = root.right;
  root.right = temp;
  innerInvertTree(root.left);
  innerInvertTree(root.right);
}

```
##101.对称二叉树 2

这个其实也可以用层序遍历，然后获取每一层的元素，然后判断是否符合对称的结果。

```java
public boolean isSymmetric(TreeNode root) {
  if (root == null) return true;
  return check(root.left, root.right);
}

private boolean check(TreeNode left, TreeNode right) {
  if (left == null && right == null) {
     return true;
  }
  if (left == null || right == null) {
     return false;
  }
  return left.val == right.val
          && check(left.left, right.right)
          && check(left.right, right.left);
}

```
