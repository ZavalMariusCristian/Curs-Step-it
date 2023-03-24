n=int(input())
D=[str(x) for x in range(0,n,3)]
f=open("date.out","wt")
f.write("\n".join(D))
f.close()