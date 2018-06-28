# Binary Search
---

## Analyse

- Time
    - Avg: `O(logn)`
    - Worst: `O(logn)`
    - Best: `O(1)`

- Space
    - Recursion: `O(logn)`
    - Iteration: `O(1)`

## Code

- Recursion

    ```java
    public static int binarySearch(int[] arr, int start, int end, int target){
        if (start > end) 
            return -1;

        int mid = start + (end - start) / 2;

        if (arr[mid] > target)
            return binarySearch(arr, start, mid - 1, target);

        if (arr[mid] < target)
            return binarySearch(arr, mid + 1, end, target);
        
        return mid;  
    }
    ```

- Iteration

    ```java
    public static int binarySearch(int[] arr, int start, int target){
        int left = start;
        int right = arr.length - 1;
        int mid = 0;

        while (left < right) {
            mid = left + (right - left) / 2;
            if (arr[mid] < target) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }
    ```

## Questions

- [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)
- [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/)
- [668. Kth Smallest Number in Multiplication Table](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/)

## Reference

- [Leetcode Binary Search 知识点总结](https://blog.csdn.net/tinkle181129/article/details/80037111)
