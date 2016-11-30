#coding=utf-8
#/usr/bin/env python
"找出平面的最近点对"

S=[(1,2),(3,4),(-2,3),(3,6),(4,5)]

def divide_conquer(s):
    length = len(s)
    left = s[0:length//2];right = s[length//2:]#根据x坐标将输入集合分成left/right
    mid = (left[-1][0]+right[0][0])/2.0#中间分割线

    if len(left) > 2:   lmin = divide_conquer(left)    #左侧部分最近点对
    else:   lmin = left
    if len(right) > 2:   rmin = divide_conquer(right)   #右侧部分最近点对
    else:   rmin = right

    if lmin.__len__() ==2: dis_l = get_distance(lmin)
    else: dis_l = float("inf")
    if rmin.__len__() ==2: dis_2 = get_distance(rmin)
    else: dis_2 = float("inf")

    d = min(dis_l, dis_2)   #最近点对距离

    mid_mins=[]
    for i in left:       #[mid-d,mid+d]
        if mid-i[0]<=d :   #如果左侧部分与中间线的距离<=d
            for j in right:
                if j[0]-mid <=d and abs(i[1]-j[1])<=d:     #如果右侧部分点在i点的(d,2d)之间
                    if get_distance((i,j))<=d: mid_mins.append([i,j])  #ij两点的间距若小于d则加入队列
    if mid_mins:
        dic=[]
        for mid_min in mid_mins:
            dic.append({get_distance(mid_min):mid_min})
        dic.sort(key=lambda x: x.keys())      #根据距离排序
        return (dic[0].values())[0]
    elif dis_l>dis_2:
        return rmin
    else:
        return lmin


# 求点对的距离
def get_distance(min):
    return (min[0][0]-min[1][0])**2 + (min[0][1]-min[1][1])**2

def nearest_dot(S):
    S = sorted(S,key=lambda x:x[0])#输入点集合按照x坐标排序
    nearest_dots=divide_conquer(S)
    print "最近点对"+str(nearest_dots[0])+"--->"+str(nearest_dots[1])

if __name__=="__main__":
    nearest_dot(S)