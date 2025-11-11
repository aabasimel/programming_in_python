s="())[]{}"

mapping = {'2': '4', '3': '6', '4': '8'}

for cha in s:
    if cha in mapping:
        print(cha)