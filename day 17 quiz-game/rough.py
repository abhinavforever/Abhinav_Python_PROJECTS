l=[]
for x in range(1,31):
    for y in range(1,31):
        for z in range(1,31):
            if z**2==x**2 + y**2 :
                t=tuple((z,x,y))
                if sorted(t,reverse=True) not in l:
                    l.append(sorted(t,reverse=True))
print(l)