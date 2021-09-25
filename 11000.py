n = int(input())

start = []
end = []
for i in range(n):
  s, e = map(int, input().split())
  start.append(s)
  end.append(e)

for s in start:
  if s in end:
    start.remove(s)
    end.remove(s)
    n -= 1
    
start.sort()
end.sort(reverse=True)

for e in end:
  for s in start:
    if s >= e:
      start.remove(s)
      end.remove(e)
      n -= 1
      break
print(n)