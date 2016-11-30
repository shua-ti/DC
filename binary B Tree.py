#-*-coding=utf-8-*-
#/usr/bin/env python
"树的平衡和再平衡"

import Node
def skew(node):
    if None in [node,node.left]:return node
    if node.lvl != node.left.lvl: return node
    left = node.left
    node.left = left.right
    left.right = node
    return left

def split(node):
    if None in [node,node.right,node.right.right]: return node
    if node.right.right.lvl != node.lvl: return node
    right = node.right
    node.right = right.left
    right.left = node
    right.lvl +=1
    return right

def insert(node,key,val):
    if node is None: return Node(key,val)#生成新的节点
    if node.key == key:node.val = val#节点存在更新值
    elif key < node.key:
        node.left = insert(node.left,key,val)#添加叶节点，叶节点的层次为1
    else:
        node.right = insert(node.right,key,val)
    node = skew(node)#递归性回溯部分执行
    node = split(node)
    return node
