T=int(input())
lst=[]
for i in range(T):
    a,b=map(int,input().split())
    lst.append(a+b)
for j in range(T):
    print(lst[j])