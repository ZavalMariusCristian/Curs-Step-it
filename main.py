f=open("my.txt", "rt")
print(f.read())
print(f.read())
f.seek(5)
print(f.tell())
f.seek(f.tell()+3)
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline())
f.seek(0)
print(f.readlines())
f.seek(0)
for l in f:
    print(l)

f2=open("alt.txt", "at")

f2.write("Hi")
f2.write("Hello")
#f2.seek(0)
#f2.write("Am uitat sa pun asta")
f2.writelines("\n".join(["unu","doi"]))
f2.seek(0,2)