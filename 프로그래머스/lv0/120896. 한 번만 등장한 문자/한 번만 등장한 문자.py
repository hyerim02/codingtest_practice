def solution(s):
    answer = ''
    dict = {}
    for x in s:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    for x in dict:
        if dict[x] == 1:
            answer += x

    return ''.join(map(str, sorted(answer)))