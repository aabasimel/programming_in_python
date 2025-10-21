# CTMS-14
# a7 p4.py
# Ahmed Abasimel
# aabasimel@constructor.university

def remove(lst_tpl):
    return [t for t in lst_tpl if t]   
lst = [('b', 'c'), (), (), ('ab',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
result = remove(lst)
print(result)