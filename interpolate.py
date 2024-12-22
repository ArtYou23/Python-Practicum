import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Исходные данные (например)
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 0.5, 2.5, 3])

# Создаем функцию интерполяции
interp_func = interp1d(x, y, kind='linear') # Можно использовать 'cubic' или другие методы

# Генерируем новые x-значения равномерно распределенные в пределах [min(x), max(x)]
new_x = np.linspace(min(x), max(x), num=50)
#print(new_x)

# Получаем соответствующие y-значения с помощью функции интерполяции
new_y = interp_func(new_x)
#print(new_y)
for i in range(len(new_x)):
    print(new_x[i], new_y[i])

# Строим график оригинальных данных и новых точек
plt.plot(x, y, 'o', label='Исходные точки')
plt.plot(new_x, new_y,'-', label='Интерполированные точки')
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Интерполяция данных')
plt.grid()
plt.show()
