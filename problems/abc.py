inp = dict(zip('ABC', map(str, sorted(map(int, input().split())))))
print(' '.join(inp[s] for s in input()))
