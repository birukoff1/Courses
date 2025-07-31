lst_in = ['Главная home',  'Python learn-python',  'Java learn-java',  'PHP learn-php']
lst_in = [x.split() for x in lst_in]
print(lst_in)

tuple_out = ()

for x in lst_in:
    tuple_out+= (tuple(x),)

print(tuple_out)