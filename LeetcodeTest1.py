#寻找长度最小的子数组
def mini1(nums,s):
    l=len(nums)
    left=0
    right=0
    min_left=float('inf')
    #print(min_left)
    sum=0
    while right<l:
        sum=sum+nums[right]
        while sum>=s:
            min_left=min(min_left,right-left+1)           
            sum=sum-nums[left]
            #print(sum)
            left=left+1
            

        right=right+1

    return min_left if min_left!=float('inf') else 0


nums=[12,28,83,4,25,26,25,2,25,25,25,12]
n1=mini1(nums,213)
print(n1)
print('---------------------')

#求旋转矩阵
def xuanzhuan(n):
    #创建一个n*n的矩阵
    res=[[0]*n for _ in range(n)]
    print(res)
    num=1
    left=0
    right=n-1
    top=0
    bottom=n-1

    while top <=bottom and left<=right:
        for i in range(left,right+1):
            res[top][i]=num
            num=num+1
        top=top+1

        for i in range(top,bottom+1):
            res[i][right]=num
            num=num+1
        right=right-1

        for i in range(right,left-1,-1):
            res[bottom][i]=num
            num=num+1
        bottom=bottom-1

        for i in range(bottom,top-1,-1):
            res[i][left]=num
            num=num+1
        left=left+1

    return res


n=xuanzhuan(4)
print(n)
print('---------------------')

#输入输出求区间和
def areasum():
    N=input()
    N=int(N)
    #创建长度为n1的list
    A=[0]*N
    print(A)
    for i in range(len(A)):
        n0=input()
        n0=int(n0)
        A[i]=n0
    print('Finish')
    #一次输入两个数怎么写
    l,r=input().split(' ')
    l, r = int(l), int(r)  # 将 l 和 r 转换为整数
    sum=0
    while l<=r:
        sum=sum+A[l]
        l=l+1
    print(sum)

   

#areasum()
print('---------------------')

h=float('inf')
t=min(h,2)
print(t)#2,inf为什么小于一个数
print('---------------------')
#区间商问题，有n*m的矩阵，垂切割一刀或者横切一刀，分成两部分，价值差最小
def area():
    n,m=input().split()
    n,m=int(n),int(m)
    A=[[0]*m for _ in range(n)]
    print(A,A[0][1])
    sum_l=0
    sum_h=0
    sum=0
    suml=[]
    sumh=[]
    data=input().split()
    for i in range(n*m):
        data[i]=int(data[i])
    num=0
    print(data)

    for i in range(n):
        for j in range(m):
            A[i][j]=data[num]
            sum_h=sum_h+A[i][j]
            sum=sum+A[i][j]
            num=num+1
            
        sumh.append(sum_h)
        sum_h=0

    for j in range(m):
        for i in range(n):
            sum_l=sum_l+A[i][j]
        suml.append(sum_l)
        sum_l=0

    print(A)
    print(suml)
    print(sumh)
    print(sum)

    result=float('inf')
    lcut=0
    ln=0
    for i in range(m):
        lcut=lcut+suml[i]
        ln=result
        result=min(result,abs(sum-2*lcut))
        if ln!=result:
            print('ln:',ln)
            print('result:',result)
            print(i)

    hcut=0
    hn=0
    for i in range(n):
        hcut=hcut+sumh[i]
        hn=result
        result=min(result,abs(sum-2*hcut))
        if hn!=result:
            print('hn:',hn)
            print('result:',result)
            print(i)
        
    print(result)
#area()
print('---------------------')
'''数组是存放在连续内存空间上的相同类型数据的集合。
数组下标都是从0开始的。
数组内存空间的地址是连续的
因为数组在内存空间的地址是连续的，所以我们在删除或者增添元素的时候，就难免要移动其他元素的地址。

'''
t=[[1,2,3,4,5],[6,7,8,9,10]]
print(id(t[0][1]),id(t[0][2]))#地址差32，因为int型数据占4个字节，32位
print(id(t[0][4]),id(t[1][0]))#地址连续
del t[1]
print(id(t[0][1]),id(t[0][2]))#删除元素后，后面的元素地址会发生变化,后面元素的地址会向前移动
print(t)
