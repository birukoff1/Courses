from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)

chars = ascii_lowercase + ascii_uppercase

def password(max_size):
    global chars
    domen = '@mail.ru'
    
    for i in range(max_size+len(domen)):
        if i<max_size:
            a = chars[random.randint(0, len(chars)-1)]
        else:
            a = domen[i-max_size]
        yield a

N = int(input())

for i in range(5):
    print(''.join(list(password(N))))

#%%

def simple_nums():
    
    complicated = []
    i = 2
    
    while True:
        simple = True
        
        for j in complicated:
            if i%j==0:
                simple = False
        if simple:
            yield i
        
        complicated.append(i)
        i+=1

simple = simple_nums()

List = []

for x in simple:
    List.append(x)
    
    if len(List)==20:
        break
    
print(*List)
    
    