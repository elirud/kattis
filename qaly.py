qaly = 0

for _ in range(int(input())):
    n = list(map(float, input().split()))
    qaly += n[0]*n[1]

print(f'{qaly:.3f}')
