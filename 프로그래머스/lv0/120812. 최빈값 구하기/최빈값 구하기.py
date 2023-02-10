def solution(array):
    s=set(array)
    dic={}
    for i in s:
        dic[i]=array.count(i)
    dic=sorted(dic.items(),key=lambda x:-x[1])
    if len(dic)>1:
        if dic[0][1]!=dic[1][1]:
            return dic[0][0]
        else:
            return -1
    else:
        return dic[0][0]
