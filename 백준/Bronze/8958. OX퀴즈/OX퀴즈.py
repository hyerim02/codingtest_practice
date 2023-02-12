n = int(input()) 
for _ in range(n):
    a = input() 
    score = 0 
    cnt = 0 
    for i in range(len(a)):
        if a[i] == 'O': 
            cnt += 1 
            score += cnt 
        if a[i] == 'X':
            cnt = 0
    print(score)