#-*-coding=utf-8-*-
#/usr/bin/env python
"寻找序列中k个最小值"

seq = [4,3,2,5,6,3,8,3,6]
#将原序列重新划分
#[lo,pivot,ho]
def partition(seq):
    pivot ,seq = seq[0],seq[1:]
    lo = [x for x in seq if x <= pivot]
    hi = [x for x in seq if x > pivot ]
    return lo,pivot,hi

#将现有的问题一分为二
#根据目标 kth 最小的元素，有选择地处理较小的分支
def selectfun(seq,k):
    lo,pivot,hi = partition(seq)
    pi = [pivot]
    m = len(lo)
    if m==k: return lo
    elif m < k:
        return lo+pi+selectfun(hi,k-m-1)
    else:
        return selectfun(lo,k)
if __name__=="__main__":
    for i in range(1,7):
        print selectfun(seq,i)

