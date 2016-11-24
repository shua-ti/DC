#coding=utf-8
#/usr/bin/env python
"搜索树定义"
from search_tree import *
class Tree:
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root,key,val)
    def __getitem__(self, key):
        return search(self.root,key)
    def __contains__(self, key):
        try: search(self.root,key)
        except KeyError:return False
        return True