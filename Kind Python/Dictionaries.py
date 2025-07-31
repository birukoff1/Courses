things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

N = 1000*int(input())

weight_sorted = [int(value) for value in things.values()]
weight_sorted.sort(reverse=True)


result = ''
for weight in weight_sorted:
    if N-weight >= 0:
        N-=weight
        
        for key, value in things.items():
            if weight == value:
                result+=f'{key} '

print(result.rstrip(' '))
