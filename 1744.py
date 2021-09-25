n = int(input())
p_nums = []
n_nums = []
new_nums = []
for _ in range(n):
  x = int(input())
  if x >= 0:
    p_nums.append(x)
  else:
    n_nums.append(x)

n_nums.sort()
p_nums.sort(reverse=True)

if p_nums:
  if len(n_nums) % 2 == 1 and p_nums[-1] == 0:
    n_nums.pop()
    p_nums.pop()

if len(n_nums) % 2 == 1:
  new_nums.append(n_nums.pop())

for i in range(0, len(n_nums), 2):
  new_nums.append(n_nums[i] * n_nums[i + 1])

if len(p_nums) % 2 == 1:
  new_nums.append(p_nums.pop())

for i in range(0, len(p_nums), 2):
  if p_nums[i] * p_nums[i + 1] > p_nums[i] + p_nums[i + 1]:
    new_nums.append(p_nums[i] * p_nums[i + 1])
  else:
    new_nums.append(p_nums[i] + p_nums[i + 1])

print(sum(new_nums))