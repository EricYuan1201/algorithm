#day11 20. 有效的括号，1047. 删除字符串中的所有相邻重复项，150. 逆波兰表达式求

##20. 有效的括号

这个题之前做过，知道是用stack实现。
有一个点需要注意一下，stack为空的时候，peek，poll都会报错，需要做好判空.

```java

public static boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == ')' && stack.size() > 0 && '(' == stack.peek()) { // ----> 这个地方会报错。
            stack.pop();
        } else if (s.charAt(i) == '}' && stack.size() > 0 && '{' == stack.peek()) {
            stack.pop();
        } else if (s.charAt(i) == ']' && stack.size() > 0 && '[' == stack.peek()) {
            stack.pop();
        } else {
            stack.push(s.charAt(i));
        }
    }
    return stack.size() == 0;
}

```
##1047. 删除字符串中的所有相邻重复项

这个也是一个stack，然后用的stringbuilder进行拼接的。
关键是最后的遍历，因为没办法倒序，所以是在StringBuilder进行reverse的。

```java
public String removeDuplicates(String s) {
    Stack<Character> stack = new Stack<>();
    for (int i = 0; i < s.length(); i++) {
        if (stack.size() > 0 && s.charAt(i) == stack.peek()) {
            stack.pop();
        } else {
            stack.push(s.charAt(i));
        }
    }
    StringBuilder stringBuilder = new StringBuilder();
    while (stack.size() > 0) {
        stringBuilder.append(stack.pop());
    }
    return stringBuilder.reverse().toString();
}

```
##150. 逆波兰表达式求

我没想到的是根据 + - * / 做逻辑。
还是用的stack，其实list也能实现吧，不过stack这种pop的逻辑很适合，list还需要remove元素，比较麻烦。

```java
public int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();
    for (int i = 0; i < tokens.length; i++) {
        if ("+".equals(tokens[i])
                || "-".equals(tokens[i])
                || "*".equals(tokens[i])
                || "/".equals(tokens[i])
        ) {
            Integer pre = stack.pop();
            Integer prePre = stack.pop();
            int s = -1;
            if ("+".equals(tokens[i])) {
                s = pre + prePre;
            } else if ("-".equals(tokens[i])) {
                s = prePre - pre;
            } else if ("*".equals(tokens[i])) {
                s = prePre * pre;
            } else {
                s = prePre / pre;
            }
            stack.push(s);
        } else {
            stack.push(Integer.parseInt(tokens[i]));
        }
    }
    return stack.pop();
}

```
