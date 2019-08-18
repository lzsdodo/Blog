---
abbrlink: c096a6bd
title: Manacher's Algorithm
categories: Algo
tags: 
  - Algo
  - Palindrome
date: 2019-01-01 00:00:00
---

[TOC]
<!-- toc -->

---

> Manacher's Algorithm
> Find longest palindromic substring

---

## Implementation

1. Preprocess

    - e.g. transform s into t

        ```
        e.g. "ababa"
        ->   s:   a b a b a
        ->   t: ^~a~b~a~b~a~$

        e.g. "abba"
        ->   s:   a b b a
        ->   t: ^~a~b~b~a~$

        -> len = 2 * n + 3
        ```

    - code

        ```java
        private char[] preProcess(String s) {
            char[] chars = new char[s.length() * 2 + 3];
            Arrays.fill(chars, '~');
            int i = 2;
            for(char c : s.toCharArray()) {
                chars[i] = c;
                i += 2;
            }
            chars[0] = '^';
            chars[chars.length - 1] = '$';
            return chars;
        }
        ```

2. Palindrome Radius 回文半径

    > `pr[i]`

    - e.g.

        ```
        e.g.: "abaaba" -> "^~a~b~a~a~b~a~$"
                    a   b   a   a   b   a
                ^ ~ a ~ b ~ a ~ a ~ b ~ a ~ $
        index: [0 1 2 3 4 5 6 7 8 9 . . . . .]
        pr[i]: [1 1 2 1 4 1 2 7 2 1 4 1 2 1 1]
        
        -> i = 7, pr[7] represents: s: ~a~b~a ~ a~b~a~
                                    i: 1, .., 7, .., 13
           len radius = pr[i] - 1 = 6:         "a~b~a~"
        -> Palindrome String 回文串: s: [i - (pr[i] - 1), i + (pr[i] - 1)]
                                       [1, 13] -> "~a~b~a~a~b~a~"
        ```

    - Map to original string

        ```
        e.g.: "assa" -> "...~a~s~s~a~..." 
                     ->         i
                     -> "assa" + "~~~~" + "~"

        e.g.: "asa"  -> "...~a~s~a~..." 
                     ->        i
                     -> "asa" + "~~~" + "~"

        -> pr[i] = (char + "~") * 2 + "~" 
        -> left  = (i - (pr[i] - 1)) / 2 = (i + 1 - pr[i]) / 2;
        -> right = left + pr[i] - 1;
        ```

3. Calculate `pr[i]`

    > This is the core part of the manacher's algorithm

    - e.g.

        ```
                  r      j           c           i      r
            ...---|------|-----------|-----------|------|---...
                       pr[j]'
                    |----|----|             |----|----|
                |--------|--------|     |--------|--------|    
                       pr[j]
                  |------------------|-----------|------|
                                                  r - i
            -> init: pr[i] = min(pr[j], r - i)
            -> expand: pr[i]
        ```

    - code

        ```java
        int index = 0, maxPR = 1;
        int r = 0, c = 0; // r: right most radius; c: center;
        for(int i = 1; i < n; i++) {
            // init pr[i]
            if(r > i) {
                int j = 2 * c - i; // mirror
                pr[i] = Math.min(pr[j], r - i);
            }
            // attempt to expand palindrome centered at i
            while(chars[i - pr[i]] == chars[i + pr[i]]) {
                pr[i]++;
            }
            // update center & radius
            if(i + pr[i] > r) {
                r = i + pr[i];
                c = i;
            }
            // update longest palindromic substring
            if(maxPR < pr[i]) {
                maxPR = pr[i];
                index = i;
            }
        }
        ```

---

## Complexity

- Time: `O(n)`
    - Description
        - If `pr[i] ≤ r – i`, we set `pr[i]` to `pr[i']` which takes exactly 1 step.
        - Otherwise we attempt to change the palindrome’s center to i by expanding it starting at the right edge, `r`.
        - Extending `r` (the inner while loop) takes at most a total of `n` steps, and positioning and testing each centers take a total of `n` steps too.
        - Therefore, this algorithm guarantees to finish in at most `2*n` steps, giving a linear time solution.
    
    - Calculate by upper bound and lower bound
        - Worst case: characters are all the same `"aaa"`
            - Each character will be accessed **5 times** in each for loop
        - Best case: characters are all the distinct `"abc"`
            - Each character will be accessed **4 times** in each for loop
        - `O(n) <= T(worst) <= T(avg) <= T(best) = O(n)`

    - Mathematical formula
        - Assume character `i` compare $f(i)$ times, and the current position `r` is $(r)_{i-1}$. So the new position of `r` is $(r)_{i}$ after comparison.
        - Equation
            1. Situation 1: $i > r_{i-1}$: $f(i) = r_{i} - i$
            2. Situation 2: $i \leq r_{i-1}$: $f(i) = r_{i} - r_{i-1}$ / $0$ 
            3. Total times: $f = \sum_{0}^{n-1} f(i) \leq \sum_{0}^{n-1} r_{i} - r_{i-1} = O(n)$

- Space: `O(n)` for `pr[]` array

---

## Code

- [LeetCode 0005. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

    ```java
    class LongestPalindromicSubstring {

        public String longestPalindrome(String s) {
            if(s == null || s.length() == 0) return s;

            char[] chars = preprocess(s);
            int[] pr = new int[chars.length];
            Arrays.fill(pr, 1);

            int index = 0, maxPR = 0;
            int c = 0, r = 0;
            for(int i = 1; i < chars.length - 1; i++) {
                // init pr[i]
                if(r > i) {
                    pr[i] = Math.min(pr[2 * c - i], r - i);
                }
                // attempt to expand palindrome centered at i
                while(chars[i - pr[i]] == chars[i + pr[i]]) {
                    pr[i]++;
                }
                // update center & radius
                if(i + pr[i] > r) {
                    r = i + pr[i];
                    c = i;
                }
                // update longest palindromic substring
                if(maxPR < pr[i]) {
                    maxPR = pr[i];
                    index = i;
                }
            }
            // map to the original string
            int left = (index + 1 - maxPR) / 2;
            int right = left + maxPR - 1;
            return s.substring(left, right);
        }

        private char[] preprocess(String s) {
            char[] chars = new char[s.length() * 2 + 3];
            Arrays.fill(chars, '~');
            int i = 2;
            for(char c : s.toCharArray()) {
                chars[i] = c;
                i += 2;
            }
            chars[0] = '^';
            chars[chars.length - 1] = '$';
            return chars;
        }
    }
    ```
