from math import ceil, log2

answer = 0
full_memory = int(input()) * 1024
for i in range(10_000, 0, -1):
    if (ceil((700 + ceil(log2(i))) / 8) * i) >= full_memory:
        answer = i - 1
print(answer)
