def counter_add(n):
    
    def inner_function(x):
        
        return x+n
    
    return inner_function()


k = int(input())

cnt = counter_add(2)

print(cnt(k))