import math
try:
    raio_circulo = float(input("digite o raio: "))

    area_circulo = math.pi * (raio_circulo ** 2)
except:
    print("erro")

print(area_circulo) 