def maximum(a,b,c):
    if(a>=b) and (a>=c):
        largest=a
    elif(b>=a and b>=c):
        largest=b
    else:
        largest=c
    return largest
#now
a=3
b=4
c=5
print(maximum(a,b,c))





























