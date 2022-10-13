# Section1.1

## 1. 准备工作

安装了gitbook，趟了所有可能遇到的坑，哎。

	https://juejin.cn/post/6931225754264928269
	https://zhuanlan.zhihu.com/p/107334179
	https://blog.csdn.net/qq_33320324/article/details/121893271
	https://www.chengweiyang.cn/gitbook/basic-usage/README.html
	https://www.byto.top/tutorial_gitbook/chap5_publish/gitpages.html
	https://ericyuan1201.github.io/algorithm/
	//解决GitHub一直推不上的问题，每天都要更新一下ip有点烦。
	//应该写个脚本，自动更新host
	https://ipaddress.com/website/github.global.ssl.fastly.net
	https://jasonkayzk.github.io/2019/10/10/%E5%85%B3%E4%BA%8E%E4%BD%BF%E7%94%A8Git%E6%97%B6push-pull%E8%B6%85%E6%97%B6-%E4%BB%A5%E5%8F%8AGithub%E8%AE%BF%E9%97%AE%E6%85%A2%E7%9A%84%E8%A7%A3%E5%86%B3%E5%8A%9E%E6%B3%95/
	gitbook有缓存啊，upload之后好久才刷新，哎。
	
## 2. 704. 二分查找

这个最基础的题，我是用了<font color=red>动态规划</font>的思想。

自己模拟的数据如：4,5 ； 4,5,6 这两个已经覆盖了所有的可能。

4，5，6毫无疑问，left + right   / 2

4, 5 的话，是4.5，需要进1，不然会一直卡在4的地方，陷入死循环。

``` java
public static int search(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
        return -1;
    }
    if (nums[0] > target || nums[nums.length - 1] < target) {
        return -1;
    }
    //int left, right, middle
    int left = 0;
    int right = nums.length - 1;
    while (left <= right) {
        int middle = Math.round((left + right) * 1.0f / 2); //注意点3
        if (nums[middle] == target) {
            return middle;
        } else if (nums[middle] < target) {
            left = middle + 1; //注意点1
        } else {
            right = middle - 1; //注意点2
        }
    }
    return -1;
}
```

## 27. 移除元素

困成狗了，今天先到这，明天再看吧。

这个是用的直接覆盖的形式，甚至没有交换。

``` java
    public int removeElement(int[] nums, int val) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int i = 0; //当前index
        int j = 0; //下一个非val的索引
        for (i = 0; i < nums.length; i ++) {
            if (nums[i] != val) {
                //这里甚至不用交换
                nums[j] = nums[i];
                j ++;
            }

        }
        return j;
    }
```


