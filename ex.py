fin = open("date.in", "rt")

# a=int(fin.readline()[:-1])
# b=int(fin.readline())

# print(a+b)

# print(sum(list(map(int,fin.readlines()))))
print(sum(list(map(int,fin.read().split(" ")))))

print("ceva")
print("chestie")