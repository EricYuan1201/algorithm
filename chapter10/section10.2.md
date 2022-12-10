#9 503.下一个更大元素II，42. 接雨水

##9 503.下一个更大元素II

取模处理

```java
public int[] nextGreaterElements(int[] nums) {
    int n = nums.length;
    int[] ret = new int[n];
    Arrays.fill(ret, -1);
    Deque<Integer> stack = new LinkedList<Integer>();
    for (int i = 0; i < n * 2 - 1; i++) {
        while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n]) {
            ret[stack.pop()] = nums[i % n];
        }
        stack.push(i % n);
    }
    return ret;
}

```
##42. 接雨水

写不来。

```java


```
