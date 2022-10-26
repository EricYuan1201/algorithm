#2 239. 滑动窗口最大值，347.前 K 个高频元

##2 239. 滑动窗口最大值

滑动窗口 + 单调队列。

参考的是这篇题解：
https://leetcode.cn/problems/sliding-window-maximum/solution/dong-hua-yan-shi-dan-diao-dui-lie-239hua-hc5u/

```java
public static int[] maxSlidingWindow(int[] nums, int k) {
    int[] res = new int[nums.length - k + 1];
    LinkedList<Integer> linkedList = new LinkedList<>();
    for (int right = 0; right < nums.length; right++) {
        while (!linkedList.isEmpty() && nums[right] >= nums[linkedList.peekLast()]) {
            linkedList.removeLast();
        }
        linkedList.add(right);
        int left = right - k + 1;
        if (linkedList.peekFirst() < left) {
            linkedList.removeFirst();
        }
        if (right + 1 >= k) {
            res[left] = nums[linkedList.peekFirst()];
        }
    }
    return res;
}

```
##347.前 K 个高频元



```java
public List<Integer> topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
    }
    PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return map.get(o1) - map.get(o2);
        }
    });
    for (Integer key : map.keySet()) {
        if (priorityQueue.size() <= k) {
            priorityQueue.add(key);
        } else if (map.get(key) > map.get(priorityQueue.peek())) {
            priorityQueue.remove();
            priorityQueue.add(key);
        }
    }
    // 取出最小堆中的元素
    List<Integer> res = new ArrayList<>();
    while (!priorityQueue.isEmpty()) {
        res.add(priorityQueue.remove());
    }
    return res;
}

```