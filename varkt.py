import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


C = 189
A = 250 - 180
A2 = 219 - 180
gamma = 0.08
gamma2 = 0.1
omega = (2 * np.pi / 20)
omega2 = 2 * np.pi / 6
arr = np.linspace(0,0,1)
arro = np.linspace(0,0,1)
t_values = np.linspace(43, 59, num=100)
t_values2 = np.linspace(64, 70, num=50)
t_values3 = np.linspace(72, 124, num=2)
t_values4 = np.linspace(182.02, 98, num=2)
t_values5 = np.linspace(133, 133, num=1)
t_values6 = np.linspace(0, 0, num=1)

arr11 = np.linspace(63.9,63.9,1)
arr12 = np.linspace(218.9,218.9,1)

y_values = 180 + A * np.exp(-gamma * t_values * ((t_values-43)/43)) * np.cos(omega * t_values * ((t_values-43)/43))
y2_values = 180 + A2 * np.exp(-gamma2 * t_values2 * ((t_values2-64)/64)) * np.cos(omega * t_values2 * ((t_values2-64)/64))


res = np.r_[arr, t_values]
res2 = np.r_[arro, y_values]

res11 = np.r_[res, arr11]
res12 = np.r_[res2, arr12]

res111 = np.r_[res11, t_values2]
res112 = np.r_[res12, y2_values]

res1111 = np.r_[res111, t_values3]
res1112 = np.r_[res112, t_values4]

res11111 = np.r_[res1111, t_values5]
res11112 = np.r_[res1112, t_values6]
#print(len(res11), len(res12))


# Создаем функцию интерполяции
interp_func = interp1d(res11111, res11112, kind='linear') # Можно использовать 'cubic' или другие методы

# Генерируем новые x-значения равномерно распределенные в пределах [min(x), max(x)]
new_x = np.linspace(min(res11111), max(res11111), num=300)
#print(new_x)

# Получаем соответствующие y-значения с помощью функции интерполяции
new_y = interp_func(new_x)
#print(new_y)
c, sm = 0, 0
for i in range(len(new_x)):
    if new_x[i] >= 43 and new_x[i] <= 59:
        c += 1
        sm += new_y[i]
print(sm / c)


plt.figure(figsize=(23,5))
plt.plot(new_x, new_y)
#plt.title('Затухающие Колебания')
#plt.xlabel('Время')
#plt.ylabel('Амплитуда')
#plt.axhline(y=195, color='r', linestyle='--', label='Конечная точка (y=195)')
#plt.axhline(y=250, color='g', linestyle='--', label='Начальная точка (y=250)')
#plt.axhline(y=147, color='g', linestyle='--', label='Серединная точка (y=147)')
#plt.legend()
plt.grid()
plt.xlim(0,140)
plt.ylim(0,260)
plt.show()

