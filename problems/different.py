import sys

for s in sys.stdin.readlines():
    a, b = map(int, s.split())
    print(abs(a - b))
