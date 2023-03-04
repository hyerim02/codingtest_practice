def solution(score):
    answer = []
    li=[]
    for i in score:
        li.append(sum(i)/len(i))
    sort_li=sorted(li,reverse=True)
    for i in li:
        answer.append(sort_li.index(i)+1)
    return answer