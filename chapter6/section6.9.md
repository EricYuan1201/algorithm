#2 235. 二叉搜索树的最近公共祖先，701.二叉搜索树中的插入操作，450.删除二叉搜索树中的节点

##2 235. 二叉搜索树的最近公共祖先


	
	你可能会疑惑这样找出来的公共祖先深度是否是最大的。其实是最大的，因为我们是自底向上从叶子节点开始更新的，
	所以在所有满足条件的公共祖先中一定是深度最大的祖先先被访问到。
```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
  if (root.val > p.val && root.val > q.val) {
     return lowestCommonAncestor(root.left, p, q);
  } else if (root.val < p.val && root.val < q.val) {
     return lowestCommonAncestor(root.right, p, q);
  }
  return root;
}

```
##701.二叉搜索树中的插入操作

最近的题都是没看懂题目

```java
解法一：
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }

        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }
        return root;
    }
}

解法二：
/**
 * 只要返回一个结果即可
 */
public TreeNode insertIntoBST(TreeNode root, int val) {
    if (root == null) {
        return new TreeNode(val);
    }
    TreeNode cur = root;
    while (cur.left != null || cur.right != null) {
        if (cur.val < val && cur.right != null) {
            cur = cur.right;
        } else if (cur.val > val && cur.left != null) {
            cur = cur.left;
        } else {
            break;
        }
    }
    if (cur.val < val) {
        cur.right = new TreeNode(val);
    } else {
        cur.left = new TreeNode(val);
    }
    return root;
}

```
##450.删除二叉搜索树中的节点

待定

```java
public TreeNode deleteNode(TreeNode root, int key) {
  if (root == null) {
     return null;
  }
  if (root.val < key) {
     root.right = deleteNode(root.right, key);
  } else if (root.val > key) {
     root.left = deleteNode(root.left, key);
  } else {
     if (root.left == null) {
        return root.right;
     } else if (root.right == null) {
        return root.left;
     } else {
        TreeNode node = root.right;
        while (node.left != null) {
           node = node.left;
        }
        node.left = root.left;
        root = root.right;
     }
  }
  return root;
}

```
