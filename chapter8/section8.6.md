#7 738.单调递增的数字，简短的总结篇

##7 738.单调递增的数字

抄了一个题解


```java
public static int monotoneIncreasingDigits(int n){
         if (n < 10) return n;
         char[] arr = String.valueOf(n).toCharArray();
         int i = 0;
         for (; i < arr.length-1; i++) {
            if (i < arr.length-1 && arr[i] > arr[i+1]) {
               break;
            }
         }
         //找到了开始下沉的i，将i-1 减一，后面全部置为9999
         if (i == arr.length -1) return n;
         int j = 0;
         for (; j <= i ; j++) {
            if (arr[j] == arr[i]) {
               break;
            }
         }
         arr[j] = (char) (arr[j]-1);
         j ++;
         for (; j < arr.length; j++) {
            arr[j] = '9';
         }
         return Integer.parseInt(String.valueOf(arr));
      }

```
##简短的总结篇



```java
1. 股票：就是把全部的利益吃掉
2. 分发饼干，直接排序，然后进行双遍历
3. k次取反，依然是排序，然后记录了反转了几次。
4. 找零，five, ten 两个指针
5. 单调增序列，记录开始递减的坐标，然后-1，后面全部置为9999

```
