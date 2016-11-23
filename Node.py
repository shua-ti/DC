#coding=utf-8
#/usr/bin/env python
"实现映射表类型的节点"
class Node:
    left = None
    right= None
    def __init__(self,key,val):
        self.key = key
        self.val = val
