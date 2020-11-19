num = int(input())
print(num)
list = [100, 50, 20, 10, 5, 2, 1]
for x in list:
    new_list = int(num/x)
    num = new_list * x
    print('{} nota(s) de R$ {},00'.format(new_list,x))
