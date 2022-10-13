# Section1.2

## 977.有序数组的平方

这里运用的是头尾指针

而且是倒序遍历，构建了一个新的数组。

```java
public int[] sortedSquares(int[] nums) {
    if (nums == null || nums.length == 0) {
        return nums;
    }
    int header = 0;
    int tail = nums.length - 1;
    int[] res = new int[nums.length];
    int i = tail;
    while (header <= tail) {
        if (nums[header] * nums[header] > nums[tail] * nums[tail]) {
            res[i] = nums[header] * nums[header];
            header ++;
        } else {
            res[i] = nums[tail] * nums[tail];
            tail --;
        }
        i --;
    }
    return res;
}
```

## 209.长度最小的子数组

用了一种很蹩脚的方式写出来了，滑动窗口

```java
public static int minSubArrayLen2(int target, int[] nums) {
    if (nums == null || nums.length == 0) {
        return 0;
    }
    int length = nums.length;
    if (length == 1) {
        if (nums[0] > target) {
            return 1;
        } else {
            return 0;
        }
    }
    int count = Integer.MAX_VALUE;
    int left = 0;
    int right = 1;
    int sum = nums[0];
    while (left < right && right < length) {
        if (nums[right] >= target) {
            return 1;
        }
        sum += nums[right];
        if (sum >= target) {
            count = Math.min(count, (right - left) + 1);
//                sum -= nums[left];
//                left ++;
//                if (left == right) {
//                    if (sum >= target) {
//                        return 1;
//                    } else {
//                        right ++;
//                    }
//                }
            while (left < right) {
                sum -= nums[left];
                left ++;
                if (sum < target) {
                    right ++;
                    break;
                } else {
                    count = Math.min(count, (right - left) + 1);
                }
            }
        } else {
            right ++;
        }
    }
    if (count == Integer.MAX_VALUE) {
        return 0;
    }
    return count;
}
```


## 59.螺旋矩阵II

没什么好说的，直接抄了答案，我觉得这种是比较好理解的

关于指针的理解，其实可以用x, y 的，这种更好理解一些。


```java
public int[][] generateMatrix(int n) {
  if (n == 1) {
     int[][] arr = new int[1][1];
     arr[0][0] = 1;
     return arr;
  }
  int[][] arr = new int[n][n];
  //直接抄答案吧，逐层填充法
  int row = 0;
  int column = 0;
  int layers = n / 2;
  int reminder = n % 2;
  int layer = 0;
  int num = 1;
  while (layer <= layers) {
     for (int i = 0; i < n -1 - layer * 2; i++) {
        arr[row][column] = num ++;
        column ++;
     }
     for (int i = 0; i < n -1 - layer * 2; i++) {
        arr[row][column] = num ++;
        row ++;
     }
     for (int i = 0; i < n -1 - layer * 2; i++) {
        arr[row][column] = num ++;
        column --;
     }
     for (int i = 0; i < n -1 - layer * 2; i++) {
        arr[row][column] = num ++;
        row --;
     }
     row ++;
     column ++;
     layer ++;
  }
  if (reminder != 0) {
     arr[n/2][n/2] = n * n;
  }
  return arr;
}
```