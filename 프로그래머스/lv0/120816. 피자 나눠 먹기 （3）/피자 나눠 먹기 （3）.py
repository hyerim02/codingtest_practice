def solution(slice, n):
    if slice>n:
        answer=1
    else:
        if n%slice==0:
            answer=n//slice
        if n%slice!=0:
            answer=(n//slice)+1
    return answer