# 树总结——递归解题

在我印象中，二叉树是有递归模板的，等我找到，再粘到这个地方。

但是实际上，很多题目也不是一个简单的模板就能解决的，都是有很多变种。

关于递归的问题，我的脑子也只能想一些边界的情况，中间的过程不需要细想。

![2022-11-06_a0fca16f298a.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_a0fca16f298a.jpg)


### 题目：

是否需要拆分方法进行递归，还是直接在原题上进行递归，其实要看递归

一个前缀，看见树的题目，先判断一下根节点。

**递归的基础思路：**

	1. 解决root节点，按照这个思路分别解决root.left节点，root.right节点。
	2. 解决了root这一层级，再分别解决下面的层级。
	3. 聚焦在解决root上面，子节点的任务交给递归就行。

#### 反转二叉树； 合并二叉树； 二叉树的路径 （处理root，递归roor.left，root.right）

![2022-11-06_29d550864d48.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_29d550864d48.jpg)

![2022-11-06_6fab46710528.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_6fab46710528.jpg)

![2022-11-06_4d0a56e53003.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_4d0a56e53003.jpg)


#### 求最大，最小 深度：（在递归中解决问题）

![2022-11-06_d95692cf6c2c.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_d95692cf6c2c.jpg)

![2022-11-06_68855ed4064d.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_68855ed4064d.jpg)


