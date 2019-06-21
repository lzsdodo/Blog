---
abbrlink: b59a5e11
title: Sorting Algorithm
categories: Algo
tags:
  - Algo
  - Sorting
date: 2019-01-01 00:00:00
---

[TOC]
<!-- toc -->

---

> Sorting Algorithm

|  Sorting Algo  | In-place | Stability | Time Complexity (AVG/BEST/WORST) | Space Complexity |
|:--------------:|:--------:|:---------:|:--------------------------------:|:----------------:|
|   Bubble Sort  |     ✓    |     ✓     |      O(n^2) / O(n) / O(n^2)      |       O(1)       |
| Insertion Sort |     ✓    |     ✓     |      O(n^2) / O(n) / O(n^2)      |       O(1)       |
| Selection Sort |     ✓    |     x     |     O(n^2) / O(n^2) / O(n^2)     |       O(1)       |
|   Merge Sort   |     x    |     ✓     |  O(nlogn) / O(nlogn) / O(nlogn)  |       O(n)       |
|   Quick Sort   |     ✓    |     x     |   O(nlogn) / O(nlogn) / O(n^2)   |       O(1)       |
|   Bucket Sort  |     x    |     ✓     |   O(n + k) / O(n + k) / O(n^2)   |     O(n + k)     |
|  Counting Sort |     x    |     ✓     |  O(n + k) / O(n + k) / O(n + k)  |       O(k)       |
|   Radix Sort   |     x    |     ✓     |       O(nd) / O(nd) / O(nd)      |     O(n + d)     |
|    Heap Sort   |     ✓    |     x     |  O(nlogn) / O(nlogn) / O(nlogn)  |       O(1)       |

## Analysis

1. Performace 执行效率
    - Time Complexity
        - Avg, Best case, Worst case
    - Compare & Swap opreation
        - 交换次数等于逆序度
    - Scale

2. Space Complexity 内存消耗
    > Sorted in place

3. Stability 稳定性
    > 值相等的元素，经过排序后，相等元素之间原有的先后顺序不变。

4. 有序度 & 逆序度
    > 有序度是数组中具有有序关系的元素对的个数。
    > Oredered: n*(n-1)/2 (满有序度)
    > 逆序度 = 满有序度 - 有序度

---

## Sorting Algorithm

- **基于比较排序的算法下界** `O(nlogn)`

    ```
    Q: 已知有数组 [a1, a2, ..., an]，求数组特定的一个排序组合
    A:
        组合数：n!
        断言：ai > aj，可排除一半的情况 => n!/2
        若比较 k 次能得到该特定的排序，求 k。
        => n! / 2^k = 1
        => 2^k = n!
        => k = log(n!) && log(n!) < log(n^n)
        => k ≈ nlog(n)
    ```

### Bubble Sort 冒泡排序

- Features
    1. In place sort
    2. Stability
    3. Best: `O(n)`, Worst: `O(n^2)`

```java
public static int[] bubbleSort(int[] arr) {
    if (arr.length <= 1) return arr;

    for (int i = 0; i < arr.length; i++) {
        boolean swapped = false;

        for (int j = 0; j < arr.length - 1 - i; j++) {
            if (arr[j + 1] < arr[j]) {
                swap(arr, j, j + 1);
                swapped = true;
            }
        }

        if (!swapped) break; // No swap
    }
    return arr;
}
```

### Insertion Sort 插入排序

- Feature
    1. In place sort
    2. Stability
    3. Best: O(n), Worst: O(n^2)

```java
public static int[] insertionSort(int[] arr) {
    if (arr.length <= 1) return arr;

    for (int i = 1; i < arr.length; i++) {
        int val = arr[i];
        int j = i - 1;

        // Find seout where to insert
        for (; j >= 0; j--) {
            if (val < arr[j]) {
                arr[j+1] = arr[j];
            } else break;
        }

        arr[j+1] = val; // Insert
    }
    return arr;
}
```

### Selection Sort

- Feature
    1. In place sort
    2. Non-Stability
    3. Best: O(n), Worst: O(n^2)

```java
public static int[] selectionSort(int[] arr) {
    if (arr.length <= 1) return arr;

    for (int i = 0; i < arr.length - 1; i++) {
        int min = arr[i];
        int minIdx = i;

        for (int j = i + 1; j < arr.length; j++) {
            if (arr[j] < min) {
                min = arr[j];
                minIdxinser = j;
            }
        }
        // Swap
        arr[minIdx] = arr[i];
        arr[i] = min;
    }
    return arr;
}
```

### Merge Sort 归并排序

> Divide and Conquer
> BOTTOM TO TOP

- Features
    1. Not in place sort => space: O(n)
    2. Not-Stability
    3. Time-Avg: O(nlogn)

```java
public static void mergeSort(int[] arr) {
    if (arr.length < 2) return;
    mergeSort(arr, 0, arr.length - 1);
}

public static void mergeSort(int[] arr, int low, int high) {
    if (low < high) {
        int mid = low + ((high - low) >> 1);
        // DaC
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        // Merge
        mergeArr(arr, low, mid, high);
    }
}
```

```java
public static void mergeArr(int[] arr, int low, int mid, int high) {
    int[] sortedArr = new int[high - low + 1];
    int k = 0, idx1 = low, idx2 = mid + 1;

    while (idx1 <= mid && idx2 <= high) {
        if (arr[idx1] < arr[idx2]) {
            sortedArr[k++] = arr[idx1++];
        } else {
            sortedArr[k++] = arr[idx2++];
        }
    }

    while (idx1 <= mid) {
        sortedArr[k++] = arr[idx1++];
    }

    while (idx2 <= high) {
        sortedArr[k++] = arr[idx2++];
    }

    for (int i=low, j=0; i<=high; i++, j++) {
        arr[i] = sortedArr[j];
    }
}
```

### Quick Sort 快速排序

> Divide and Conquer
> TOP to BOTTOM

- Features
    1. In place sort => space: O(1)
    2. Not-Stability
    3. Time-Avg: O(nlogn),
        - Worst: O(n^2) depending on the `pivot` value

- How to optimzie **quick sort**
    - Choose a better **pivot** which can even split the array
        - Pick the median of `arr[low], arr[(low+high)/2], arr[high]` as pivot
        - Randomly pick an element as pivot
        - Many other methods

```java
public static void quickSort(int[] arr) {
    // 1. In place sort, Space: O(1)
    // 2. Not-Stability
    // 3. Time-Avg: O(nlogn), Worst: O(n^2)
    // TOP to BOTTOM
    if (arr.length < 2) return;
    quickSort(arr, 0, arr.length - 1);
}

public static void quickSort(int[] arr, int start, int end) {
    if (start >= end) return;
    
    int divIndex = partition(arr, start, end);
    quickSort(arr, start, divIndex - 1);
    quickSort(arr, divIndex + 1, end);
}
```

```java
public static int partition(int[] arr, int start, int end) {
    int pivot    = arr[end]; // Find pivot
    int divIndex = start;    // Divide index

    for (int i = start; i < end; i++) {
        if (arr[i] < pivot) {
            swap(arr, divIndex, i);
            divIndex++;
        }
    }
    swap(arr, divIndex, end);
    return divIndex;
}

private static void swap(int[] arr, int i, int j) {
    if (i == j) return;
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
```

```java
private static int findPivot(int[] arr, int low, int high) {
    int nMid = arr[low + ((high - low) >> 1)];
    int[] num = new int[]{arr[low], nMid, arr[high]};
    // 3 point median
    if (num[0] > num[1]) swap(num, 0, 1);
    if (num[1] > num[2]) swap(num, 1, 2);
    if (num[0] > num[1]) swap(num, 0, 1);
    return num[1];
}
```

- Typical problem
    - Find kth largest element

        ```java
        public int kthLargestElement(int n, int[] nums) {
            return quickSelect(nums, 0, nums.length - 1, nums.length - n);
        }

        private int quickSelect(int[] nums, int start, int end, int k) {
            if (start == end) return nums[k];

            // choose pivot
            int pivot = nums[start + (end - start) / 2];

            int left = start, right = end;
            while (left <= right) {
                while (left <= right && nums[left] < pivot) {
                    left++;
                }
                while (left <= right && nums[right] > pivot) {
                    right--;
                }
                if (left <= right) {
                    swap(nums, left, right);
                    left++;
                    right--;
                }
            }

            if (k <= right) {
                return quickSelect(nums, start, right, k);
            } else {
                return quickSelect(nums, left, end, k);
            }
        }
        ```

    - Rainbow sort

        ```java
           public void sortColors2(int[] colors, int k) {
                if (colors == null || colors.length == 0) return;
                rainbowSort(colors, 0, colors.length - 1, 1, k);
            }

            private void rainbowSort(int[] colors, int start, int end, 
                                     int colorFrom, int colorTo) {

                if (colorFrom == colorTo) return;
                if (start >= end) return;

                int colorMid = (colorFrom + colorTo) / 2; // like pivot
                int left = start, right = end;
                while (left <= right) {
                    while (left <= right && colors[left] <= colorMid) {
                        left++;
                    }
                    while (left <= right && colors[right] > colorMid) {
                        right--;
                    }
                    if (left <= right) {
                        swap(colors, left, right);
                        left++;
                        right--;
                    }
                }
                // Attention to the bound, left side include colorMid
                rainbowSort(colors, start, right, colorFrom, colorMid);
                rainbowSort(colors, left, end, colorMid + 1, colorTo);
            }
        ```


### Bucket Sort

- Analysis
    - Assume there are m buckets, each bucket has $k = n / m$ elements
    - Use quick sort in each bucket in O(klogk) time
    - Total in $O(m * klogk) = O(nlogk)$ time
    - When $m ≈ n$, which means k is really small => $O(nlogk) ≈ O(n)$

- Suitable for big data, when we can not load all the data in RAM at the same time (外部排序)

- Case
    - Question
        - 有 10GB 的订单数据，我们希望按订单金额（假设金额都是正整数）进行排序，但是我们的内存有限，只有几百 MB，没办法一次性把 10GB 的数据都加载到内存中。这个时候该怎么办呢？
    - Answer
        1. 先扫描一遍文件，看订单金额所处的数据范围。
        2. 将所有订单根据金额划分到 100 个桶。
        3. 理想的情况下，如果订单金额均匀分布，那订单会被均匀划分到 100 个文件中，每个小文件中存储大约 100 MB。
        4. 将这 100 个小文件依次放到内存中，用快排来排序。
        5. 所有文件都排好序之后，我们只需要按照文件编号，从小到大依次读取每个小文件中的订单数据，并将其写入到一个文件中。

### Counting Sort

- Analysis
    - It's like a special case of bucket sort.
    - 计数排序只能用在数据范围不大的场景中，如果数据范围 k 比要排序的数据 n 大很多，就不适合用计数排序了。
    - 而且，计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。

```
Data range: [0, 9]
Input data: [1, 4, 1, 2, 7, 5, 2]

1) Take a count array to store the count of each unique object.
Index: 0  1  2  3  4  5  6  7  8  9
Count: 0  2  2  0  1  1  0  1  0  0

2) Add prefix sum
Index: 0  1  2  3  4  5  6  7  8  9
Count: 0  2  4  4  5  6  6  7  7  7

3) Output each object from the input sequence followed by
  decreasing its count by 1.
Process the input data: [1, 4, 1, 2, 7, 5, 2].
Index: 0  1  2  3  4  5  6  7  8  9
Count: 0  2  4  4  5  6  6  7  7  7
// [->1, 4, 1, 2, 7, 5, 2]
Count: 0  2-1 4  4  5  6  6  7  7  7
Index: 0  1   2  3  4  5  6
Data:  -  *1  -  -  -  -  -
// [1, ->4, 1, 2, 7, 5, 2]
Count: 0  1  4  4  5-1 6  6  7  7  7
Index: 0  1  2  3  4   5  6
Data:  -  1  -  -  *4  -  -
// [1, 4, ->1, 2, 7, 5, 2]
Index: 0  1   2  3  4  5  6
Count: 0  1-1 4  4  4  6  6  7  7  7
Data:  *1 1   -  -  4  -  -
// ...
```

```java
// 计数排序，a 是数组，n 是数组大小。假设数组中存储的都是非负整数。
public void countingSort(int[] a, int n) {
  if (n <= 1) return;

  // 查找数组中数据的范围
  int max = a[0];
  // 遍历数组的所有的元素，找到最大的元素
  for (int i = 1; i < n; ++i) {
     // 若后面的元素大于指定的数组元素，则把元素进行交换
     if (max < a[i]) max = a[i];
  }

  // 申请一个计数数组 c，下标大小 [0,max]
  int[] c = new int[max + 1];
  for (int i = 0; i <= max; ++i) {
    c[i] = 0;
  }

  // 计算每个元素的个数，放入 c 中
  for (int i = 0; i < n; ++i) {
    c[a[i]]++;
  }

  // 依次累加
  for (int i = 1; i <= max; ++i) {
    c[i] = c[i-1] + c[i];
  }

  // 临时数组 r，存储排序之后的结果
  int[] r = new int[n];
  // 计算排序的关键步骤，有点难理解
  for (int i = n - 1; i >= 0; --i) {
    int index = c[a[i]]-1;
    r[index] = a[i];
    c[a[i]]--;
  }

  // 将结果拷贝给 a 数组
  for (int i = 0; i < n; ++i) {
    a[i] = r[i];
  }
}
```

### Radix Sort

- ![Radix Sort](https://img.zsliang.me/cs/algo/sorting/radix-sort.gif)

- Analysis
    - 基数排序对要排序的数据是有要求的，需要可以分割出独立的 "位" 来比较，而且位之间有递进的关系，如果 a 数据的高位比 b 数据大，那剩下的低位就不用比较了。
    - 除此之外，每一位的数据范围不能太大，要可以用线性排序算法来排序，否则，基数排序的时间复杂度就无法做到 O (n) 了。

- Case
    - Question
        - 如何根据年龄给 100 万用户排序？(Like sorting 1 million phone number)
    - Answer
        - Make it all the username or uid the same length
            - (ban, candy, john, ...) => (ban00, candy, john0)
            - '0' < any letter in ASCII value
        - Radix sort (Assume the size of username or uid is smaller than 20)
            - Time complexity is similar to O(n)

### Timsort
> Timsort is a **hybrid stable sorting algorithm**, derived from **merge sort** and **insertion sort**, designed to perform well on many kinds of real-world data.

- Using neat merge method
    1. 找出左分区最后一个元素 (最大) 及在右分区的位置
    2. 找出右分区第一个元素 (最小) 及在左分区的位置
    3. 仅对这两个位置之间的元素进行合并，之外的元素本身就是有序的

### Heap sort

> See data structure "heap"

---

## Optimization

- Choose the sorting algo according to the data size
    - When the element is less than **5**, it will sorted by **insertion sort**
        - When O(nlogn) is actually calculated as $f(n) = knlogn + c$, it may bigger than $f(n) = n ^ 2$
        - Like $n = 100$, $k = 1000$, $c = 200$
        - So for a small size of data, algorithm with `O(n^2)` maybe a better choice
    - When the capacity is small, like **1k, 2k**, ... we can choose **merge sort**

- Case
    - Java 1.8
        - [0, 47]: **Selection sort**
        - [47, 286]: **Quick sort** (Dual Pivot Quick Sort)
        - [286, ...]: **Timsort** (merge sort)
        - For some basic type like `byte, char, short`: **Counting sort**
    - Google v8 quick sort
        - [10, 1000]: choose `arr[mid]` as pivot
        - [1000, ...]: Pick an elements from every 200 elements and choose the median as pivot.
        - Split in 3 part: `[<pivot], [=pivot], [>pivot]`
    - Glibc qsort()
        - [0, 4]: **Insertion sort**
        - Small size: **Merge sort**
        - Large size: **Quick sort**
        - Implement a stack on heap in case of stack overflow

---

## Other case

- Case 1
    - Question
        - 现在你有 10 个接口访问日志文件，每个日志文件大小约 300MB，每个文件里的日志都是按照时间戳从小到大排序的。你希望将这 10 个较小的日志文件，合并为 1 个日志文件，合并之后的日志仍然按照时间戳从小到大排列。如果处理上述排序任务的机器内存只有 1GB，你有什么好的解决思路，能 "快速" 地将这 10 个日志文件合并吗？
    - Answer
        - 维持一个按时间戳排序的 Min Heap。
        - 依次读取日志文件并放入 Min Heap 中。
        - 同时从 Min Heap 取出最早的日志存到合并文件中。

---

## Reference

- [数据结构与算法之美 11-14](https://time.geekbang.org/column/intro/126)
- [排序算法](https://mp.weixin.qq.com/s/pgPfAYbD-itnCeMTSXHueQ)
- [Counting Sort | GeeksforGeeks - YouTube](https://www.youtube.com/watch?v=7zuGmKfUt7s&feature=youtu.be)
