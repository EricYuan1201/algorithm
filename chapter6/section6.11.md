# 树总结一 （遍历）

### 树的遍历概念：

理解前序、中序、后序遍历：（看着这个图能够理解遍历顺序）

![2022-11-06_d80b00f4db40.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_d80b00f4db40.jpg)

	前序遍历：先中，然后把所有的左边的遍历完，然后遍历右。
	
	中序遍历：先左，然后中，最后是右。
	
	后序遍历：先左，后右，最后是中。

### 树的遍历算法：

#### 1. 递归写法

	    public void preOrderTree(){}

	    public void inorderTree(){}
	
	    public void postOrderTree(){}
	
	    /**
	     * 如果是递归版本，只需要调整下面3行代码的顺序即可。
	     */
	    public void order(TreeNode node, List<TreeNode> res){
	        if (node == null) {
	            return;
	        }
	        order(node.left, res);
	        res.add(node);
	        order(node.right, res);
	    }

####2. 迭代写法：

**先序遍历**

![2022-11-06_758e9e9cf25a.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_758e9e9cf25a.jpg) 

**中序遍历**

![2022-11-06_b749e1b2d5ef.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_b749e1b2d5ef.jpg)

**后序遍历**
![2022-11-06_c48a928a4785.jpg](https://cdn.jsdelivr.net/gh/EricYuan1201/img/2022-11-06_c48a928a4785.jpg)

### 总结：

	
	二叉树的递归遍历一般是easy级别，但是如果用迭代就变成了medium或者hard了。
	
	
	（中午休息了一下，有点怀疑自己现在做的事情是否有意义）
	
	
	迭代是需要自己在脑子里过一些整个顺序，如果自己大脑的推演能力不行的话，很容易就中断了。


   