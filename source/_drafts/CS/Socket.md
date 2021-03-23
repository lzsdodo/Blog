---
abbrlink:
title: Socket
categories: CS
tags: [Socket]
date: 2019-01-01 00:00:00
---

## Table of Content
<!-- toc -->

---

> What is a socket?
> To the kernel, a socket is an endpoint of communication
> To an application, a socket is a file descriptor that lets the application read/write from/to the network
> > All Unix I/O devices, including networks, are modeled as files.

- Two types of socket
    - Based on file system
        - `_fd file descriptor`
    - Based on network
        - `protocol, IP, port`

- Usually `C/S` model
    - Client
        - `New Socket()`, `Connect()`, `Recv()/Send()`, `Close()`
        - Status: `established`, `syn_send`
    - Server
        - `New Socket()`, `Bind()`, `Listen()`, `Accept()`, `Recv()/Send()`, `Close()`
        - Status: `established`, `syn_rcvd`
    - 3 time shake
        - Connecting: C: `SYN`; S: `SYN+ACK`; C: `ACK`;
        - Closing: C: `FIN`; S: `ACK`; S: `FIN`; C: `ACK`;

- Each socket maintaining 2 queue
    - A queue of connected client which is at the

- Communication between 2 process
    - We need to find out the other process
        - In local ENV, we we use PID because it's unique in local ENV.
        - In network, we know IP is unique for an host, and TCP protocol can find out the unique process for this host with its port.
        > `IP:PORT` (Contains 2 protocol: TCP/IP)

![](https://pic2.zhimg.com/v2-c397b75852db5484b834239709eca8d7_r.jpg)


- 内核中，Socket 是一个文件，那对应就有文件描述符。
- 每一个进程都有一个数据结构 task_struct，里面指向一个文件描述符数组，来列出这个进程打开的所有文件的文件描述符。
- 文件描述符是一个整数，是这个数组的下标。
- 数组中的内容是一个指针，指向内核中所有打开的文件的列表。
- 既然是一个文件，就会有一个 inode，只不过 Socket 对应的 inode 不像真正的文件系统一样，保存在硬盘上的，而是在内存中的。
    - Diff from `fd`
- 在这个 inode 中，指向了 Socket 在内核中的 Socket 结构。
