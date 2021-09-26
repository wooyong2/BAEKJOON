import itertools

N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
op_list = []

for i in range(len(opers)):
    
    # 덧셈
    if i == 0:
        for j in range(opers[i]):
            op_list.append('+')
    # 뺄셈
    if i == 1:
        for j in range(opers[i]):
            op_list.append('-')
    # 곱셈
    if i == 2:
        for j in range(opers[i]):
            op_list.append('*')
    # 나눗셈
    if i == 3:
        for j in range(opers[i]):
            op_list.append('//')

all_oper = list(itertools.permutations(op_list))
all_oper = set(all_oper)
all_oper = list(all_oper)

ans = []

for oper in all_oper:
    tmp = nums[0]
    for i in range(len(oper)):
        if oper[i] == '+':
            tmp = tmp + nums[i + 1]
        if oper[i] == '-':
            tmp = tmp - nums[i + 1]
        if oper[i] == '*':
            tmp = tmp * nums[i + 1]
        if oper[i] == '//':
            if (tmp < 0 and nums[i + 1] > 0) or (tmp > 0 and nums[i + 1] < 0):
                tmp = abs(tmp) // abs(nums[i + 1])
                tmp = -tmp
            else:
                tmp = tmp // nums[i + 1]
    ans.append(tmp)
    
print(max(ans))
print(min(ans))