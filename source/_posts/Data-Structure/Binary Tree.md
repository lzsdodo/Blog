---
abbrlink: e0e2589a
title: Binary Tree
categories: Data Structure
tags:
  - Data Structure
  - Tree
date: 2019-01-01 00:00:00
---

## Table of Content
<!-- toc -->

---

## Definition

- Binary Tree
    - Each node has only two childs

    ```java
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
    ```

- Classic structure
    - **BST**
    - **Red-black tree**
    - **Heap**

### Traversing binary tree

- We can traverse a tree recursively to retrieve all the data in **pre-order**, **in-order** or **post-order**
    - Pre-order: `root-left-right`
    - In-order: `left-root-right`
        - We will get an ordered list after **in-order traversing a BST**
    - Post-order: `left-right-root`

- Recursive traversal solution

    ```java
    /* Preorder Traversal - Recursive Solution*/
    public void preorder(TreeNode root, ArrayList<Integer> result) {
        if (root != null) return null;
        result.add(root.val);           // visit the root
        preorder(root.left, result);    // traverse left subtree
        preorder(root.right, result);   // traverse right subtree
    }
    ```

    ```java
    /* Inorder Traversal - Recursive Solution*/
    public void inorder(TreeNode root, ArrayList<Integer> result) {
        if (root != null) return null;
        inorder(root.left, result);
        result.add(root.val);
        inorder(root.right, result);
    }
    ```

    ```java
    /* Postorder Traversal - Recursive Solution*/
    public void postorder(TreeNode root, ArrayList<Integer> result) {
        if (root != null) return null;
        postorder(root.left, result);
        postorder(root.right, result);
        result.add(root.val);
    }
    ```

- Iterative traversal solution

    ```java
    // Preorder Traversal - Iterative Solution
    public List<Integer> preorder(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        if (root == null) return ret;

        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);

        TreeNode node;
        while (!stack.empty()) {
            node = stack.pop();
            // root -> left -> right
            ret.add(node.val);
            if (node.right != null) stack.push(node.right);
            if (node.left != null)  stack.push(node.left);
        }
        return answer;
    }
    ```

    ```java
    // Inorder
    // Left -> Root -> Right (Stack, FILO)
    if (node.right != null) stack.push(node.right);
    ret.add(node.val);
    if (node.left != null)  stack.push(node.left);
    ```

- DaC perspective

    ```java
    // Thought: Divide and Conquer
    public ArrayList<Integer> dacTraversal(TreeNode root) {
        if (root != null) return null;
        ArrayList<Integer> ret = new ArrayList<Integer>();
        // Divide
        ArrayList<Integer> left = dacTraversal(root.left);
        ArrayList<Integer> right = dacTraversal(root.right);
        // Conquer (adjust the order here)
        // Pre-order: ret.add(root.val); ret.addAll(left);  ret.addAll(right);
        // In-order
        ret.addAll(left);  ret.add(root.val); ret.addAll(right);
        // Post-order: ret.addAll(left);  ret.addAll(right); ret.add(root.val);
        return ret;
    }
    ```

### Complexity Analysis

- Complexity
    - T: `O(n)`
        - Because we visit each node exactly once.
    - S: `O(n)` / `O(1)`
        - Taking system stack into consideration
        - Worst case, $level = size$

- To be cautious
    - When the depth of tree is too large, we might suffer from stack overflow problem, and the depth of the tree might be N in the worst case.
        - That's one of the main reasons why we want to solve this problem iteratively sometimes.
    - And the complexity might be different due to a different implementation.

---

### Construct Binary Tree

- From Inorder and Preorder Traversal

    ```
    preorder: [root, [left-subtree], [right-subtree]]
    inorder:  [[left-subtree], root, [right-subtree]]
    ```

    ```java
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTree(preorder, inorder, 0, inorder.length - 1, 0);
    }

    private TreeNode buildTree(int[] preorder, int[] inorder,
                               int iS, int iE, int pS) {
        if(iS > iE)  return null;
        if(iS == iE) return new TreeNode(inorder[iS]);

        // This part can be optim by using HashMap
        int iRoot = iS;
        for(int i = iS; i <= iE; i++) {
            if(inorder[i] == preorder[pS]) {
                iRoot = i;
                break;
            }
        }

        TreeNode root = new TreeNode(inorder[iRoot]);
        root.left = buildTree(preorder, inorder, iS, iRoot - 1, pS + 1);
        root.right = buildTree(preorder, inorder, iRoot + 1, iE, pS + (iRoot - iS) + 1);

        return root;
    }
    ```

- From Inorder and Postorder Traversal

    ```
    postorder: [[left-subtree], [right-subtree], root]
    inorder:   [[left-subtree], root, [right-subtree]]
    ```

    ```java
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return buildTree(inorder, postorder, 0, inorder.length - 1, postorder.length - 1);
    }

    private TreeNode buildTree(int[] inorder, int[] postorder,
                               int iS, int iE, int pE) {
        if(iS > iE)  return null;
        if(iS == iE) return new TreeNode(inorder[iS]);

        // This part can be optim by using HashMap
        int iRoot = iS;
        for(int i = iS; i <= iE; i++) {
            if(inorder[i] == postorder[pE]) {
                iRoot = i;
                break;
            }
        }

        TreeNode root = new TreeNode(inorder[iRoot]);
        root.left = buildTree(inorder, postorder, iS, iRoot - 1, pE - (iE - iRoot) - 1);
        root.right = buildTree(inorder, postorder, iRoot + 1, iE, pE - 1);

        return root;
    }
    ```
