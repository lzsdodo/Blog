---
abbrlink: 
title: Hash Table
categories: Data Structure
tags: [Data Structure, HashTable]
date: 2019-01-01 00:00:00
---

[TOC]
<!-- toc -->

---

## Hash function

> Hash table utilize the random access feature of array, so it's kind of extension of array.

- Design hash function
    - `hash(key)` => `index` of the table
    - Requirements for a hash function
        1. The result is always a **non-negative integer**
        2. If `key1 == key2`, then `hash(key1) == hash(key2)`
        3. If `key1 != key2`, then `hash(key1) != hash(key2)`
            - For the 3rd requirement, it's impossible to achieve
            - When `key1 != key2` and `hash(key1) == hash(key2)`, we call it hash collision

- Solve hash collision problem
    - Two ways to solve it
        1. **Open addressing** 开放寻址法
            - Main idea: when detect conflict, we find another available place to insert
                - Linear Probing 线性探测
                    - `hash(key)+0，hash(key)+1，hash(key)+2, ...`
                - Quadratic probing 二次探测
                    - `hash(key)+0，hash(key)+1^2，hash(key)+2^2, ...`
                - Double hashing 双重散列
                    - `hash1(key)，hash2(key)，hash3(key), ...` 
            - The probability of hash collision will increase with the size increasing, so we use **`load factor`** to ensure there are enough space for new elements
                - $load factor = size / capacity$
        2. **Chaining** 链表法
            - Each bucket / slot will point to a linked list
            - We store the elements with same value of `hash(key)` in the linked list
            - Steps to lookup the value
                - Get bucket by `hash(key)`
                - Traverse the linked list `node.key == key` then `return node.val` 
                    - In `O(k)` time, $k = n / m$, `m` is the size of the bucket, `k` is `ideal average length of the linked list` (distributed evenly)

- Pros & Cons
    - Open addressing: Java ThreadLocalMap
        - Pros
            - Easy to serialization
            - Improve lookup performance utilizing the CPU Cache since all stored in an array
        - Cons
            - Complicated to delete elements
            - Higher prive for hash collision
        - When?
            - Small size of data
            - Small load factor
    - Chaining: Java LinkedHashMap
        - Pros
            - Higher tolerance for hash collision
        - Cons
            - Need larger space to store the linkedlist
            - Not friendly to CPU Cache which affects the performance
        - When?
            - Big object and big data size
            - More **flexiable optimization strategy**
                - Use **red-black tree** / **skiplist** instead of linkedlist
                    - Lookup in `O(logk)` time
                    - In the extremely case, there only one bucket, still lookup in O(logn) time

---

## Design a industrial level hash table

> Target
> 1. Avoid sharp drop performance in case of hash collisions
> 2. Resist hash collision attacks

- Requirements
    1. Keep it **simple**
        - Otherwise it will cost too much computing resource
    2. Result should be **random** and **distributed evenly**
    3. Dynamic expansion
        - Set a **threshold value** for the **load factor**
        - Once it hits the threshold, expand the table 
        - Move the elements to the new table 
            - In equalization situation, it's still `O(1)` for insertion
            - But the problem is one-time expansion is time consuming
            - Make it inertia, just create space and move later
        - It's a **trade-off decision** for when to expand the hash table
            - When the RAM is limited, and not require high performance, $load factore >= 1$ is accectable
    4. Dynamic moving
        - Insert one new elem to new table with copying a old one
        - Lookup for new table first than the old table

- Summary
    - What features an industrial level hash table should have
        1. Support quick `lookup/insert/delete` operations
        2. Reasonable RAM usage, do not waste too much space 
        3. Stable performance, even in a extreme situation, the performance should be still acceptable
    - How to design this hash table
        1. Design a proper hash function
        2. Define a proper threshold value for the load factor
        3. Design a proper dynamic expansion strategy
        4. Choose a proper method to solve hash collision problem

---

## Case: **Java HashMap**

- Design
    - Default capacity: `16`
    - Max load factor: `0.75`
    - Expansion: Double the size
    - Use chaining method to solve hash collision
        - It will **TREEFY** to red-black tree when hits the `TREEFY_THRESHOLD = 8`
        - Oppositely, it will **UNTREEFY** to linkedlist hits the `UNTREEFY_THRESHOLD = 6`

        ```java
        // capitity: capitity of the hash table
        int hash(Object key) {
            int h = key.hashCode();
            return (h ^ (h >>> 16)) & (capitity - 1);
        }
        ```

        ```java
        // String's hashCode method
        public int hashCode() {
            int var1 = this.hash;
            if(var1 == 0 && this.value.length > 0) {
                char[] var2 = this.value;
                for(int var3 = 0; var3 < this.value.length; ++var3) {
                    var1 = 31 * var1 + var2[var3];
                }
                this.hash = var1;
            }
            return var1;
        }
        ```

---

## Questions

- Q1
    - Q: 假设我们有 10 万条 URL 访问日志，如何按照访问次数给 URL 排序？
    - Answer
        - 遍历 10 万条数据，以 URL 为 key，访问次数为 value，存入散列表，同时记录下访问次数的最大值 K，时间复杂度 O (N)。
        - 如果 K 不是很大，可以使用桶排序，时间复杂度 O (N)。如果 K 非常大（比如大于 10 万），就使用快速排序，复杂度 O (NlogN)。
- Q2
    - Q: 有两个字符串数组，每个数组大约有 10 万条字符串，如何快速找出两个数组中相同的字符串？
    - Answer
        - 以第一个字符串数组构建散列表，key 为字符串，value 为出现次数。再遍历第二个字符串数组，以字符串为 key 在散列表中查找，如果 value 大于零，说明存在相同字符串。时间复杂度 O (N)。

---

## Reference

- [数据结构与算法之美 18-19](https://time.geekbang.org/column/intro/126)
