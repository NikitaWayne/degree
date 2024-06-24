def degree(a,n):
    if n==1:
        return a
    elif n%2==1:
        return degree(a,n-1)*a
    else:
        r=degree(a,n//2)
        return r*r

a=int(input())
n=int(input())
print(degree(a,n))
