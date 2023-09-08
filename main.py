import sympy
# создаем символьные переменные
a1 = sympy.symbols('a1')
a2 = sympy.symbols('a2')
h = sympy.symbols('h')
t = sympy.symbols('t')
x1 = sympy.Function('x1')(t)
x2 = sympy.Function('x2')(t)
b1 = sympy.symbols('b1')
b2 = sympy.symbols('b2')
T1 = sympy.symbols('T1')
xx = sympy.symbols('xx') # xx это x1'
u = sympy.Function('u')(x1 , x2) # управление
# задаем модель
dx1 = a1 * x1 - b1 * x1 * x2
dx2 = -a2 * x2 + b2 * x1 * x2 + u
psi = x1 - xx # цель
# Дискретизация модели
f1 = x1 + h * dx1
f2 = x2 + h * dx2

print('')
print('')
print('Модель: ')
print('dx1/dt =', dx1)
print('dx2/dt =', dx2)
print('Цель ψ =', psi, '--> 0')
print('')
print('Дискретизированные f1 и f2:')
print('f1 =', f1)
print('f2 =', f2)
print('')
lagrangian = T1 * psi + f2 - xx
print(lagrangian)
print('Уравнение Эйлера-Лагранжа:', lagrangian)
print('')
# Выразить управление u из уравнения Эйлера-Лагранжа
u_solution = sympy.solve(lagrangian, u)
# Вывести решение
print('Управление u =', u_solution)
