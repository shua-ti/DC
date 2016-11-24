#coding=utf-8
#/usr/bin/env python
"二分搜索树"
import Node

#插入操作
#键值已经存在，更新原有的值
#键值不存在，增加新的节点
#返回当前节点
def insert(node,key,val):
    if node is None:return Node(key,val)
    if node.key == key: node.val = val
    elif key < node.key:
        node.left = insert(node.left,key,val)
    else:
        node.right = insert(node.right,key,val)
    return node


#递归描述
#每次经过两次比较进入对应的分支
def search(node,key):
    if node is None:raise KeyError #叶节点的分支，抛异常
    if node.key == key:return node.val #返回对应的值
    elif key < node.key:  #左分支
        return search(node.left,key)
    else:                 #右分支
        return  search(node.right,key)
