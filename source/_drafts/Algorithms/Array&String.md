---
title: Array & String
categories: Algorithms
tags: [Two Pointer, KMP, BM]
date: {{ date }}
updated: {{ date }}
---

# Array & String
---

## Two Pointer



## **BM** - Boyer-Moore Algorithm

> The Boyer-Moore algorithm is considered as **the most efficient string-matching algorithm** in usual applications.
> A simplified version of it or the entire algorithm is often implemented in text editors for the **«search»** and **«substitute»** commands.

- Time (Text/Haystack (`n`), Pattern/Needle (`m`))
    - Preprocessing: `O(m+σ)`;
    - Searching: `O(mn)`;
    - Best: `O(n/m)`

- It uses **two precomputed functions** to shift the window to the right.
    1. **good-suffix shift (or matching shift)** 
        ![bm1](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/21372498.jpg)
        ![bm2](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/77131328.jpg)
    
    2. **bad-character shift (or occurrence shift)**
        ![bm3](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/69786964.jpg)
        ![bm4](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/46309067.jpg)

- Code in Paper    
    ![algo-1](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/27315401.jpg)
    ![algo-2](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/52203052.jpg)
    ![algo-3](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/98296025.jpg)

- Example

    ```java
    bmBadChar[];
    bmGoodSuff[];
    ```

- Reference
    - [Original Paper](https://www.cs.utexas.edu/~moore/publications/fstrpos.pdf)
    - [New Variation Paper](https://www.cs.utexas.edu/~moore/publications/sustik-moore.pdf)
    - [Boyer-Moore algorithm](http://www-igm.univ-mlv.fr/~lecroq/string/node14.html#SECTION00140)
    - [字符串匹配的 Boyer-Moore 算法 / 阮一峰](http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)


## **KMP** - Knuth-Morris-Pratt Algorithms

- ![KMP](http://7xqccv.com1.z0.glb.clouddn.com//18-7-7/37376383.jpg)

- Refeerence
    - [Matrix67: The Aha Moments - KMP 算法详解](http://www.matrix67.com/blog/archives/115)
