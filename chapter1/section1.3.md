# 数组总结一

## 1.二分查找

	这个里面注意点：middle
	left = middle + 1
	right = middle -1
	以及寻址middle的时候要进一，用的是Math.round()
	想的点是4，5；如果是直接/2，就会一直卡在4上面。
	
## 2. 移除元素

	用的指针思想，有一个指针单独记录非target的数据的指针。
	然后for循环的时候，直接 num[j] = num[i]
	这个果然已经忘记思路了。今天相当于复习了一遍。
	还是理解for循环，究竟代表什么。
	for循环就是遍历所有元素，是一种动态的思想。
	用了一种反着的思想。可以判断非target的元素，也可以判断是target的元素。
	
## 3. 有序数组的平方和

	双指针思想：
	left, right
	slow, fast
	head, tail
	这个是用的head，tail的思想。
	然后用的是倒序遍历的形式。
	header ++
	tail ++
	
## 4.长度最小的子数组

	大名鼎鼎的滑动数组思想。
	虽然知道是滑动数组思想，但是当时写有写出来。
	比较的模版代码：
	int res = Integer.MAX_VALUE:
	res = Math.min(res, (right - left) + 1)
	滑动窗口，两个while循环。
	while(right < end) {
		while(sum >= target) {
			sum -= nums[start]
			start++
		}
		end ++
	}
	最后的一个return甚至都有坑。如果是最大值，return 0，否则 return res。
	
## 5.螺旋矩阵II

	没啥说的，直接抄的答案。
	x, y
	layer, layers
	如果是5，每一行遍历4个元素。
	while循环，for循环。
	

## 整体总结

	1. 需要再次理解for循环，while循环思想。
	2. 指针，常用的双指针以及二维数组x,y。指针要写对。
	3. 一些模版代码。Math.min() , target...
	4. 滑动窗口
	5. 正反逻辑，满足target，不满足target。