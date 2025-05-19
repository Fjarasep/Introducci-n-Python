print("Cálculo de utilidades considerando usuarios normales y premium")

# Entradas
P = float(input("Ingrese el precio base de suscripción: "))
Unormal = int(input("Ingrese el número de usuarios normales: "))
Upremium = int(input("Ingrese el número de usuarios premium: "))
GT = float(input("Ingrese el gasto total: "))

# Cálculo
Ppremium = P * 1.5
utilidades = (P * Unormal) + (Ppremium * Upremium) - GT

# Resultado
print(f"Las utilidades del proyecto son: {utilidades:.2f}")