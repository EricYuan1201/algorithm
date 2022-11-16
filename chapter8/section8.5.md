#5 435. 无重叠区间，763.划分字母区间，56. 合并区间

##5 435. 无重叠区间



```java
public int eraseOverlapIntervals(int[][] intervals) {
      Arrays.sort(intervals, (o1, o2) -> Integer.compare(o1[0], o2[0]));
      int preEnd = intervals[0][1];
      int res = 0;
      for (int i = 1; i < intervals.length; i++) {
         int nowS = intervals[i][0];
         int nowE = intervals[i][1];
         if (nowS >= preEnd) {
            preEnd = nowE;
         } else if (nowE <= preEnd) {
            res ++;
            preEnd = nowE;
         } else {
            res ++;
         }
      }
      return res;
   }

```
##763.划分字母区间



```java


```
##56. 合并区间



```java


```
