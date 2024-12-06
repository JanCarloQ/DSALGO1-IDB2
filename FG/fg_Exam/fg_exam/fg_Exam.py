#Number 1
print("1.")
x=[1,2,3,4,5]
y=[]
z=[]

z.insert(0,x.pop(0))
z.insert(1,x.pop(0))
z.insert(2,x.pop(0))
y.insert(0,x.pop(0))
y.insert(1,x.pop(0))
print(x)
print(y)
print(z)


#Number 2
print()
print("2.X = [1, 2, 21, 33, 45, 65, 12]")
X = [1, 2, 21, 33, 45, 65, 12]
print()
print("insertion")
for i in range(1,len(X)):
    key=X[i]
    j=i-1
    while j>=0 and key>X[j]:
        X[j+1]=X[j]
        j-=1
    X[j+1]=key
print(X)

print()
print("selection")
for i in range(len(X)):
    mix_idx=i
    for j in range(i+1,len(X)):
        if X[mix_idx]>X[j]:
            mix_idx=j
    X[i],X[mix_idx]=X[mix_idx],X[i]
print(X)


