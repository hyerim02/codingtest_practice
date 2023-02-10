def solution(order):
    answer=sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
    return answer