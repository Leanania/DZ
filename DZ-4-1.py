# lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
lst = []
l = lst[:3]
m = lst[3:]
n = lst[:2]
o = lst[2:]
p = lst[:1]
r = lst[1:]
if len(lst) == 3:
    print([n, o])
elif len(lst) == 6:
    print([l, m])
elif len(lst) == 0:
    print([p, r])