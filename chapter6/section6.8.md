#1 530.二叉搜索树的最小绝对差，501.二叉搜索树中的众数，236. 二叉树的最近公共祖先

##1 530.二叉搜索树的最小绝对差

二叉搜索树看到这个题目就想到中序遍历，中序遍历是一个自增的数组，

关键是看中间那个print变形成什么样子。

```java
private TreeNode preNode = null;
private int min = Integer.MAX_VALUE;

public int getMinimumDifference(TreeNode root) {
  inorder(root);
  return min;
}

private void inorder(TreeNode root) {
  if (root == null) {
     return;
  }
  inorder(root.left);
  if (preNode != null) {
     min = Math.min(min, Math.abs(root.val - preNode.val));
  }
  preNode = root;
  inorder(root.right);
}

```
##501.二叉搜索树中的众数

这个绝对不是一个简单题，依然是中序遍历。

```java
List<Integer> answer = new ArrayList<Integer>();
int base, count, maxCount;


public int[] findMode(TreeNode root) {
  inorder(root);
  int[] arr = new int[answer.size()];
  for (int i = 0; i < answer.size(); i++) {
     arr[i] = answer.get(i);
  }
  return arr;
}

public void inorder(TreeNode root) {
  if (root == null) {
     return;
  }
  inorder(root.left);
  update(root);
  inorder(root.right);
}

private void update(TreeNode root) {
  if (root.val == base) {
     count ++;
  } else {
     base = root.val;
     count = 1;
  }
  if (count == maxCount) {
     answer.add(root.val);
  } else if (count > maxCount) {
     answer.clear();
     answer.add(root.val);
     maxCount = count;
  }
}

```
##236. 二叉树的最近公共祖先

开始有点不理解了。。。。

p,qp,q 其中一个在 rootroot 的 右子树 中，此时 rightright 指向 pp（假设为 pp ）；
p,qp,q 两节点都在 rootroot 的 右子树 中，此时的 rightright 指向 最近公共祖先节点 ；

有一点懵懂的感觉

```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
  if (root == null) return root;
  if (root.val == p.val) {
     return root;
  }
  if (root.val == q.val) {
     return root;
  }
  if (find(root.left, p) && find(root.left, q)) {
     return lowestCommonAncestor(root.left, p, q);
  }
  if (find(root.right, p) && find(root.right, q)) {
     return lowestCommonAncestor(root.right, p, q);
  }
  return root;
}

private boolean find(TreeNode root, TreeNode target) {
  if (root == null) return false;
  if (root.val == target.val) return true;
  return find(root.left, target) || find(root.right, target);
}

```
