A=[3, 4, 56, 100, 15, 2, 20, 30]
p=1
for a in A:
    if a % 3==0 and a % 5==0:
        p = p * a
    print(p)