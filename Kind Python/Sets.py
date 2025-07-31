lst_in = ['Пушкин: Сказка о рыбаке и рыбке', 'Есенин: Письмо к женщине', 'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']

list_new = [value.split(':') for value in lst_in]
for index in range(len(list_new)):
    list_new[index][1] = list_new[index][1].lstrip(' ')

d = {author: {book for a, book in list_new if a==author} for author in set([subauthor[0] for subauthor in list_new])}


print(*d.items())