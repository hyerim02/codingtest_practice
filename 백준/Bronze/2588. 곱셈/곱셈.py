a=int(input())
b=input()
for i in range(0,len(b)):
    print(a*int(b[len(b)-1-i])) 
print(a*int(b))    