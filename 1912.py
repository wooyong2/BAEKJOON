n = int(input())
seq = list(map(int, input().split()))


sum_list = [seq[0]]
for i in range(1, len(seq)):
    sum_list.append(max(sum_list[i - 1] + seq[i], seq[i]))
    
print(max(sum_list))