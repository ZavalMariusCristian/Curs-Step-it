a=68916

inv = list(str(a))
inv.sort()
inv=int("".join(inv))
print(a-inv)

print(a-int("".join(sorted(list(str(a))))))

L=[10, 15, 40, 3]

C=[list(str(x)) for x in L ]

C=[]
for x in L:
    C.extend(list(str(x)))
C=list(set(C))
C.sort()
C=[int(x) for x in C]
C=list(map(int, C))
print(C)

def sumStrList(LC):
    return sum([int(x) for x in LC])

a=98102819
aC=list(str(a))
sP=(sum(list(map(int, aC[::2]))))
sI=(sum([int(x) for x in aC[1::2]]))
print(sP*sI)
