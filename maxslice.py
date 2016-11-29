#-*-coding=utf-8-*-
#/usr/bin/env python
"寻找最大切片"

seq =[1,2,3,-3,-4,23,45,-34]

def maxSlice(seq,lo=0,hi=None):
    if hi==None: hi=len(seq)
    mid = (lo+hi)//2
    if mid-lo >1: gap_left=maxSlice(seq,lo,mid)#区间表示左闭右开
    else:gap_left=(lo,mid)
    if hi-mid >1: gap_right=maxSlice(seq,mid,hi)
    else:gap_right=(mid,hi)
    s1 = sum(seq[gap_left[0]:gap_left[1]]);s2=sum(seq[gap_right[0]:gap_right[1]])
    s = max(s1,s2)
    leftsums = [sum(seq[i:mid]) for i in range(lo,mid)]
    rightsums =[sum(seq[mid:j]) for j in range(mid+1,hi+1)]
    cross = []
    for i in range(lo,mid):
        for j in range(mid+1,hi+1):
            ss = leftsums[i-lo]+rightsums[j-mid-1]
            if ss > s:
                cross.append({ss:(i,j)})
    if cross:
        cross.sort(key=lambda x:x.keys())
        return (cross[-1].values())[0]
    elif s1>s2:
        return gap_left
    else:
        return gap_right


if __name__=="__main__":
    interval = maxSlice(seq)
    slice = seq[interval[0]:interval[1]]
    print "slice is: " ,slice
    print "sum is:  " ,sum(slice)