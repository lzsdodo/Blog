---
abbrlink: e0e2589a
title: Binary Tree
categories: Data Structure
tags: [Data Structure, Tree]
date: 2019-01-01 00:00:00
---

[TOC]
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

- Application
    - **BST**, **Red-black tree**
    - **Heap**

### Traversing binary tree

- 3 types
    - Pre-order: `root-left-right`
    - In-order: `left-root-right`
        - We will get an ordered list after **inorder traversing a BST**
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
        ArrayList<Integer> result = new ArrayList<Integer>();
        // Divide
        ArrayList<Integer> left = dacTraversal(root.left);
        ArrayList<Integer> right = dacTraversal(root.right);
        // Conquer (adjust the order here)
        // result.add(root.val); result.addAll(left);  result.addAll(right); // preorder
        result.addAll(left);  result.add(root.val); result.addAll(right); // inorder
        // result.addAll(left);  result.addAll(right); result.add(root.val); // postorder
        return result;
    }
    ```

### Complexity Analysis

- Complexity
    - T: `O(n)`
        - Because we visit each node exactly once.
    - S: `O(n)`
        - Taking system stack into consideration
        - Worst case, $level = size$

- To be cautious
    - When the depth of tree is too large, we might suffer from stack overflow problem

