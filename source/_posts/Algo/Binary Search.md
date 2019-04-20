---
abbrlink: cf581b8c
title: Binary Search Algorithm
categories: Algo
tags: 
  - Algo
  - Binary Search
date: 2019-01-01 00:00:00
---

[TOC]

---

> Binary Search

> Although the first binary search algorithm appeared in 1946, the first completely correct binary search algorithm was not implemented until 1962. - Donald E.Knuth

---

## Analyse

- Time
    - Avg: `O(logn)`
    - Worst: `O(logn)`
    - Best: `O(1)`

- Space
    - Recursion: `O(logn)`
    - Iteration: `O(1)`

- Attention
    - Stop condition 
    - How to update lower & upper bound (`low` & `high`)
    - How to choose the return value (`mid`)

---

## Restriction

1. Sorted/Ordered 单调递增或递减
2. Bounded 存在上下界
3. Accessible by index 可通过索引访问
    - Fit for array not linked list
4. Not suitable for dataset which is too small or too big 
    - Too small, the performance is similar
    - Too big, the data is not stored consequently

---

## Implementation

- Iteration

    ```java
    public static int bsearch(int[] arr, int data) {
        return bsearch(arr, 0, arr.length-1, data)
    }

    public static int bsearch(int[] arr, int start, int end, int data){
        int low = start, high = end;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] < data) {
                low  = mid + 1;
            } else if (arr[mid] > data) {
                high = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
    ```

- Recursion

    ```java
    public static int bsearch(int[] arr, int start, int end, int data){
        if (start > end) return -1;

        int mid = start + (end - start) / 2;

        if (arr[mid] > target)
            return bsearch(arr, start, mid - 1, data);

        if (arr[mid] < target)
            return bsearch(arr, mid + 1, end, data);
        
        return mid;  
    }
    ```

---

## Variants

1. Find the first target

    ```java
    public static int findFirstTarget(int[] arr, int start, int end, int data) {
        int low = start, high = end;

        while (low <= high) {
            int mid = low + ((high - low) >> 1);

            if (arr[mid] > data) {
                high = mid - 1;
            } else if (arr[mid] < data) {
                low  = mid + 1;
            } else {
                // Equal, first of arr || first of repeated target
                if ((mid == start) || (arr[mid - 1] != data))
                    return mid;
                high = mid - 1;
            }
        }
        return -1;
    }
    ```

2. Find the last target

    ```java
    public static int findLastTarget(int[] arr, int start, int end, int data) {
        int low = start, high = end;

        while (low <= high) {
            int mid = low + ((high - low) >> 1);

            if (arr[mid] > data) {
                high = mid - 1;
            } else if (arr[mid] < data) {
                low  = mid + 1;
            } else {
                // Equal, last of arr || last of repeated target
                if ((mid == end) || (arr[mid + 1] != data))
                    return mid;
                low = mid + 1;
            }
        }
        return -1;
    }
    ```
    
3. Find the first number bigger than `>= target`

    ```java
    public static int findFirstBigger(int[] arr, int start, int end, int data) {
        int low = start, high = end;

        while (low <= high) {
            int mid = low + ((high - low) >> 1);

            if (arr[mid] >= data) {
                // >=, first of arr || first elem bigger than target
                if((mid == start) || (arr[mid - 1] < data))
                    return mid;
                high = mid - 1;
            } else {
                low  = mid + 1;
            }
        }
        return -1;
    }
    ```

4. Find the last number smaller than `<= data`

    ```java
    public static int findLastSmaller(int[] arr, int start, int end, int data) {
        int low = start, high = end;

        while (low <= high) {
            int mid = low + ((high - low) >> 1);

            if (arr[mid] <= data) {
                // >=, end of arr || last elem smaller than target
                if ((mid == end) || (arr[mid + 1] > data))
                    return mid;
                low  = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
    ```

## Skip List

> Reform linked list in order to support binary search, which is **skip list**. (跳表)
> It's a outstanding dynamic data structure. (Sometime Red-black tree can replaced by skip list)
> Sorted Set in Redis is implemented with skip list and hashmap.

- What is skip list
    - Linked list with multi-level indice.

- How many indice do we need
    - Given a linked list with size n.
    - Number of indice nodes at level `k` is `#: n / 2^k`
    - Assume there `h` level, $h = log2n - 1$
        - When `maxLevel = 1`, it's just a simple linked list

- Time complexity
    - Assume we need to traverse m nodes at each index layer
    - `O(mlogn)` and `max(m) = 3` => `O(logn)`

- Space complexity
    - Indice nodes number: $n/2 + n/4 + ... + 4 + 2 = n - 2$
    - `O(n)`
    - In order to reduce the size, we can add a index node every 3 or 5 nodes rather than 2 nodes. ($n/3 + n/9 + ... + 9 + 3 + 1 ≈ n/2 = O(n)$)
    - But considering the nodes are just pointers, we don't need to store the object itself, so in many cases we can just ignore the this extra space.

- Operation
    - `Insert` / `Delete` / `Search` in `O(logn)`
    - Maintain index
        - When insert an new element, add a new index through a random function
    - `Search in range` (which is better than Red-black tree)
    - [Ref Code](https://github.com/wangzheng0822/algo/blob/master/java/17_skiplist/SkipList.java)

- Summary
    - 跳表是一种动态数据结构，支持快速的插入、删除、查找操作，时间复杂度都是 O (logn)。
    - 跳表的实现非常灵活，可以通过改变索引构建策略，有效平衡执行效率和内存消耗。
    - 跳表使用空间换时间的设计思路，通过构建多级索引来提高查询的效率，实现了基于链表的 "二分查找"。
    - 虽然跳表的代码实现并不简单，但是作为一种动态数据结构，比起红黑树来说，实现要简单多了。

## View

- 凡是用二分查找能解决的，绝大部分我们更倾向于用散列表或者二叉查找树。
- 二分查找更适合用在 "近似" 查找问题。

## Question

- Q1: 假设我们有 1000 万个整数数据，每个数据占 8 个字节，如何设计数据结构和算法，快速判断某个整数是否出现在这 1000 万数据中？我们希望这个功能不要占用太多的内存空间，最多不要超过 100MB，你会怎么做呢？
    - Answer
        - 最简单的办法就是将数据存储在数组中，内存占用差不多是 80MB，符合内存的限制。
            - 先排序，再查找。
        - 大部分情况下，用二分查找可以解决的问题，用散列表、二叉树都可以解决。
            - 不管是散列表还是二叉树，都会需要比较多的额外的内存空间。
            - 如果用散列表或者二叉树来存储这 1000 万的数据，用 100MB 的内存肯定是存不下的。

- Q2: 假设我们有 12 万条这样的 IP 区间与归属地的对应关系，如何快速定位出一个 IP 地址的归属地呢？
    - Answer
        - 如果 IP 区间与归属地的对应关系不经常更新，我们可以先预处理这 12 万条数据，让其按照起始 IP 从小到大排序。
        - 如何来排序呢？我们知道，IP 地址可以转化为 32 位的整型数。
        - 所以，我们可以将起始地址，按照对应的整型值的大小关系，从小到大进行排序。
        - 要查询某个 IP 归属地时，我们可以先通过二分查找，找到最后一个起始 IP 小于等于这个 IP 的 IP 区间。
        - 然后，检查这个 IP 是否在这个 IP 区间内，如果在，我们就取出对应的归属地显示；如果不在，就返回未查找到。

## Reference

- [数据结构与算法之美 15-17](https://time.geekbang.org/column/intro/126)
- [Leetcode Binary Search 知识点总结](https://blog.csdn.net/tinkle181129/article/details/80037111)
