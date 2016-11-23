#coding=utf-8
#/usr/bin/env python
"二分搜索树"
import Node

def insert(node,key,val):
    if node is None:return Node(key,val)
    if node.key == key: node.val = val
    elif key < node.key:
        node.left = insert(node.left,key,val)
    else:
        node.right = insert(node.right,key,val)
    return node

def search(node,key):
    if node is None:raise KeyError
    if node.key == key:return node.val
    elif key < node.key:
        return search(node.left,key)
    else:
        return  search(node.right,key)
