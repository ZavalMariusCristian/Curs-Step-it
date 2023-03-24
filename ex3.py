nume = input("Nume fisier:")
fin=open(nume,"rt")
nrs = list(map(int,fin.readlines()))
print(nrs)

divs=[]

for x in nrs:
    div=[]
    for d in range(1, x+1):
        if x%d==0:
            div.append(d)
    divs.append(div)

print(divs)
for l in divs:
    l=list(map(str,l))
    fout=open("res/divs {}".format(l[-1]), "wt")
    fout.write("\n".join(l))
    fout.close()