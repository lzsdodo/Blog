# Link List 链表
---

## Datastructure

- Sequential storage structure 顺序存储结构
- Linked Storage Structure 链式存储结构

## Properties



## Structure

- 单向链表

    ```java
    class ListNode {
        int val;
        ListNode next;

        ListNode(int val) { this.val = val; }
    }
    ```

- 双向链表

    ```java
    class DListNode {
        int val;
        DListNode prev, next;
        
        DListNode(int val) {
            this.val = val;
            this.prev = this.next = null;
        }
    }
    ```

## Basic func

- Reverse a Linked List


- Find the Middle Point

    ```java
    public ListNode findMiddle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
    ```

- Find the Nth Element

    ```java
    public ListNode findNthElem(ListNode head) {
        ListNode fast = head;
        for (int i = 0; i < n - 1; i++) {
            fast = fast.next;
            if (fast == null) {
                return null;
            }
        }
    }
    ```

- Dummy Node

    ```java
    ListNode dummy = new ListNode(Integer.MIN_VALUE);
    ListNode current = dummy;
    ...
    while (current != null) {
        ...
        current.next = blahblahblah;
        ...
        current = current.next;
    }
    ...
    return dummy.next;
    ```

- Merge Two Sorted Lists

```java
public ListNode mergeTwoLinkedLists(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0);
    ListNode lastNode = dummy;

    while (l1 != null && l2 != null) {
        if (l1.val < l2.val) {
            lastNode.next = l1;
            l1 = l1.next;
        } else {
            lastNode.next = l2;
            l2 = l2.next;
        }
        lastNode = lastNode.next;
    }

    if (l1 != null) {
        lastNode.next = l1;
    } else {
        lastNode.next = l2;
    }

    return dummy.next;
}
```

- Linked List Has Cycle

    ```java
    public Boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode fast, slow;
        fast = head.next;
        slow = head;
        while (fast != slow) {
            if(fast==null || fast.next==null)
                return false;
            fast = fast.next.next;
            slow = slow.next;
        }
        return true;
    }
    ```
