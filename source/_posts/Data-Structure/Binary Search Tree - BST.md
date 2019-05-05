---
abbrlink: 
title: Binary Search Tree
categories: Data Structure
tags: [Data Structure, Tree]
date: 2019-01-01 00:00:00
---

[TOC]
<!-- toc -->

---

> Binary Search Tree
> A data structure created for quick search.

- Definition

- BST (Ordered Binary Tree)
    1. All nodes' value on current nodes' left subtree are smaller than current node's value
    2. All nodes' value on current nodes' right subtree are greater than current node's value
    3. Recursively, both left subtree and right subtree are BST

- Main features
    - Support insert, delete and lookup operation in `O(logn)` time.

## Operation

- Node

    ```java
    public static class Node {
        private int data;
        private Node left;
        private Node right;
 
        public Node(int data) {
            this.data = data;
        }
    } 
    ```

- Find operation
    - T: `O(logn)`

    ```java 
    public Node find(Node root, Node target) {
        return find(root, target.val);
    }

    public Node find(Node root, int data) {
        Node node = root;
        while (node != null) {
            if (data < node.data) {
                node = node.left;
            } else if (data > node.data) {
                node = node.right;
            } else {
                return node;
            }
        }
        return null;
    }
    ```

- Find father node

    ```java
    public Node findFather(Node root, Node target) {
        return findFather(root, target.val);
    }

    public Node findFather(Node root, int data) {
        Node node   = root;
        Node father = null;

        while (node != null) {
            if (node.val == data) 
                return father;

            father = node;
            if (data > node.val) {
                node = node.right;
            } else { // data <= node.val
                node = node.left;
            }
        }
        // Not exist
        return null;
    }
    ```

- Insert operation
    - Usually we insert new data on a leaf node.
    - If new data is bigger than node's data.
        1. The node has no right child, insert to its right child's position. 
        2. Recursively find the position in the node's right subtree.
    - If new data is smaller than node's data, similar to the instructions above.

    ```java
    public void insert(Node root, int data) {
        if (root == null) {
            root = new Node(data);
            return;
        }
        
        Node node = root;
        while (node != null) {
            if (data > node.data) {
                if (node.right == null) {
                    node.right = new Node(data);
                    return;
                }
                node = node.right;
            } else { // data <= node.data
                if (node.left == null) {
                    node.left == new Node(data);
                    return;
                }
                node = node.left;
            }
        }
    }
    ```

- Delete operation
    - 3 situations under consideration
        1. The node to be deleted is a leaf node.
            - Set it as null from its father node.
        2. The node has a child.
            - Replace the node with its child.
        3. The node has two child.
            - Find the min node in its right tree and replace the node with that min node.
            - Delete that min node from its original position.


    ```java
    public void delete(Node root, int data) {
        Node node   = root; 
        Node father = null;

        // Find position
        while (node != null && node.data != data) {
            father = node;
            if (data > node.data) {
                node = node.right;
            } else { // data <= node.data
                node = node.left;
            }
        }
        if (node == null) return; // Not exist

        // Two child
        if (node.left != null && node.right != null) {
            Node minNode = node.right;
            Node minNodeFather = node;
            while (minNode.left != null) {
                minNodeFather = minNode;
                minNode = minNode.left;
            }
            node.data = minNode.data;   // Replace node's data
            node   = minNode;           // Delete minNode
            father = minNodeFather;
        }

        // One child or no child
        Node child = null; // Node's child
        if (node.left != null) {
            child = node.left;
        } else if (node.right != null) {
            child = node.right;
        }

        if (father == null) {
            root = child; // Delete root
        } else if (father.left == node) {
            father.left = child;
        } else { // father.right == node
            father.right = child;
        }
         
    }
    ```

- Find max/min node

    ```java
    public Node findMin(Node root) {
        if (root == null) return null;
        Node node = root;
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }
    ```

    ```java
    public Node findMax(Node root) {
        if (root == null) return null;
        Node node = root;
        while (node.right != null) {
            node = node.right;
        }
        return node;
    }
    ```

- Find predecessor/successor node
    - Predecessor
        1. Find max node of left subtree

            ```
              o(node)
             / \
            o   o
             \
              o(pred)
            ```

        2. Find father node (the node is father's right child)

            ```
             o(pred)
              \
               o(node)
              / \
            null o
            ```

        3. Find left side father node
            
            ```
                 o(pred)
                  \
                   o
                  /
                 o
                /
               o(node)
              / \
            null o
            ```

    ```java
    public Node findPredecessor(Node root, Node target) {
        Node node = find(root, target);
        
        if (node.left != null) return findMax(node.left);

        TreeNode father = findFather(root, node);
        while (father != null && node == father.left) {
            node = father;
            father = findFather(root, node);
            // it would be more easier if there is pointer for father node
        }
        // father == null => not exist or root
        // node   == father.right => father node is the predecessor
        return father;
    }
    ```

    - Successor
        1. Find min node of right subtree

            ```
              o(node)
             / \
            o   o
               /
              o(succ)
            ```

        2. Find father node (the node is father's left child)

            ```
                 o(succ)
                /
               o(node)
              / \
             o   null
            ```

        3. Find right side father node

            ```
              o(pred)
             /
            o
             \
              o
               \
                o(node)
               / \
              o  null
            ```

    ```java
    public Node findSuccessor(Node root, Node target) {
        Node node = find(root, target);
        if (node.right != null) return findMin(node);

        TreeNode father = findFather(node);
        while (father != null && node == father.right) {
            node = father;
            father = findFather(root, node);
        }
        return father;
    }
    ```

## Support duplication

- In practice, the data stored in BST usually is a multi-field object
    - We take one field as the key to build the BST.
    - Other fields are called satellite data.

- What if there are two key that has same value
    1. Use datastructure like linked list and array (support dynamic expansion) to store those objects on the same node.
    2. Inset that object to its right tree. (consider it with a greater key value)
        - For `find()`, we **keep looking up on candidate node's right subtree until we meet a leaf node** so that we find out all the nodes with same key value.
        - For `delete()`, we also need to find out all the nodes with the same key value and delete it one by one.

## Runtime

- Time: `O(logn)`
- Worst: `O(n)`
    - BST deterioratded to an unbalanced binary tree (extreme case a linked list)

- Nodes (assume max layer is `L`)
    - `n >= 1 + 2 + 4 + 8 + ... + 2^(L-2) + 1`
    - `n <= 1 + 2 + 4 + 8 + ... + 2^(L-2) + 2^(L-1)`

- Level
    - `[log2(n+1), log2n + 1]`

---

## Why BST not HashTable

- HashTable have insert/delete/find operation in `O(1)` time
    - But it is not stored in order, we can get an sorted list by inorder traversing the BST in `O(n)` time
    - Capacity expansion is time-consuming for HashTable
    - HashTable's performance is not stable because of hash collision
    - Designing hash function, solving hash collision, capacity expansion and etc. to be considered, while BST just need to solve the balancing problem and it has a mature scheme like red-black tree.

- Choosing the data structure according to the application scene

---

## BST Variants

### Red-black tree 

> Balanced BST

### B+ Tree 

> Support outputing in range


---
