#24. 两两交换链表中的节点，19.删除链表的倒数第N个节点， 链表相交，142.环形链表II

##24. 两两交换链表中的节点

关键是需要操作4个元素，我之前想的是3个元素，然后一直写不出来。

但是本质还是 pre, cur的变种。

```java
public static ListNode swapPairs(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }
    ListNode preHead = new ListNode(0);
    preHead.next = head;
    ListNode pre = preHead;
    ListNode cur = head;
    ListNode next = null;
    int i = 0;
    while (cur.next != null) {
        i++;
        next = cur.next;
        ListNode nextNext = cur.next.next;
        if (i % 2 == 1) { //2怎么丢了？？？
            next.next = cur;
            pre.next = next;
            cur.next = nextNext;
        } else {
            pre = cur;
            cur = next;
        }
    }
    return preHead.next;
}

```
##19.删除链表的倒数第N个节点

这个题绝对做过，关键是找到倒数第n个节点。

```java

public static ListNode removeNthFromEnd(ListNode head, int n) {
    if (head == null) {
        return null;
    }
    if (head.next == null && n == 1) {
        return null;
    }
    ListNode preHead = new ListNode(0);
    preHead.next = head;
    ListNode nHead = preHead;  //------> 这一行才是注意点
    ListNode cur = preHead;    //------> 这一行才是注意点
    for (int i = 0; i < n; i++) {
        if (nHead == null) {
            return preHead.next;
        }
        nHead = nHead.next;
    }
    while (nHead != null && nHead.next != null) {
        nHead = nHead.next;
        cur = cur.next;
    }
    //找到cur就是倒数第n-1个节点。
    //【0】，1，2，3，4，5
    //【0】，1
    //【0】，1，2 ---》 2
    //节点貌似有点问题。
    if (cur != null && cur.next != null) {
        cur.next = cur.next.next;
    }
    return preHead.next;
}
```
##链表相交

记得思路，还是没写出来。最后的终止条件是两个都为null。

```java
public static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    if (headA == null || headB == null) {
        return null;
    }
    if (headA.next == null && headB.next == null) {
        if (headA == headB) return headA;
        return null;
    }
    //题目数据 保证 整个链式结构中不存在环。
    //
    //注意，函数返回结果后，链表必须 保持其原始结构 。
    //你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？

    //1,2,3,4,5
    //2,4,5
    //完全没思路啊
    ListNode curA = headA;
    ListNode curB = headB;
//        while (true) {
//            if (curA == curB) {
//                return curA;
//            }
//            if (curA.next == null) {
//                curA.next = headB;
//            } else {
//                curA = curA.next;
//            }
//            if (curB.next == null) {
//                curB.next = headA;
//            } else {
//                curB = curB.next;
//            }
//        }
    while (curA != curB) {
        if (curA == null) { //----> 必须用这个，不能改变节点的结构。
            curA = headB;   //4,1,6 和 5，1 不算交点，如果没有交点，最后会卡到null，null直接return了。
        } else {            //这一个写代码的时候，死活没想起来。
            curA = curA.next;
        }
        if (curB == null) {
            curB = headA;
        } else {
            curB = curB.next;
        }
    }
    return curA;
}

```
##142.环形链表II

最后运用到了数学知识，好吧，我做过，还是没写出来。

```java
/**
 * 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
 *
 * 不允许修改 链表。
 */
public ListNode detectCycle(ListNode head) {
    if (head == null || head.next == null) {
        return null;
    }
    //快慢指针？？
//        ListNode preHead = new ListNode(0);
//        preHead.next = head;
    // 3,2,0,-4, [2]
    // 1, 2 [1]
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            break;
        }
    }
    fast = head;
    while (slow != fast) {
        slow = slow.next;
        fast = fast.next;
    }
    return fast;
}

```
