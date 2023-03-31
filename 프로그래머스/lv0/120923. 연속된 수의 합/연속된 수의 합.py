def solution(num, total):
    answer = []
    d = sum(range(num))
    start = (total - d)//num
    answer = [i for i in range(start, start+num)]
    return answer