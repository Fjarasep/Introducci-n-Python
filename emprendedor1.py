print("Cálculo de utilidades de un proyecto")

# Entradas
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese el gasto total: "))

# Cálculo de utilidades
utilidades = P * U - GT

# Resultado
print(f"Las utilidades del proyecto son: {utilidades:.2f}")
