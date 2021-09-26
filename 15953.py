T = int(input())
prize = []
for i in range(T):
    a, b = map(int, input().split())
    if a == 0:
        a_money = 0
    elif a == 1:
        a_money = 5000000
    elif a <= 3:
        a_money = 3000000
    elif a <= 6:
        a_money = 2000000
    elif a <= 10:
        a_money = 500000
    elif a <= 15:
        a_money = 300000
    elif a <= 21:
        a_money = 100000
    else:
        a_money = 0
    
    if b == 0:
        b_money = 0
    elif b == 1:
        b_money = 5120000
    elif b <= 3:
        b_money = 2560000
    elif b <= 7:
        b_money = 1280000
    elif b <= 15:
        b_money = 640000
    elif b <= 31:
        b_money = 326000
    else:
        b_money = 0
        
    prize.append(a_money + b_money)
    
for p in prize:
    print(p)