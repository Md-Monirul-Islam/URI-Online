a = int(input())
b = int(input())
c = int(input())
d = int(input())
value_new = b > c
value_new = value_new and d > a
value_new = value_new and c+d > a+b
value_new = value_new and c>0 and d>0
value_new = value_new and a % 2 == 0
if (value_new):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")