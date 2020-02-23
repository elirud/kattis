restaurant_amount = int(input())
for i in range(1, restaurant_amount + 1):
    ingredients = {}
    pizzas = {}
    for _ in range(int(input())):
        _ = input()
        unknown = tuple(input().split()[1:]) # Neither key 
        known = set(input().split()[1:])
        pizzas[unknown] = tuple(known)       # nor value can be a list.
        for ingredient in unknown:
            if ingredient not in ingredients.keys():
                ingredients[ingredient] = known
            else:
                ingredients[ingredient] = ingredients[ingredient] & known
    for foreign in sorted(ingredients.keys()):
        for pizza in pizzas:
            if foreign not in pizza:
                ingredients[foreign].difference_update(set(pizzas[pizza]))
        for translated in sorted(ingredients[foreign]):
            print(f'({foreign}, {translated})')
    if i < restaurant_amount:
        print()
