lis = [1,2,3,"xyz",{"1":"2"},(1,2,3)]
print(lis)
for i in lis:
    if isinstance(i , dict):
        print("Yes it is dict")
    print(i)

tup = (1,2,{"a":"b"},"xyz00",[1,2,3])
print(tup)
for j in tup:
    print(j)

set = {1,2,"xzt"}
# print(set)

try:
    print(10 / 0)
except Exception as e:
    print('error accoured is ',e)
finally :
    print("This is final bloack")


tup2 = (1,2,[1,2,3],"xyz")
a , b , c ,d = tup2
print(c)

val = {}
k = ord("a")
for i in tup2:
    val[chr(k)]=i
    k+=1
print(val)