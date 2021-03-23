---
abbrlink: b8827cf7
title: Mining XMR
categories: Cryptocurrency
tags: [XMR, Mining]
date: 2018-06-20 00:00:00
---

## Table of Content
<!-- toc -->

---

> **Mining XMR**

## Dependencies

- Ubuntu

    ```sh
    sudo apt -y install libmicrohttpd-dev libssl-dev cmake build-essential libhwloc-dev
    ```

- CentOS

    ```sh
    sudo yum -y install centos-release-scl epel-release
    sudo yum -y install cmake3 devtoolset-4-gcc* hwloc-devel libmicrohttpd-devel openssl-devel make
    scl enable devtoolset-4 bash
    ```

- MacOS

    ```sh
    brew install hwloc libmicrohttpd gcc openssl cmake
    # For NVIDIA GPUs
    brew cask install nvidia-cuda
    ```

## Download xmr-stak

- Find the latest releases and precompiled binaries on GitHub under [release](https://github.com/fireice-uk/xmr-stak/releases)

    ```bash
    wget https://github.com/fireice-uk/xmr-stak/archive/2.4.5.tar.gz
    ```

## Edit the default donation

```bash
vi ./xmrstak/donate-level.hpp
# Default: 2.0 / 100.0 = 2%
constexpr double fDevDonationLevel = yourDonatedRate / 100.0;
```

## Compile

> More details on official repo's [doc](https://github.com/fireice-uk/xmr-stak/tree/master/doc)

- Ubuntu

    ```sh
    git clone https://github.com/fireice-uk/xmr-stak.git
    mkdir xmr-stak/build
    cd xmr-stak/build
    cmake ..
    make install
    ```

- CentOS

    ```sh
    git clone https://github.com/fireice-uk/xmr-stak.git
    mkdir xmr-stak/build
    cd xmr-stak/build
    cmake3 ..
    make install
    ```

- MacOS
    - CMake options
        - For NVIDIA GPUs: `-DOpenCL_ENABLE=OFF`
        - For AMD GPUs: `-DCUDA_ENABLE=OFF -DOpenCL_ENABLE=ON`
        - For CPU-only: `-DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF`

    ```sh
    cmake . -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl <options>
    cmake . -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=ON
    ```

## Start the miner

```sh
chmod +x ./xmr-stak
./xmr-stak
```

## Mining pool

> [mineXMR](https://www.minexmr.com/)

- Connection
    - Choose server
        - Ping each connection to choose the fastest server
        - Canada `ca.minexmr.com` is the fastest server in my test

    - Mining ports
        - `4444`, `5555` for `Low range CPU/GPU` with starting difficulty `15000`
        - `7777`, `80` & `443` for `Mid range CPU/GPU` with starting difficulty `35000`
        - `6666` for `SSL port` with starting difficulty `35000`
        - `3333` for `Modern High End` with starting difficulty `1000000`


## Reference

- [XMR-Stak](https://github.com/fireice-uk/xmr-stak)

