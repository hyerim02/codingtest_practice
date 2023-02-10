X=int(input())
N=int(input())
lst=[]
for i in range(N):
    a,b=map(int,input().split())
    X -= a*b
print('No' if X else 'Yes')