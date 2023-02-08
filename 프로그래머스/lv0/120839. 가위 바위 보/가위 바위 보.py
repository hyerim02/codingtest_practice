def solution(rsp):
    result={'0':'5','2':'0','5':'2'}
    answer = ''
    for i in rsp:
        answer += result[i]
    return answer