i = dict(zip(['start', 'found', 'needed'], map(int, input().split())))
bottles = i['start'] + i['found']
sodas = 0

while bottles >= i['needed']:
    sodas += bottles // i['needed']
    bottles = bottles // i['needed'] + bottles % i['needed']

print(sodas)
