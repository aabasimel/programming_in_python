def remove(lst_tpl):
    return [t for t in lst_tpl if t]   
lst = [('b', 'c'), (), (), ('ab',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
result = remove(lst)
print(result)