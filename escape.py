import math

print("Cálculo de la Velocidad de Escape")
print("Por favor, ingrese los datos en las unidades solicitadas.")

# Entrada de datos
r_km = float(input("Ingrese el radio del planeta en kilómetros: "))
g = float(input("Ingrese la constante gravitacional en m/s²: "))

# Conversión de km a m
r_m = r_km * 1000

# Cálculo de velocidad de escape
ve = math.sqrt(2 * g * r_m)

# Resultado
print(f"La velocidad de escape es {ve:.1f} [m/s]")