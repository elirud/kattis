for _ in range(int(input())):
    length, ants = map(int, input().split())
    positions = []
    got_positions = False
    
    # Since input could separate ants positions by newline, 
    # I could not figure out how to do something like the row below.
    
    # positions = [x for x in map(int(input().split()))]
    
    # So I ended up using a bool to check if we got all positions.
    
    while not got_positions:
        positions += list(map(int, input().split()))
        if len(positions) == ants:
            got_positions = True 
    min_ = max([min(x, length - x) for x in positions])
    max_ = max([max(x, length - x) for x in positions])
    print(min_, max_)