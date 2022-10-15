# day03 203.移除链表元素，206.反转链表 

## 203.移除链表元素 

还是乜有真正理解for循环，开始写的复杂了。

```java

public static ListNode removeElements2(ListNode head, int val) {
  ListNode dummyHead = new ListNode(0);
  dummyHead.next = head;
  ListNode temp = dummyHead;
  while (temp.next != null) {
     if (temp.next.val == val) {
        temp.next = temp.next.next; //注意点
     } else {
        temp = temp.next;
     }
  }
  return dummyHead.next;
}

最开始的写法

public static ListNode removeElements(ListNode head, int val) {
  if (head == null) {
     return null;
  }
  //指针思想？
  ListNode preHead = new ListNode(0);
  preHead.next = head;
  ListNode temp = preHead;
  while (temp != null && temp.next != null) {
     if (temp.next.val == val) {
        temp.next = temp.next.next;
     } else {
        temp = temp.next; //注意点在这，应该是else，我之前写在了外面。
     }

  }
  return preHead.next;
}

   
```

## 206.反转链表 

需要达到熟读背诵的情况。



```java

public static ListNode reverseList(ListNode head) {
    ListNode pre = head;
    ListNode cur = head.next;
    pre.next = null;  //注意点
    ListNode temp = null;
    while (cur != null) {
        temp = cur.next;
        cur.next = pre;
        pre = cur;
        cur = temp;
    }
    return pre;
}

```