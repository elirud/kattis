from math import ceil

jobs, cap = map(int, input().split())

max_running = 0
running = []

for _ in range(jobs):
    time = int(input())
    running.append(time)
    for t in running:
        if abs(time - t) >= 1000:
            running.remove(t)
        else:
            break
    max_running = len(running) if len(running) > max_running else max_running

print(ceil(max_running / cap))
