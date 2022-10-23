#day10 232.用栈实现队列，225. 用队列实现

##232.用栈实现队列

这个题很经典了，写了很多错误的地方。
我有印象是两个栈实现一个队列，但是没记得名字，其实是一个 inStack，一个outStack。
每次添加元素都用inStack。
每次取元素，都判断outStack是否为空，如果不为空，直接取outStack。
否则把inStack塞到outStack，再取outStack，因为stack的顺序是颠倒的，颠倒一次直接顺序就变成队列的那种了。

```java
class MyQueue {

    Stack<Integer> stack = new Stack<>();
    Stack<Integer> tmpStack = new Stack<>();
    /**
     * 栈是先进后出
     * 队列是先进先出
     */
    public MyQueue() {

    }

    public void push(int x) {
        stack.push(x);
    }

    /**
     * 先进先出了
     *
     * 1,2,3
     */
    public int pop() {
        if (tmpStack.size() > 0) {
            while (stack.size() > 0) {
                tmpStack.push(stack.pop());
            }
        }
        return tmpStack.pop();
    }

    public int peek() {
        if (tmpStack.size() > 0) {
            while (stack.size() > 0) {
                tmpStack.push(stack.pop());
            }
        }
        return tmpStack.peek();
    }

    public boolean empty() {
        return stack.size() == 0 && tmpStack.size() == 0;
    }
}



```
##225. 用队列实现栈

队列实现栈，只需要一个队列，这个可以记下来了。
之前是在out上下功夫，这个就需要在in上下功夫。
添加直接添加就行，添加完成之后，要把之前的元素都再添加一遍。每次来元素的时候都是颠倒的。
取元素直接取就行。

```java
class MyStack {

    Queue<Integer> queue = new LinkedList<>();

    /**
     * 队列先进先出, 1,2,3, 4, 5
     *
     * 栈先进后出
     */
    public MyStack() {

    }

    public void push(int x) {
        int n = queue.size();
        queue.offer(x);
        for (int i = 0; i < n; i++) {
            queue.offer(queue.poll());
        }
    }

    public int pop() {
        return queue.poll();
    }

    public int top() {
        return queue.peek();
    }

    public boolean empty() {
        return queue.isEmpty();
    }
}

```
