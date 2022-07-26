n = [50, 50, 70, 80, 100]
num_sum = 0
cnt = 0

for i in n:
    num_sum += i
    avg = num_sum / len(n)

for i in n:
    if i > avg:
        cnt += 1

print(cnt / len(n) * 100, '%')