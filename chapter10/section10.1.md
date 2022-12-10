#8 739. 每日温度，496.下一个更大元素 I

##8 739. 每日温度

单调栈，用到了栈的知识。

```java
public int[] dailyTemperatures(int[] temperatures) {
    int length = temperatures.length;
    int[] ans = new int[length];
    Deque<Integer> stack = new LinkedList<Integer>();
    for (int i = 0; i < length; i++) {
        int temperature = temperatures[i];
        while (!stack.isEmpty() && temperature > temperatures[stack.peek()]) {
            int prevIndex = stack.pop();
            ans[prevIndex] = i - prevIndex;
        }
        stack.push(i);
    }
    return ans;
}

```
##496.下一个更大元素 I

跟上面那个有点类似。

```java
public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    Deque<Integer> stack = new ArrayDeque<Integer>();
    for (int i = nums2.length - 1; i >= 0; --i) {
        int num = nums2[i];
        while (!stack.isEmpty() && num >= stack.peek()) {
            stack.pop();
        }
        map.put(num, stack.isEmpty() ? -1 : stack.peek());
        stack.push(num);
    }
    int[] res = new int[nums1.length];
    for (int i = 0; i < nums1.length; ++i) {
        res[i] = map.get(nums1[i]);
    }
    return res;
}
```
