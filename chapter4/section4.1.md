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

while循环和for循环的区别：

首先，两者从表达能力上说是等价的，即两者能够完成的事情是一样的。其次，由于for语句将初始化，循环条件和每次循环后对循环变量的修改放在一起，比较清晰直观。因此for语句常用于能够预先判断循环次数的循环或遍历中。如遍历一个数组，或者执行某操作若干次之类。此时用for语句较优。

while语句的历史更久，表达方式上更自由灵活，常用于无法事先判断循环次数的循环。譬如经典的计算C风格字符串的长度的代码，又如后根遍历二叉树的非递归实现。此时用while语句会使程序更清晰。最后强调，两者从表达能力上说是等价的。



```java
public static String reverseWords(String s) {
    int left = 0;
    int right = s.length() - 1;
    //首先去除了两边的空格
    for (int i = left; i <= right; i++) {
        if (s.charAt(i) == ' ') {
            left++;
        } else {
            break;
        }
    }
    for (int i = right; i >= left; i--) {
        if (s.charAt(i) == ' ') {
            right--;
        } else {
            break;
        }
    }
    StringBuilder stringBuilder = new StringBuilder();
    while (right >= left) {
        int index = right;
        while (right >= 0 && s.charAt(right) != ' ') {
            right--;
        }
        for (int i = right + 1; i <= index; i++) {
            stringBuilder.append(s.charAt(i));
        }
        if (right > left) {
            stringBuilder.append(" ");
        }
        while (right >= 0 && s.charAt(right) == ' ') {
            right --;
        }
    }
    return stringBuilder.toString();
}

```
##剑指Offer58-II.左旋转字符串



```java


```
