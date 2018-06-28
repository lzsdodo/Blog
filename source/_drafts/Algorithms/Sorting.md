# Sorting
---

## Summary

![主流排序算法概览](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/91637844.jpg)

## Algorithms

- Bubble Sort 冒泡排序
    - ![Bubble Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/94466382.jpg)

    ```java
    public static void bubbleSort(int[] arr) {
        int i, temp, len = arr.length;
        boolean changed;
        do {
            changed = false;
            len--;
            for (i = 0; i < len; i++) {
                if (arr[i] > arr[i + 1]) {
                    temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    changed = true;
                }
            }
        } while (changed);
      }
    ```

- Heap Sort 堆排序
    - ![Heap Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/14144240.jpg)

- Insertion Sort 插入排序
    - ![Insertion Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/82724373.jpg)

    ```java
    public static void insertion_sort(int[] arr){
        for( int i=0; i<arr.length-1; i++ ) {   
            for( int j=i+1; j>0; j-- ) {
                if( arr[j-1] <= arr[j] )
                    break;
                int temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
        }
    }
    ```

- Merge Sort 归并排序
    - Divide and Conquer
    - ![Merge Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/84336698.jpg)
    - ![mergesort](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)
    

    ```java
    public static void merge_sort_recursive(int[] arr, int[] result, int start, int end) {
        if (start >= end)
            return;

        int len = end - start, mid = (len >> 1) + start;
        int start1 = start, end1 = mid;
        int start2 = mid + 1, end2 = end;
        merge_sort_recursive(arr, result, start1, end1);
        merge_sort_recursive(arr, result, start2, end2);
        
        int k = start;
        while (start1 <= end1 && start2 <= end2)
            result[k++] = arr[start1] < arr[start2] ? arr[start1++] : arr[start2++];
        while (start1 <= end1)
            result[k++] = arr[start1++];
        while (start2 <= end2)
            result[k++] = arr[start2++];
        for (k = start; k <= end; k++)
            arr[k] = result[k];
    }

    public static void merge_sort(int[] arr) {
        int len = arr.length;
        int[] result = new int[len];
        merge_sort_recursive(arr, result, 0, len - 1);
    }
    ```

- Quick Sort 快速排序
    - Divide and Conquer
    - ![Quick Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/65401276.jpg)

    ```java
    public static void qSort(int[] arr, int head, int tail) {
        if (head >= tail || arr == null || arr.length <= 1)
            return;

        int i = head, j = tail, pivot = arr[(head + tail) / 2];
        
        while (i <= j) {
            while (arr[i] < pivot) {
                ++i;
            }
            while (arr[j] > pivot) {
                --j;
            }
            if (i < j) {
                int t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
                ++i;
                --j;
            } else if (i == j) {
                ++i;
            }
        }

        qSort(arr, head, j);
        qSort(arr, i, tail);
    }
    ```

- SelectSort
    - ![Selection Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/42060807.jpg)

- Other Sort
    - ![Counting Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/65456307.jpg)
    - ![Radix Sort](http://7xqccv.com1.z0.glb.clouddn.com//18-6-21/95335203.jpg)

## Reference

- [排序算法](https://mp.weixin.qq.com/s/pgPfAYbD-itnCeMTSXHueQ)
