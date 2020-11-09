from collections import Counter

def solution(n, d):
    str_num = ''
    for i in range(n+1):
        str_num += str(i*i)
        
    return Counter(str_num)[str(d)]