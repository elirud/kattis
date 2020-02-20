import functools

for _ in range(int(input())):
  d = list(map(int, input().split()))
  avg = functools.reduce(lambda a, b: a + b, d[1:]) / d[0]
  print(f'{100 * len(list(filter(lambda x: x > avg, d[1:]))) / d[0]:.3f}' + '%')
