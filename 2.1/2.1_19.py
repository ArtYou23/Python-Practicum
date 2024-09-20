name = input()
cost = int(input())
weight = int(input())
money = int(input())
q1 = len('================Чек================')
qq1 = q1 - 6 - len(name)
print('================Чек================')
print('Товар:', ' ' * qq1, name, sep='')
qq2 = q1 - 5 - 11 - len(str(cost)) - len(str(weight))
print('Цена:', ' ' * qq2, weight, 'кг * ', cost, 'руб/кг', sep='')
qq3 = q1 - 6 - len(str(cost * weight)) - 3
print('Итого:', ' ' * qq3, cost * weight, 'руб', sep='')
qq4 = q1 - 8 - len(str(money)) - 3
print('Внесено:', ' ' * qq4, money, 'руб', sep='')
qq5 = q1 - 6 - len(str(money - cost * weight)) - 3
print('Сдача:', ' ' * qq5, money - cost * weight, 'руб', sep='')
print('===================================')