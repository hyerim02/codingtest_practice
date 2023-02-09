import math

def solution(denum1, num1, denum2, num2):
    num = denum1 * num2 + denum2 * num1
    denum = num1 * num2
    gcd = math.gcd(num, denum)
    return [num//gcd, denum//gcd]