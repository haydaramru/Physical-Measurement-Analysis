import numpy as np
import matplotlib.pyplot as plt

T = np.arange(-55, 151, 1)
k = 10/1000
V = k*T

plt.plot (T, V, linewidth = 3, label=f'Vo = (10mV/°C)T')
plt.xlabel('T(°C)')
plt.ylabel('Vo(volt)')
plt.legend(fontsize = 10, loc = 'lower center')

plt.show()

plt.plot (V, T, linewidth = 3, label=f'T = (100°C/V)Vo')
plt.xlabel('Vo(volt)')
plt.ylabel('T(°C)')
plt.legend(fontsize = 10, loc = 'lower center')

plt.show()

print(np.random.randn(100)*0.5)

# variabel bebas
x = np.arange(-0.55, 1.51, 0.1)
V = x

# variabel terikat
T = 100*V
y = T

for i in range (len(V)):
    if (T[i] > 25):
        T[i] = T[i] + np.random.randn()*0.5
    print(f"{round(V[i], 3)}volt => {round(T[i], 3)}°C")

n = len(x)
xy = np.zeros(n)
x2 = np.zeros(n)
Sx = np.sum(x)
Sy = np.sum(y)

for i in range (0, n):
    xy[i] = x[i]*y[i]
    x2[i] = x[i]*x[i]
Sxy = np.sum(xy)
Sx2 = np.sum(x2)
print(f'Sx = {Sx}')
print(f'Sy = {Sy}')
print(f'Sxy = {Sxy}')
print(f'Sx2 = {Sx2}')

a = (Sy*Sx2-Sx*Sxy)/(n*Sx2-Sx*Sx)
b = (n*Sxy-Sx*Sy)/(n*Sx2-Sx*Sx)
t = np.arange(np.min(x), np.max(x), 1/1000)
f = a + b*t

plt.plot (t, f, linewidth = 3, label=f'T = {round(a,3)}°C + ({round(b,3)}°C/V)Vo')
plt.plot (x, y, 'ro', linewidth = 3)
plt.xlabel('Vo(volt)')
plt.ylabel('Suhu (°C)')
plt.legend(fontsize = 10, loc = 'lower center')

plt.show()

