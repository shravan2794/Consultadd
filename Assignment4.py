"""
1)
s="1234khaskha"
c=s[::-1]
print(c)
"""
"""
2)
def koi(txt):
    total=0
    count=0
    for i in txt:
        if i.isupper():
            total=total+1
        else:
            count=count+1
    print("The total number of upper case letters are %s" %total)
    print("The total number of upper case letters are %s" %count)
koi('kjhGGG')
"""
"""
3)
def uniq(lst):
    y=[]
    for x in lst:
        if x not in y:
            y.append(x)
    return y
print(uniq([1,2,3,3,4,5,5,5,6,6]))
"""
"""
5)
def cap(s):
    x=s.upper()
    
    return x
print(cap("The koi jsg"))
"""
"""
6)
def sop(x,y):
    a=int(x)
    b=int(y)
    c=a+b
    return c
print(sop('2','3'))
"""
"""
7)
def kop(x,y):
     if len(x)>len(y):
         return x
     else:
         return y
print(kop('kha ksha','kjsadhjk skajdhjka'))
"""
"""
9)
def lim(limit):
    i=0
    while i<limit+1:
        if i%2==0:
            print (i,'EVEN')
            i=i+1
        else:
            print (i,"ODD")
            i=i+1
(lim(7))
"""
x=range(0,21)
def fill(x):
    if x%2==0:
        return True
    else:
        return False

y=list(filter(fill,x))
print(y)







