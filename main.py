import numpy as np
import matplotlib.pyplot as plt

#Masukkan nilai variabel bebas
x = np.arange(1,14)

#Masukkan nilai variabel terikat
y = [245, 200, 150, 110, 100, 80, 70, 60, 50, 45, 43, 42, 41]

n = len(x)
xy = np.zeros(n)
x2 = np.zeros(n)
Sx = np.sum(x)
Sy = np.sum(y)
print(f"x = {x}")
print(f"y = {y}")

plt.plot (x, y, 'ro', linewidth = 3)
plt.xlabel('waktu(s)')
plt.ylabel('CO2 (ppm)')

plt.show()

plt.plot (x, y, linewidth = 3)
plt.plot (x, y, 'ro', linewidth = 3)
plt.xlabel('waktu(s)')
plt.ylabel('CO2 (ppm)')

plt.show()

#Linearisasi
# y = Aexp(Bx) --> ln(y) = ln(A) + Bx --> z = C + Bx
z = np.log(y)

n = len(x)
xz = np.zeros(n)
x2 = np.zeros(n)
Sx = np.sum(x)
Sz = np.sum(z)
print(f"x = {x}")
print(f"z = {z}")

for i in range (0, n):
    xz[i] = x[i]*z[i]
    x2[i] = x[i]*x[i]
Sxz = np.sum(xz)
Sx2 = np.sum(x2)
print(f'Sx = {Sx}')
print(f'Sz = {Sz}')
print(f'Sxz = {Sxz}')
print(f'Sx2 = {Sx2}')

D = (n*Sx2-Sx*Sx)
C = (Sz*Sx2-Sx*Sxz)/D
A = np.exp(C)
B = (n*Sxz-Sx*Sz)/D
print("A = ", A)
print("B = ", B, "\n")
print (f"|[ y = {round(A, 3)} + ({round(B, 3)})x ]|")

m = 0
t = np.arange(np.min(x)-m, np.max(x)+m, 1/1000)
g = C + B*t

plt.plot (x, z, 'ro', linewidth = 3)
plt.xlabel('waktu(s)')
plt.ylabel('ln(CO2 (ppm))')

plt.show()

plt.plot (x, z, linewidth = 3)
plt.plot (x, z, 'ro', linewidth = 3)
plt.xlabel('waktu(s)')
plt.ylabel('ln(CO2 (ppm))')

plt.show()

plt.plot (t, g, linewidth = 3, label=f'z = ln({round(np.exp(C),3)}) + {round(B,3)}x')
plt.plot (x, z, 'ro', linewidth = 3)
plt.xlabel('waktu(s)')
plt.ylabel('ln(CO2 (ppm))')
plt.legend(fontsize = 10, loc = 'lower center')

plt.show()

#Konversi Exponen
#z = C + Bx --> y = Aexp(Bx)
A = np.exp(C)
f = A*np.exp(B*t)

plt.plot (x, y, 'ro', linewidth = 3)
plt.plot (t, f, linewidth = 3, label=f'y = ({round(A,3)})exp({round(B,3)}x)')
plt.xlabel('waktu(s)')
plt.ylabel('CO2 (ppm)')
plt.legend(fontsize = 10, loc = 'lower center')
plt.show()

