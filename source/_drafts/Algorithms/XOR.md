# XOR 异或
---

## Define
> Exclusive Or.

- Symbol
    - `XOR / EOR / ⊕ / ^`
    
- Operation

    ```
    1 ⊕ 1 = 0;  0 ⊕ 0 = 0;
    1 ⊕ 0 = 1;  0 ⊕ 1 = 1;
    ```

## Properties

1. `A ⊕ B = B ⊕ A`
2. `(A ⊕ B) ⊕ C = A ⊕ (B ⊕ C)`
3. `A ⊕ A = 0`, `A ⊕ 0 = A`
4. `A ⊕ B ⊕ B = A ⊕ 0 = A`

## Usage

- Turn over bits 翻转特定位
    - `11110001 ^ 00000001 = 11110000`

- Parity Check 奇偶检验

- 校验和恢复
    - IF `a ^ b = c` THEN `a ^ c = b`

- Compare 2 number if they are equal
    - `a ^ b == 0` is more effient than `a - b == 0`

- Exchange 2 variable without intermediate variable. 交换两个变量的值，不允许使用中间变量。

    ```
    a = a ^ b;
    b = a ^ b;  // (a ^ b) ^ b = a ^ (b ^ b) = a ^ 0 = a;
    a = a ^ b;  // (a ^ b) ^ (a ^ b ^ b) = a ^ b ^ a = b
    ```

- Put 1-1000 in an array with 1001 elem. Only one elem is repeated. Findout the repeated elem.
    1. SUM: `x = sum(all) - sum(1~1000)`;
    2. XOR: `(1^2^...^1000^x) ^ (1^2^...^1000)= x`

- Extended: Except 2 numbers appear once, all the other appear twice. Findout these 2 number.
    1. XOR ALL: `res1 = a ^ z = (a^b^b^...^y^y^z)`
    2. XOR ALL specific bit is 1: Because `a is not z` => `a ^ z != 00000000`; Assume that `a ^ z = 10010110`; Then we can XOR all the number which is `res2 = (1xxxxxx^...) ^ a ^ z` => we get one of `a` or `z`: `res2 = a / z`;
    3. XOR Again: `res1 ^ res2 = z / a`
    4. Loop 2 times: O(N); Space: O(1);
