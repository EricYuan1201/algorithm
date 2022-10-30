# 链表总结一

## 203.移除链表元素

	1. 链表因为不知道length，所以一般是用while循环。
	2. 这个算法知道了还是很简单的。while循环，temp = temp.next。
	3. 哨兵节点，简直是必备的了。
	4. 值传递，还是值传递，即使构建了一个temp，也是里面的元素。


## 206.反转链表

	1. 这个需要记得像吃饭喝水一样。
	2. 构建哨兵节点，pre, cur, tmp。
	3. 最后return的是pre，注意处理head节点。
	4. while(cur != null) ----》 这句话的意思是cur == null 的时候终止的，
	   外界条件一定是 cur == null。

## 24. 两两交换链表中的节点

	1. 需要处理4个节点，pre, cur ,next, nextNext。
	2. 之前有一句话说的好，还是pre, cur， tmp的变形题。
	3. 构建了一个i，判断该节点是否需要处理。
	4. 构建哨兵节点。

## 19.删除链表的倒数第N个节点

	1. 删除节点的本质就是 cur.next = cur.next.next()；这样就把第cur.next节点给删除了。
	2. 依然构建哨兵节点。
	3. 这个也之前做过了。

## 链表相交
   
     1. 记得思路，没写出来。
     2. 这个思路是，A走了 123，45，2；B走了 2，45，123，然后二者相交。
     3. 如果一定相交的话，A走到结束了指向B，B结束了指向A的头。
     4. 终止条件就是 curA == curB，那么while循环就是 curA != curB。
     5. 结合反转链表，对while循环多了一些理解。

## 142.环形链表II

	1. 交点不是环形的入口。
	2. 构建了slow，fast指针
	3. slow : s，fast： s + nb ，同时 fast= 2s ---> s = nb。
	4. 则slow再走k步就到了入口，k + n *b ; k + 0 * b
	4. 二者一定在入口处相交。让fast指向head，二者再次跑。
























