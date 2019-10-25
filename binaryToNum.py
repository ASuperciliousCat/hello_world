def numToBaseB(N, B):
    if N <= 0:
        return '0'
    if N//B == 0:
        return str(N % B)
    return numToBaseB(N//B, B) + str(N % B)

def baseBToNum(S, B):
    if S == '':
        return 0
    return B * baseBToNum(S[:-1], B) + int(S[-1])

def baseToBase(B1, B2, SinB1):
    if B1 == 0 or B2 == 0 or SinB1 == '':
        return ''
    num = baseBToNum(SinB1, B1)
    base = numToBaseB(SinB1, B2)
    return base

def add(S, T):
    if S == '' or T == '':
        return ''
    addi = add(baseBToNum(S, 2), baseBToNum(T, 2))
    return numToBaseB(addi, 2)

def addB(x, y, carry_in):
    if len(x) != len(y):
        maxi = max(len(x), len(y))
        mini = min(len(x), len(y))
        if len(x) > len(y):
            y = (maxi-mini)*'0' + y
        if len(y) > len(x):
            x = (maxi-mini)*'0' + x
    if x == '' and y == '':
        return  carry_in + '' 
    if int(x[-1]) + int(y[-1]) + int(carry_in) == 2:
        carry_in == '1'
        return addB(x[:-1], y[:-1], carry_in) + '0'
    if int(x[-1]) + int(y[-1]) + int(carry_in) == 1:
        carry_in == '0'
        return addB(x[:-1], y[:-1], carry_in) + '1'
    if int(x[-1]) + int(y[-1]) + int(carry_in) == 3:
        carry_in == '1'
        return addB(x[:-1], y[:-1],carry_in) + '1'
