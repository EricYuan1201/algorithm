#5 860.柠檬水找零，406.根据身高重建队列，452. 用最少数量的箭引爆气球

##5 860.柠檬水找零

好久没有过的一遍过了！！！
我知道是用一个东西记录，但是没想到两个指针就可以了。


```java
public boolean lemonadeChange(int[] bills) {
  if (bills == null) {
     return true;
  }
  int five = 0;
  int ten = 0;
  for (int i = 0; i < bills.length; i++) {
     if (bills[i] == 5) {
        five ++;
     } else if (bills[i] == 10) {
        if (five == 0) {
           return false;
        }
        ten ++;
        five --;
     } else if (bills[i] == 20) {
        if (ten == 0) {
           if (five < 3) {
              return false;
           }
           five -=3;
        } else {
           if (five == 0) {
              return false;
           }
           ten --;
           five --;
        }
     }
  }
  return true;
}

```
##406.根据身高重建队列



```java


```
##452. 用最少数量的箭引爆气球

贪心算法重叠空间。

学习了一下排序的写法，return -1 是升序的。大概了解了一下写法。

```java
/**
 * 重叠区间的贪心算法
 */
public int findMinArrowShots(int[][] points) {
    if (points.length == 0) return 0;
    Arrays.sort(points, (p1, p2) -> p1[1] < p2[1] ? -1 : 1);
    int border = points[0][1];
    int count = 1;
    for (int[] point : points) {
        if (point[0] > border) {
            border = point[1];
            count ++;
        }
    }
    return count;
}

```
