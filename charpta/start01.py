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