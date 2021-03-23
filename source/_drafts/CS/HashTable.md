---
abbrlink:
title: HashTable
categories: nil
tags: [nil]
date: 2019-01-01 00:00:00
---

## Table of Content
<!-- toc -->

---

## Set/Map and HashTable

- Hash Table
    - Key -> Hash Function -> Table -> Value
    - 系统是否可以提供若干个较小的连续空间，而每个空间又能存放一定数量的记录

## Hash Function

> Like classifing different categories

- Hash Function Requirement
    - Hash function should return an unsigned integer.
    - if `key1 == key2`, then `hash(key1) == hash(key2)`
    - if `key1 != key2`, then `hash(key1) != hash(key2)`

- MOD
    - Coherence Theorem (同余定理) is like Classification
    - 将任意长度的输入，通过哈希算法，压缩为某一固定长度的输出
    - `f(x) = x mod size`
        - Optim - improve the randomness by adding salt: `f(x) = (x + salt) mod size`

- Collision
    - Table -> Linked List -> Value

## Example

- In Java
    - default size=16
    - default 0.75 * capacity -> expension
