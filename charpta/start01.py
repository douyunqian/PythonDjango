#coding:utf-8

from setuptools import dist,find_packages
a=["a","B","A"]
a.sort()#从小到大
print "%#x"%108

print "MM/DD/YY %02d/%02d/%d"%(1,2,95)
# startswith endswith ,count find
from string import maketrans
a="abcde"
b="12345"
trans=maketrans(a,b)
str = "this is string example....wow!!!"
print str.translate(trans)
a=["a","Python","456"]
a=set(a)
b=set(["a","Python","c"])
print a.symmetric_difference(b)
a={"a":"123"}
a.setdefault("b","456")
print(a)
# Pyhon实现的快速排序算法

a=[4,0,3,-143,5,31,8]
print u"排序前:"
print a

def mkkl(a):
    length=len(a)
    for i in range(0,length-1):
        for j in range(1,length-1):
            if a[i]>a[j]:
                a[j],a[i]=a[i],a[j]







print u"排序后"
mkkl(a)
print a


