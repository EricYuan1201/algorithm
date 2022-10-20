#day08 344.反转字符串，541. 反转字符串II， 剑指Offer 05.替换空格，151.翻转字符串里的单词，剑指Offer58-II.左旋转字符串

##day08 344.反转字符串

先不写了

```java


```
##541. 反转字符串II

边界条件没写好

```java

    /**
     * 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
     * <p>
     * 如果剩余字符少于 k 个，则将剩余字符全部反转。
     * 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
     */
    public String reverseStr(String s, int k) {
        int length = s.length();
        char[] chars = s.toCharArray();
        for (int i = 0; i < length; i = i + 2 * k) {
            int left = i;
            int right = Math.min(i + k-1, length - 1);
             revert(chars, left, right);
        }
        return new String(chars);
    }

    public void revert(char[] chars, int left, int right) {
        while (left <= right) {
            char temp = chars[right];
            chars[right] = chars[left];
            chars[left] = temp;
            left++;
            right++;
        }
    }
    

```
##剑指Offer 05.替换空格



```java

    public String replaceSpace(String s) {
        int length = s.length();
        char[] chars = s.toCharArray();
        char[] newChars = new char[length * 3];
        int size = 0;
        for (int i = 0; i < length; i++) {
            if (chars[i] == ' ') {
                newChars[size] = '%';
                newChars[size++] = '2';
                newChars[size++] = '0';
            } else {
                newChars[size] = chars[i];
            }
            size ++;
        }
        return new String(chars, 0, size);
    }

```
##151.翻转字符串里的单词



```java


```
##剑指Offer58-II.左旋转字符串



```java


```
