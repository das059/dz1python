A = "asdxfghyxyx"
r=''
for i in range(len(A)):
    if A[i] == 'x':
        r=r+'y'
    else:
        r=r+A[i]
        print(r)