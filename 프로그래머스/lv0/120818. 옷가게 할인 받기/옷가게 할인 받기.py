def solution(price):
    if price >= 500000:
        answer=int(price*0.8)
    elif price >= 300000 and price < 500000:
        answer=int(price * 0.9)
    elif price >= 100000 and price < 300000:
        answer=int(price * 0.95)
    else:
        answer=price
    return answer    