a = int(input('Введите пятизначное число:'))
f = 10000
x = 1000
y = 100
z = 10
left, right = divmod(a, f)
n, m = divmod(right, x)
n1, m1 = divmod(m, y)
n2, m2 = divmod(m1, z)
left, n, n1, n2, m2 = m2, n2, n1, n, left
print(left, n, n1, n2, m2)
