n = int(input())
str = list(input())
answer = 0 
M=1234567891
for i in range(n): 
    answer += ((ord(str[i]) - 96) * (31 ** i))
print(answer % M)
