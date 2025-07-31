lst_in = [

          'Номер;Имя;Оценка;Зачет',

          '1;Портос;5;Да',

          '2;Арамис;3;Да',

          '3;Атос;4;Да',

          '4;д\'Артаньян;2;Нет',

          '5;Балакирев;1;Нет'

         ]

key = 'Имя;Зачет;Оценка;Номер'.split(';')


Tuple = list(list(s.split(';')) for s in lst_in)

for i in range(len(Tuple)):
    for j in range(len(Tuple[i])):
        try:
            Tuple[i][j] = int(Tuple[i][j])
        except:
            pass


t_sorted = tuple([tuple(sorted(x, key = lambda s: [key.index(x) for x in Tuple[0]][x.index(s)])) for x in Tuple])


for x in t_sorted:
    print(x)

t_true = (('Имя', 'Зачет', 'Оценка', 'Номер'), ('Портос', 'Да', 5, 1), ('Арамис', 'Да', 3, 2), ('Атос', 'Да', 4, 3), ("д'Артаньян", 'Нет', 2, 4), ('Балакирев', 'Нет', 1, 5))
for x in t_true:
    print(x)
    
t_true == t_sorted