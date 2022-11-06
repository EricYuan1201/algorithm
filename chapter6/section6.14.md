# 树总结——二叉搜索树

### 概念题：

**二叉搜索树的核心：中序遍历是一个自增序列。**

二叉搜索树的搜索部分，有点类似Java的二分查找法，这里复习一下。

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

![2022-11-06_41e48d7d05bc.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_41e48d7d05bc.jpg)

这个题依然利用了前面的递归部分。


![2022-11-06_0af98b2c7b4d.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_0af98b2c7b4d.jpg)

### 二叉搜索树的插入、删除

### 最近公共祖先部分：

（有点撑不住了，这个算法真的要分上午，中午，下午去看，如果一天一直看算法，简直头晕脑胀）
