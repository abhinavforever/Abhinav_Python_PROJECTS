# # print("Total=%4d,votes=%45.1f"%(480,7.2))
# # print("{0:124.10s}".format("Code Tantra"),end=" ")
# # print("a")
# # l=[]
# # print(type(l))
# # print(type({}))
# # print(type(set()))
# # print(type(()))
# # print(type(3))
# # print(type(3.4))
# # print(type(-3))
# # print(type(True))
# #
# # a=[1,2,3]
# # b=a
# # a[0]='a'
# # print(b)
# #
# # l=[None,"we"]
# # l2=[0,1]
# # print(all(l),all(l2))
# # print(any(l),any(l2))
# #
# # l=[1,2,"r"]
# # l2=[]
# # print(all(l),all(l2))
# #
# # l=[1,4,89,5]
# # l2=l.sort(reverse=True)
# # print(l)#None is o/p cuz return type of .sort function is None.It just sorts the mutable iterables
# # l2=sorted(l)#doesn't sort the list but returns a sorted list
# # print(l2)
# # print(l)
# #
# # print(l.__sizeof__())
# #
# # set1={1,2,3,4,5,6,7,8,9,10}
# # set2={2,3,4,6,8,10}
# # print(set1.difference(set2))
# # set1.difference_update(set2)
# # print(set1)
# #
# # set1={1,2,3}
# # set2=set1
# # set1.clear()
# # print(set2)
#
# l=[1,2,3,['f','u','n']]
# l[1]=4 # reassign an item
# l[3][0]='p' #change the items
# l.append([1,2,5]) #add items
# l.extend("fire")
# l.remove('i')
# print(l)
#
# s1={1,2,3}
# s2={4,5,6}
# s1.add(1)
# # s1.add(s2) gives error TypeError:unhashable type : 'set' since a set is mutable so we can't add mutable items to a set since items of a set are immutable
# s1.add(('w','e'))
# s1.remove(2)
# print(s1)
#
# t=tuple()
# t=({1:2,'a':3})
# print(t)
#
# l=['we',1]
# print(l)
#
# # octal to decimal using int()
# print("int() on 0o12 =", int('012'))#default base=10
#
# # binary to decimal using int()
# print("int() on 0b110 =", int('0b110',2))
#
# # hexa-decimal to decimal using int()
# print("int() on 0x1A =", int('0x1A',16))
#
# print(hex(10))
#
# print(complex(1,3))
#
# l1=[1,2]
# l2=['one','two']
# d=zip(l1,l2)
# print(dict(d))
#
# print(1,2,3,sep="",end='')
# print(1,2,3,sep=" ",end='\t\t')
# print(1,2,3,sep=" ",end="")
# print()
#
# a=3.5
# b=a
# print(a is b)
# a=5
# print(b)
#
# l1=[1,2,3]
# l2=l1
# print(l2 is not l1)
# l2.remove(2)
# print(l1)
#
# print(5 and 0.0)
#
# l1=[1,2,3]
# t=set(l1,l)
# print(t)

s=input("str: ")
l=[int(i) for i in s if i.isdigit()==True]
print(l)

d={}
for i in l:
    if i not in d.keys():
        c=l.count(i)
        d[i]=c
for k,v in d.items():
    print(f"{k} \t {v}")