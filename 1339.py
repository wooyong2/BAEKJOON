import operator

n = int(input())
words = []
alp = {}
for _ in range(n):
    word = input()
    for i in range(len(word)):
        if word[i] in alp:
            alp[word[i]] += 10 ** (len(word) - i - 1)
        else:
            alp[word[i]] = 10 ** (len(word) - i - 1)
alp = sorted(alp.items(), key=operator.itemgetter(1), reverse=True)
num = 9
ans = 0
for i in alp:
    ans += i[1] * num
    num -= 1
print(ans)