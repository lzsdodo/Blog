---
abbrlink: 
title: Concurrency
categories: CS
tags: [Concurrency]
date: 2019-04-23 12:00:00
---

> Concurrency

[TOC]
<!-- toc -->

---

> Concurrency is not Parallelism. - [Go Concurrency Patterns, Google IO 2012](https://talks.golang.org/2012/concurrency.slide#1)

## Problem

> [The C10K problem](http://www.kegel.com/c10k.html#top): Handling 10,000 clients simultaneously through a single server.

> CPU operation is more faster than I/O operation, so **I/O strategies** is important in the same hardware condition.

### I/O

### Process, Thread & Coroutine

---

## Concurrent Model

### Thread & Lock

### Actor Model

> One ant is no ant, one actor is no actor.

- Actor is the basic unit, and actors do not share memory.
- Message is the only communication approach.
- Actor is like a mailbox handler, handling different type of mail.

- Actor's feature
    - Each actor has a mailbox
    - Actor handle the mail sequentially
    - The message in actor is unmutable

- Actor hase to implement 3 basic part
    - Processing
    - Storage
        - Mailbox (messageQueue)
    - Communication

- The Actor Model
    - Everything is an actor
    - An actor has a mailbox, which is also an actor and needs a mailbox
    - Axioms
        1. Create more actors
        2. Send messages to actors that it has addresses before
        3. Designate what to do with the next message
    - Conceptually 1 message at a time.
    - Message can **be dilivered at most one time** in **arbitrary order**
    - Address != Identity
        - Many-to-many relationship among actors and addresses
    - No channel, they go directly

- Akka
    - The underlying layer is still using the synchronization mechanism of Java and JVM
    - It does not use any lock mechanism which means it will not appear deadlock
    - The processing of concurrent execution does not use thread switching (improve thread efficiency and reduce the cost of switching thread)
    - Provides a higher level of concurrent abstract models

### CSP Model

> CSP: Golang ([src/runtime/chan.go](https://golang.org/src/runtime/chan.go) which is also ref to [Libtask: a Coroutine Library for C and Unix](https://swtch.com/libtask/))

---

## Reference

- [Wiki - Concurrency](https://en.wikipedia.org/wiki/Concurrency_control)
- [Lock](https://en.wikipedia.org/wiki/Lock_%28computer_science%29)
- [Wiki Actor Model](https://en.wikipedia.org/wiki/Actor_model)
- [Youtube: The Actor Model](https://www.youtube.com/watch?v=7erJ1DV_Tlo)
- [Java/Scala - Akka](https://akka.io/)
- [Akka series demo](https://github.com/godpan/akka-demo)
- [Wiki CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes)
- [并发模型之间的比较 知乎](https://zhuanlan.zhihu.com/p/44917920)

