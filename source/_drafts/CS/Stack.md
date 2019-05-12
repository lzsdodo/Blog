---
abbrlink: 
title: Stack
categories: nil
tags: [nil]
date: 2019-01-01 00:00:00
---

[TOC]
<!-- toc -->

---

# Data Structure - Stack 

## Achieved an Array based Stack

- Main methods
    - push
    - pop
    - top
    - isEmpty

# Call Stack 调用栈

> 表示函数或子例程像堆积木一样存放，以实现层层调用。
> 程序运行的时候，总是先完成最上层的调用，然后将它的值返回到下一层调用，直至完成整个调用栈，返回最后的结果。

```
main()
# Program start
```

```
Class()
main()
# Calling Constructor
```

```
method()
Class()
main()
# Calling instance method
```

# RAM Area 内存区域

> 存放数据的一种内存区域
> 一般来说，系统会划分出两种不同的内存空间：
> Stack 栈 & Heap 堆

- Diff 
    - Structure
        - Stack 是有结构的，每个区块按照一定次序存放，可以明确知道每个区块的大小；
        - Heap 是没有结构的，数据可以任意存放。
        * => Stack 内变量的分配速度会比 Heap 快，Heap 内分配需要调用 malloc
        * => Stack 的寻址也会比 Heap 快，通过 sp/fp 寄存器间接寻址
    - Size
        - Init stack 时 size 是确定的，数据超出范围，就会发生溢出 stack overflow
        - Heap 的 size 是不确定的，可以按需增加
        * => size(stack) << size(heap)
        * => 数据存放的规则是：只要是局部的、占用空间确定的数据，一般都存放在 stack 里面，否则就放在 heap 里面。
    - Data
        - 栈存放的内容，函数返回地址、相关参数、局部变量和寄存器内容等。
    - Release (操作系统对进程占用的内存空间的两种管理方式)
        - function{...release(stack)}
        - Heap 人工释放 malloc()/free()；若程序员不释放，程序结束时由 OS 回收。
    - Others
        - RAM Address: Stack (h->l) vs. Heap (l->h)
        - 每个线程分配一个 Stack，每个进程分配一个 Heap
        - 分配效率不同，hardware optim for stack (specific register)
        * => Stack 线程独占，Heap 线程共用

- Example 
    
    ```java
    public void Main() {
        int val = 4;
        Class cls = new Class();
    }
    // Main() 结束，会清空 Stack
    // 但 Heap 的 cls obj 继续存在，直到 garbage collector 回收这部分内存
    // 一般来说，内存泄漏都发生在 heap，即某些内存空间不再被使用了，却因为种种原因，没有被系统回收。
    ```

    ```
    # Stack
    ...
    ...
    cls(ref)
    val
    ```

    ```
    # Heap
    cls obj
    ...
    ```
