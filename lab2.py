from sympy import *

x = Symbol('x')
y = Function('y')(x)
dy = Derivative(y)

F=((3*(y**2))/x**3)+(x**2)+((dy**2)/x)
print(f"Функция={F}\n")

dFdy = Derivative(F, y)
dFd1y = Derivative(F, dy)
dFdy.doit()
dFd1y.doit()
#Ур эйлера
L = dFdy - Derivative(dFd1y, x)
print(f"Уравнение эйлера={L.doit()}\n")
sol = dsolve(L)
eq1 = sol.subs({x:1, y:2})
eq2 = sol.subs({x:2, y:8.5})
С = solve([eq1, eq2])
print(f"У(х)={sol}\n")
print(f"Найдес коснтанты С1 и С2:")
print(f"Уравнение1={eq1}")
print(f"Уравнение2={eq2}")
print(f"C1 и C2={С}\n")
res = sol.subs(С)
print(f"Итог={res}\n")


 