#coding=utf-8
#/usr/bin/env python
"binary search"
seq = [1,2,3,3,5,6,7]

def binsearch(S,x,lo,hi=None):
    if hi==None: hi = len(S)
    while (hi-lo)>1:
        mid = (lo+hi) //2
        if x < S[mid]:hi = mid
        else:lo = mid
    if S[lo]==x:return lo
    else:return -1

#适用于有序向量插入操作子接口
#无论查找是否成功，返回可行的最大位置
def bisect_right(S,x,lo,hi=None):
    if hi==None: hi=len(S)
    while lo < hi:
        mid = (lo+hi)//2
        if x < S[mid]: hi = mid
        else:lo = mid + 1 #lo=mid 会导致死循环
    return lo

def rec_bisect_right(S,x,lo,hi = None):
    if hi==None: hi = len(S)
    if lo < hi:
        mid = (lo+hi) // 2
        if x < S[mid]:
            return rec_bisect_right(S,x,lo,mid)
        else:
            return rec_bisect_right(S,x,mid+1,hi)
    else:
        return lo
if __name__=='__main__':
    print rec_bisect_right(seq,3,0)
