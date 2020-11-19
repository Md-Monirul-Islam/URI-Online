value = input()
value_int = [int(x) for x in value.split(' ')]
a = value_int[0]
b = value_int[1]
c = value_int[2]
d = value_int[3]
value_new = b > c
value_new = value_new and d > a
value_new = value_new and c+d > a+b
value_new = value_new and c>0 and d>0
value_new = value_new and a % 2 == 0
if (value_new):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")