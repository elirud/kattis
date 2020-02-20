min_ = int(input())
max_ = int(input())
target = int(input())
sum_ = 0

for n in range(min_, max_ + 1, 1):
    sum_ = 0
    for l in str(n):
        sum_ = sum_ + int(l)
    if sum_ == target:
        print(str(n))
        break

for m in range(max_, min_ - 1, -1):
    sum_ = 0
    for l in str(m):
        sum_ = sum_ + int(l)
    if sum_ == target:
        print(str(m))
        break
